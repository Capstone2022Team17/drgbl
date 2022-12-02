"""
HBM Port Access is meant to allow the HBM to be written over AXI Lite
following cues from the LiteDRAM code
"""
# pylint: disable = unused-wildcard-import
from migen import *

# pylint: disable = unused-wildcard-import
from litex.soc.interconnect.csr import *


ONE_BIT_WIDE = 1
TWO_BITS_WIDE = 2


class HBMReadAndWriteSM(Module, AutoCSR):
    """
    Fill in this comment as the code develops
    """

    # Here, axi_port is an AXILite object, to be used with AXILite2AXI.
    def __init__(self, axi_port):

        self.perform_write = CSRStorage(ONE_BIT_WIDE, description="Perform a write")
        self.perform_read = CSRStorage(ONE_BIT_WIDE, description="Perform a read")
        self.write_resp = CSRStatus(TWO_BITS_WIDE, description="Response after writing")
        self.read_resp = CSRStatus(TWO_BITS_WIDE, description="Response after read")
        self.strb_readwrite = CSRStorage(
            axi_port.data_width // 8,
            description="Indicates the byte lanes that hold valid data",
        )
        self.address_readwrite = CSRStorage(
            axi_port.address_width, description="Address to perform read or write at"
        )
        self.data_writein = CSRStorage(
            axi_port.data_width, description="Data to write after performing write"
        )
        self.data_readout = CSRStatus(
            axi_port.data_width, description="Data to read after performing read"
        )
        self.exec_read_done = CSRStatus(
            ONE_BIT_WIDE, description="High if done performing read"
        )
        self.exec_write_done = CSRStatus(
            ONE_BIT_WIDE, description="High if done performing write"
        )
        self.acknowledge_readwrite = CSRStorage(
            ONE_BIT_WIDE,
            description="Acknowledge to state machine read or write happened",
        )

        hbm_port_fsm = FSM(reset_state="WAIT_INSTRUCTION")
        self.submodules.hbm_port_fsm = hbm_port_fsm

        # Set address, strobe, and possibly data_writein BEFORE performing read or write
        hbm_port_fsm.act(
            "WAIT_INSTRUCTION",
            If(
                self.perform_read.storage,
                NextState("PERFORM_READ_COMMAND"),
            )
            .Elif(
                self.perform_write.storage,
                NextState("PREPARE_WRITE_COMMAND"),
            )
            .Else(
                NextState("WAIT_INSTRUCTION"),
            ),
        )
        hbm_port_fsm.act(
            "PREPARE_WRITE_COMMAND",
            axi_port.aw.addr.eq(self.address_readwrite.storage),
            axi_port.aw.valid.eq(1),
            axi_port.w.data.eq(self.data_writein.storage),
            axi_port.w.strb.eq(self.strb_readwrite.storage),
            axi_port.w.valid.eq(1),
            If(axi_port.aw.ready, NextState("PREPARE_WRITE"),).Else(
                NextState("PREPARE_WRITE_COMMAND"),
            ),
        )
        hbm_port_fsm.act(
            "PREPARE_WRITE",
            axi_port.w.data.eq(self.data_writein.storage),
            axi_port.w.strb.eq(self.strb_readwrite.storage),
            axi_port.aw.addr.eq(0),
            axi_port.aw.valid.eq(0),
            axi_port.w.valid.eq(1),
            If(axi_port.w.ready, NextState("PREPARE_W_RESPONSE"),).Else(
                NextState("PREPARE_WRITE"),
            ),
        )
        hbm_port_fsm.act(
            "PREPARE_W_RESPONSE",
            axi_port.w.data.eq(self.data_writein.storage),
            axi_port.aw.addr.eq(self.address_readwrite.storage),
            axi_port.w.valid.eq(0),
            axi_port.w.strb.eq(0),
            axi_port.b.ready.eq(1),
            If(axi_port.b.valid, NextState("DONE_WRITE")).Else(
                NextState("PREPARE_W_RESPONSE")
            ),
        )
        hbm_port_fsm.act(
            "DONE_WRITE",
            self.exec_write_done.status.eq(1),
            self.write_resp.status.eq(axi_port.b.resp),
            If(self.acknowledge_readwrite.storage, NextState("WAIT_INSTRUCTION"),).Else(
                NextState("DONE_WRITE"),
            ),
        )
        hbm_port_fsm.act(
            "PERFORM_READ_COMMAND",
            axi_port.ar.valid.eq(1),
            axi_port.ar.addr.eq(self.address_readwrite.storage),
            If(axi_port.ar.ready, NextState("PERFORM_READ")).Else(
                NextState("PERFORM_READ_COMMAND")
            ),
        )
        hbm_port_fsm.act(
            "PERFORM_READ",
            axi_port.r.ready.eq(1),
            axi_port.ar.addr.eq(self.address_readwrite.storage),
            If(axi_port.r.valid, NextState("DONE_READ")).Else(
                NextState("PERFORM_READ")
            ),
        )
        hbm_port_fsm.act(
            "DONE_READ",
            self.exec_read_done.status.eq(1),
            self.data_readout.status.eq(axi_port.r.data),
            self.read_resp.status.eq(axi_port.r.resp),
            If(self.acknowledge_readwrite.storage, NextState("WAIT_INSTRUCTION"),).Else(
                NextState("DONE_READ"),
            ),
        )

    #         def write(self, addr, data, strb=None):
    #     if strb is None:
    #         strb = 2**len(self.w.strb) - 1
    #     # aw + w
    #     yield self.aw.valid.eq(1)
    #     yield self.aw.addr.eq(addr)
    #     yield self.w.data.eq(data)
    #     yield self.w.valid.eq(1)
    #     yield self.w.strb.eq(strb)
    #     yield
    #     while not (yield self.aw.ready):
    #         yield
    #     yield self.aw.valid.eq(0)
    #     yield self.aw.addr.eq(0)
    #     while not (yield self.w.ready):
    #         yield
    #     yield self.w.valid.eq(0)
    #     yield self.w.strb.eq(0)
    #     # b
    #     yield self.b.ready.eq(1)
    #     while not (yield self.b.valid):
    #         yield
    #     resp = (yield self.b.resp)
    #     yield self.b.ready.eq(0)
    #     return resp

    # def read(self, addr):
    #     # ar
    #     yield self.ar.valid.eq(1)
    #     yield self.ar.addr.eq(addr)
    #     yield
    #     while not (yield self.ar.ready):
    #         yield
    #     yield self.ar.valid.eq(0)
    #     # r
    #     yield self.r.ready.eq(1)
    #     while not (yield self.r.valid):
    #         yield
    #     data = (yield self.r.data)
    #     resp = (yield self.r.resp)
    #     yield self.r.ready.eq(0)
    #     return (data, resp)


class HBMAXILiteAccess(Module, AutoCSR):
    """
    Fill in this comment as the code develops
    """

    # Here, axi_port is one of the 32 AXIInterface objects from the hbm variable.
    def __init__(self, axi_port):

        # This is the declaration of all the csr registers we will read and write to.
        # For now, this is simply a way to connect to all the registers of AXI Lite.
        # A migen state machine will likely be applied later for these.

        # CSR Status = What to read from
        # CSR Storage = What to write to

        # Write command
        self.aw_valid = CSRStorage(ONE_BIT_WIDE, description="Write Command valid")
        self.aw_ready = CSRStatus(ONE_BIT_WIDE, description="Write Command ready")
        self.aw_addr = CSRStorage(
            axi_port.address_width, description="Write Command address"
        )

        # Write
        self.w_valid = CSRStorage(ONE_BIT_WIDE, description="Write valid")
        self.w_ready = CSRStatus(ONE_BIT_WIDE, description="Write ready")
        self.w_data = CSRStorage(axi_port.data_width, description="Write data")
        self.w_strb = CSRStorage(
            axi_port.data_width // 8,
            description="Write strobe: Indicates the byte lanes that hold valid data",
        )

        # Write response
        self.b_valid = CSRStatus(ONE_BIT_WIDE, description="Write response valid")
        self.b_ready = CSRStorage(ONE_BIT_WIDE, description="Write response ready")
        self.b_resp = CSRStatus(
            2,
            description="Write response: This indicates the status of the write transaction",
        )

        # Read command
        self.ar_valid = CSRStorage(ONE_BIT_WIDE, description="Read Command valid")
        self.ar_ready = CSRStatus(ONE_BIT_WIDE, description="Read Command ready")
        self.ar_addr = CSRStorage(
            axi_port.address_width, description="Read Command address"
        )

        # Read
        self.r_valid = CSRStatus(ONE_BIT_WIDE, description="Read valid")
        self.r_ready = CSRStorage(ONE_BIT_WIDE, description="Read ready")
        self.r_data = CSRStatus(axi_port.data_width, description="Read data")
        self.r_resp = CSRStatus(
            2, description="Read response: Indicates the status of the read response"
        )

        # All other variables for HBM controller are set to default values here, as in AXILite2AXI

        burst_type = "INCR"  # Comment in AXILite2AXI says the following:

        # Burst type has no meaning as we use burst length of 1, but AXI slaves may require certain
        # type of bursts, so it is probably safest to use INCR in general.

        burst_type = {
            "FIXED": 0b00,
            "INCR": 0b01,
            "WRAP": 0b10,
        }[burst_type]

        burst_size = log2_int(axi_port.data_width // 8)

        # Comment from AXILiteInterface:
        # present for interconnect with other cores but not used by LiteX.
        prot = 0

        # Write command I/O's
        # Set with variables
        axi_port.aw.valid.eq(self.aw_valid.storage)
        self.aw_ready.status.eq(axi_port.aw.ready)
        axi_port.aw.addr.eq(self.aw_addr.storage)

        # Set with default values
        axi_port.aw.burst.eq(burst_type)
        axi_port.aw.len.eq(0)  # 1 transfer per burst
        axi_port.aw.size.eq(burst_size)
        axi_port.aw.lock.eq(0)  # Normal access
        axi_port.aw.prot.eq(prot)
        axi_port.aw.cache.eq(0b0011)  # Normal Non-cacheable Bufferable
        axi_port.aw.qos.eq(
            0
        )  # (Quality of Service) Identifier sent for each write transaction
        axi_port.aw.id.eq(0)  #

        # Write I/O's
        # Set with variables
        axi_port.w.valid.eq(self.w_valid.storage)
        self.w_ready.status.eq(axi_port.w.ready)
        axi_port.w.data.eq(self.w_data.storage)
        axi_port.w.strb.eq(self.w_strb.storage)

        # Set with default values
        axi_port.w.last.eq(1)  # Signal indicates last transfer in a write burst

        # Write response I/O's
        # Set with variables
        self.b_valid.status.eq(axi_port.b.valid)
        axi_port.b.ready.eq(self.b_ready.storage)
        self.b_resp.status.eq(axi_port.b.resp)

        # Read command I/O's
        # Set with variables
        axi_port.ar.valid.eq(self.ar_valid.storage)
        self.ar_ready.status.eq(axi_port.ar.ready)
        axi_port.ar.addr.eq(self.ar_addr.storage)

        # Set with default values
        axi_port.ar.burst.eq(burst_type)
        axi_port.ar.len.eq(0)  # 1 transfer per bit
        axi_port.ar.size.eq(burst_size)
        axi_port.ar.lock.eq(0)  # Normal access
        axi_port.ar.prot.eq(prot)
        axi_port.ar.cache.eq(0b0011)  # Normal Non-cacheable Bufferable
        axi_port.ar.qos.eq(0)
        axi_port.ar.id.eq(0)

        # Read I/O's
        # Set with variables
        self.r_valid.status.eq(axi_port.r.valid)
        axi_port.r.ready.eq(self.r_ready.storage)
        self.r_data.status.eq(axi_port.r.data)
        self.r_resp.status.eq(axi_port.r.resp)
