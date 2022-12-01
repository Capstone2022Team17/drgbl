from migen import *
from litex_boards.platforms import digilent_nexys4ddr

from litex.build.generic_platform import *

_rgb_io = {
    ("rgb_led", 0, Pins("R12"), IOStandard("LVCMOS33")),
    ("rgb_led", 1, Pins("M16"), IOStandard("LVCMOS33")),
    ("rgb_led", 2, Pins("N15"), IOStandard("LVCMOS33")),
    ("rgb_led", 3, Pins("G14"), IOStandard("LVCMOS33")),
    ("rgb_led", 4, Pins("R11"), IOStandard("LVCMOS33")),
    ("rgb_led", 5, Pins("N16"), IOStandard("LVCMOS33")),
}


class RGB_led(Module):
    def __init__(self) -> None:
        super().__init__()


def main():
    nexys_platform = digilent_nexys4ddr.Platform()

    nexys_platform.add_extension(_rgb_io)

    rgb_module = RGB_led()
    rgb_module.ticks = Signal(32)
    rgb_module.RedCount = Signal(8)
    rgb_module.GreenCount = Signal(8)
    rgb_module.BlueCount = Signal(8)
    rgb_module.pwmCount = Signal(8)
    rgb_module.ticked_up = Signal(1)
    rgb_module.delay_count = Signal(32)
    rgb_module.red_inc = Signal(1)
    rgb_module.blue_inc = Signal(1)
    rgb_module.green_inc = Signal(1)


    rgb_fsm = FSM(reset_state="IDLE")
    rgb_module.submodules += rgb_fsm

    leds = []

    delay = 0xfff

    ctr_leds = []
    for idx in range(16):
        ctr_leds.append(nexys_platform.request("user_led", idx))

    for idx in range(6):
        switch = nexys_platform.request("user_sw", idx)
        led = nexys_platform.request("rgb_led", idx)
        leds.append(led)
        # rgb_module.comb += led.eq(switch)

    rgb_fsm.act("IDLE", NextValue(rgb_module.RedCount, 0), NextValue(rgb_module.BlueCount, 0xFF), NextValue(rgb_module.GreenCount, 0), NextValue(rgb_module.pwmCount, 0), NextState("INCREMENT"))

    rgb_fsm.act(
        "INCREMENT",
        If(rgb_module.pwmCount == 0xFF, NextState("RGB_INCREMENT")).Else(
            NextValue(rgb_module.pwmCount, rgb_module.pwmCount + 1),
            NextState("INC_DELAY"),
        ),
    )

    rgb_fsm.act(
        "INC_DELAY",
        If(
            rgb_module.delay_count == delay,
            NextValue(rgb_module.delay_count, 0),
            NextState("INCREMENT"),
        ).Else(NextValue(rgb_module.delay_count, rgb_module.delay_count + 1)),
    )

    rgb_fsm.act(
        "RGB_INCREMENT",
        If(
            rgb_module.red_inc,
            NextValue(rgb_module.RedCount, rgb_module.RedCount + 1),
            NextValue(rgb_module.BlueCount, rgb_module.BlueCount - 1)
        )
        .Elif(
            rgb_module.green_inc,
            NextValue(rgb_module.GreenCount, rgb_module.GreenCount + 1),
            NextValue(rgb_module.RedCount, rgb_module.RedCount - 1),
        )
        .Elif(
            rgb_module.blue_inc,
            NextValue(rgb_module.BlueCount, rgb_module.BlueCount + 1),
            NextValue(rgb_module.GreenCount, rgb_module.GreenCount - 1)
        )
        .Else(
            NextValue(rgb_module.RedCount, 0),
            NextValue(rgb_module.GreenCount, 0),
            NextValue(rgb_module.BlueCount, 0),
        ),
        NextState("INCREMENT"), NextValue(rgb_module.pwmCount, 0),
    )

    rgb_module.comb += leds[0].eq(rgb_module.pwmCount < rgb_module.BlueCount)
    rgb_module.comb += leds[1].eq(rgb_module.pwmCount < rgb_module.GreenCount)
    rgb_module.comb += leds[2].eq(rgb_module.pwmCount < rgb_module.RedCount)
    rgb_module.comb += leds[3].eq(rgb_module.pwmCount < rgb_module.GreenCount)
    rgb_module.comb += leds[4].eq(rgb_module.pwmCount < rgb_module.RedCount)
    rgb_module.comb += leds[5].eq(rgb_module.pwmCount < rgb_module.BlueCount)
    rgb_module.comb += rgb_module.red_inc.eq((rgb_module.GreenCount == 0) & (rgb_module.RedCount < 0xFF))
    rgb_module.comb += rgb_module.green_inc.eq((rgb_module.BlueCount == 0) & (rgb_module.GreenCount < 0xFF))
    rgb_module.comb += rgb_module.blue_inc.eq((rgb_module.RedCount == 0) & (rgb_module.BlueCount < 0xFF))

    for idx in range(8):
        rgb_module.comb += ctr_leds[idx].eq(rgb_module.pwmCount[idx])
        rgb_module.comb += ctr_leds[idx + 8].eq(rgb_module.RedCount[idx])

    nexys_platform.build(rgb_module)

    programmer = nexys_platform.create_programmer()

    programmer.load_bitstream("build/top.bit")


if __name__ == "__main__":
    main()
