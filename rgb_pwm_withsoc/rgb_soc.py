#!/usr/bin/env python3

from migen import *

from migen.genlib.io import CRG

from litex.build.generic_platform import *
from litex.build.xilinx import XilinxPlatform

from litex.soc.integration.soc_core import *
from litex.soc.integration.builder import *
from litex.soc.cores import dna, xadc
from litex.soc.cores.spi import SPIMaster
from litex.soc.interconnect.csr import CSRStorage, AutoCSR

# IOs ----------------------------------------------------------------------------------------------

_io = [

    ("user_rgb_led", 0,
        Subsignal("r", Pins("N16")),
        Subsignal("g", Pins("R11")),
        Subsignal("b", Pins("G14")),
        IOStandard("LVCMOS33"),
    ),

    ("clk100", 0, Pins("E3"), IOStandard("LVCMOS33")),

    ("cpu_reset", 0, Pins("C12"), IOStandard("LVCMOS33")),

    ("serial", 0,
        Subsignal("tx", Pins("D4")),
        Subsignal("rx", Pins("C4")),
        IOStandard("LVCMOS33"),
    ),

    ("adxl362_spi", 0,
        Subsignal("cs_n", Pins("D15")),
        Subsignal("clk", Pins("F15")),
        Subsignal("mosi", Pins("F14")),
        Subsignal("miso", Pins("E15")),
        IOStandard("LVCMOS33")
    ),

]

class RGBLed(Module, AutoCSR):
    def __init__(self, pads):
        self.red = CSRStorage(len(pads.r))
        self.green = CSRStorage(len(pads.g))
        self.blue = CSRStorage(len(pads.b))

        self.comb += [
            pads.r.eq(self.red.storage),
            pads.g.eq(self.green.storage),
            pads.b.eq(self.blue.storage)
        ]
        # self.submodules.r = PWM(pads.r)
        # self.submodules.g = PWM(pads.g)
        # self.submodules.b = PWM(pads.b)

# Platform -----------------------------------------------------------------------------------------

class Platform(XilinxPlatform):
    default_clk_name   = "clk100"
    default_clk_period = 1e9/100e6

    def __init__(self):
        XilinxPlatform.__init__(self, "xc7a100t-csg324-1", _io, toolchain="vivado")

# Design -------------------------------------------------------------------------------------------

# Create our platform (fpga interface)
platform = Platform()

# Create our soc (fpga description)
class BaseSoC(SoCCore):
    def __init__(self, platform):
        sys_clk_freq = int(100e6)

        # SoC with CPU
        SoCCore.__init__(self, platform,
            cpu_type                 = "vexriscv",
            clk_freq                 = 100e6,
            ident                    = "LiteX CPU Test SoC", ident_version=True,
            integrated_rom_size      = 0x8000,
            integrated_main_ram_size = 0x4000)

        # Clock Reset Generation
        self.submodules.crg = CRG(platform.request("clk100"), ~platform.request("cpu_reset"))

        # FPGA identification
        self.submodules.dna = dna.DNA()
        self.add_csr("dna")

        # FPGA Temperature/Voltage
        self.submodules.xadc = xadc.XADC()
        self.add_csr("xadc")

        # RGB Led
        self.submodules.rgbled  = RGBLed(platform.request("user_rgb_led",  0))
        self.add_csr("rgbled")

soc = BaseSoC(platform)

# Build --------------------------------------------------------------------------------------------

builder = Builder(soc, output_dir="build", csr_csv="csr.csv")
builder.build(build_name="top")

