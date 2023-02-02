### Imports in the `xilinx_alveo_u280.py` 
`from migen import *`

`from migen.genlib.resetsync import AsyncResetSynchronizer`

- https://github.com/m-labs/migen/blob/master/migen/genlib/resetsync.py

`from litex.gen import LiteXModule`
 - allows for the use of Litex sintax to convert to migen

`from litex_boards.platforms import xilinx_alveo_u280`
 - uploads the alveo u280 board specs

`from litex.soc.cores.clock import *`

- https://github.com/enjoy-digital/litex/tree/master/litex/soc/cores/clock

`from litex.soc.integration.soc_core import *`

- https://github.com/enjoy-digital/litex/blob/master/litex/soc/integration/soc_core.py

`from litex.soc.integration.soc import SoCRegion`

- https://github.com/enjoy-digital/litex/blob/master/litex/soc/integration/soc.py
  - there is a class in this file that has ‘SoCRegion’


`from litex.soc.integration.builder import *`

- https://github.com/enjoy-digital/litex/blob/master/litex/soc/integration/builder.py

`from litex.soc.interconnect.axi import *`

- https://github.com/enjoy-digital/litex/tree/master/litex/soc/interconnect/axi

`from litex.soc.interconnect.csr import *`

- https://github.com/enjoy-digital/litex/blob/master/litex/soc/interconnect/csr.py

`from litex.soc.cores.ram.xilinx_usp_hbm2 import USPHBM2`

- https://github.com/enjoy-digital/litex/blob/master/litex/soc/cores/ram/xilinx_usp_hbm2.py
  - This could be a problem because when it gets created it doesn't specify that it needs to be AXI3

`from litex.soc.cores.led import LedChaser`

- https://github.com/enjoy-digital/litex/blob/master/litex/soc/cores/led.py

`from litedram.modules import MTA18ASF2G72PZ`

- https://github.com/enjoy-digital/litedram/blob/master/litedram/modules.py
  - This is for the DDR4 RDIMM

`from litedram.phy import usddrphy`

- https://github.com/enjoy-digital/litedram/blob/master/litedram/phy/usddrphy.py
  - For Xilinx ddr4 or ddr3

`from litepcie.phy.usppciephy import USPPCIEPHY`

- https://github.com/enjoy-digital/litepcie/blob/master/litepcie/phy/usppciephy.py
  - Add PCIe conectivity

`from litepcie.software import generate_litepcie_software`

- https://github.com/enjoy-digital/litepcie/tree/master/litepcie/software
  - Generate_litepcie_software is in ” __init__.py”

`from litedram.common import *`

- https://github.com/enjoy-digital/litedram/blob/master/litedram/common.py

`from litedram.frontend.axi import *`

- https://github.com/enjoy-digital/litedram/blob/master/litedram/frontend/axi.py
  - Holds methods to change native ports to AXI ports

`from litescope import LiteScopeAnalyzer`
- https://github.com/enjoy-digital/litescope/tree/master/litescope

### in main function
`from litex.build.parser.py import LiteXArgumentParser`
 - https://github.com/enjoy-digital/litex/blob/master/litex/build/parser.py
  - creates a parser to turn LiteX code into something that can be turned into a Verilog file

## How the `xilinx_alveo_u280.py` runs

### In `def main()`

#### Makes LiteXArgumentParser
- LiteX argument parser creates an object that can hold all the information that is needed to create the HDL
 - It also holds an array of arguments that are used to set defaults of wires and clocks and other things 
- Adds Alveo u280 platform
- sets the system clock frequency to 150e6
- sets default DDram channel to 0
- Enables PCIe support
- Generates PCIe Driver
- Enables HBM2 use
- Enables the Analyzer (for basic IO)
- Enables the LED Chaser
#### parses the argument 
Now we have and `args` that has all the info for calling the other 2 classes
#### checks if we are using the HBM
If we are we change the system clock to 250e6
#### Creates the `soc`
Calls `BaseSOC(...,...,...,...)`

Uses the `args` for the inputs of BaseSoc

In BaseSoc it starts instanciating the physical hardware.

The first thing it does is set some variables
 - `sys_clk_freq` sets to 150e6 (default is 150e6)
 - `ddram_channel` sets to 0 (default is 0)
 - `with_pcie` sets to true (default is false)
 - `with_led_chaser` sets to true (default is false)
 - `with_hbm` sets to true (default is false)
 - `**kwargs` array of arguments that can be passed in

Then it sets the platform to the Alveo u280 platform (prenamed wires to connect to the board)

### Creates the `_CRG`

Uses the function `ClockDomain()` to set some values
 - `ClockDomain()` creates new clocks
 - `self.cd_sys` creates system clock
 - `self.cd_hbm_ref` creates HBM reference clock
 - `self.cd_apb` creates clock for apb (what is this?) - apb is the Advance Peripheral Bus protocol, which uses its own clock

Then it moves onto setting some things for the HBM

- `self.pill = pll = USMMCM(speedgrade=-2)`
- PLL - phase-locked loop
- MMCM - mixed-mode clock manager
- PLL - used to sync clock signals or generate new ones
 - TODO What does this do?
- it registers clock in (and does some other stuff I dont know)
- it creates clock out with the system frequency
- it creates the HBM refrence clock and sets the frequency to 100e6
- it creates the APB clock and sets frequency to 100e6
- adds platform constraints for the System clock and the APB clock

Finishes creating the CRG

### Going back to `BaseSoC`

Initalizes the SoCCore
 - https://github.com/enjoy-digital/litex/blob/master/litex/soc/integration/soc_core.py
 - given the arguments `platform, sys_clk_freq, ident="LiteX SoC on Alveo U280 (ES1)", **kwargs)`
 - Initalizes
  - Bus paramaters ("wishbone")
  - CPU parameters ("Vexriscv")
  - CFU parameters
  - ROM parameters
  - SRAM parameters
  - MAIN_RAM parameters
  - CSR parametsers
  - Interrupt parameters
  - Identifier parameters
  - UART parameters
  - Timer parameters
  - Controller parameters
  - uses `**Kwargs` for setting other parameters

Creates the CPU

Creates the HBM  core(line 111)

Gets the HBM .xci file to add

adds AXI ports to the HBM
- Creates HBM axi port
- Creates Axi Lite port
- Convirts the HBM axi port and converts it to axi lite 
- adds the convirted axi port as a submodule
- adds a slave to the bus that connects to the convierted axi port

Adds PCIe port the the project (pcie_x4)

Adds LED chaser

### Going back to `main()`

Creates new buildier using the SOC

Creates the driver for the PCIe connection

