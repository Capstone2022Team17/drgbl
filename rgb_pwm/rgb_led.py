from migen import *
from litex_boards.platforms import digilent_nexys4ddr

from litex.build.generic_platform import *

_rgb_io = {("rgb_led",  0, Pins("R12"), IOStandard("LVCMOS33")),
    ("rgb_led",  1, Pins("M16"), IOStandard("LVCMOS33")),
    ("rgb_led",  2, Pins("N15"), IOStandard("LVCMOS33")),
    ("rgb_led",  3, Pins("G14"), IOStandard("LVCMOS33")),
    ("rgb_led",  4, Pins("R11"), IOStandard("LVCMOS33")),
    ("rgb_led",  5, Pins("N16"), IOStandard("LVCMOS33")),}

class RGB_led(Module):
    def __init__(self) -> None:
        super().__init__()


def main():
    nexys_platform = digilent_nexys4ddr.Platform()
    nexys_platform.add_extension(_rgb_io)

    rgb_module = RGB_led()

    for idx in range(6):
        switch = nexys_platform.request("user_sw", idx)
        led = nexys_platform.request("rgb_led", idx)
        rgb_module.comb += led.eq(switch)

    nexys_platform.build(rgb_module)

    programmer = nexys_platform.create_programmer()

    programmer.load_bitstream("build/top.bit")

if __name__ == "__main__":
    main()