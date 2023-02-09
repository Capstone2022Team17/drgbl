from migen import *

from litex_boards.targets.HBMPortAccess import *



from litex.soc.interconnect.axi import AXIInterface

def simulate_write():
    yield dut.perform_write.storage.eq(1)
    yield dut.address_readwrite.storage.eq(0x0000_0001)
    yield dut.data_writein.storage.eq(0xDEADBEEF)
    while not (yield myAxi.aw.valid):
        yield
    yield myAxi.aw.ready.eq(1)
    yield
    while not (yield myAxi.w.valid):
        yield
    yield myAxi.aw.ready.eq(0)
    yield myAxi.w.ready.eq(1)
    yield
    yield myAxi.w.ready.eq(0)
    yield myAxi.b.valid.eq(1)
    while not (yield myAxi.b.ready):
        yield
    yield myAxi.b.valid.eq(0)
    yield dut.acknowledge_readwrite.storage.eq(1)
    yield 


def simulate_read():
    pass

myAxi = AXIInterface(data_width=256, address_width=33)

dut = HBMReadAndWriteSM(myAxi)

run_simulation(dut, simulate_write(), vcd_name="sim.vcd")