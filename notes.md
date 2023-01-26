## Imports in the `xilinx_alveo_u280.py` 
from migen import *
from migen.genlib.resetsync import AsyncResetSynchronizer
-https://github.com/m-labs/migen/blob/master/migen/genlib/resetsync.py
from litex.gen import LiteXModule
from litex_boards.platforms import xilinx_alveo_u280
from litex.soc.cores.clock import *
-https://github.com/enjoy-digital/litex/tree/master/litex/soc/cores/clock
from litex.soc.integration.soc_core import *
-https://github.com/enjoy-digital/litex/blob/master/litex/soc/integration/soc_core.py
from litex.soc.integration.soc import SoCRegion
-https://github.com/enjoy-digital/litex/blob/master/litex/soc/integration/soc.py
- there is a class in this file that has ‘SoCRegion’
from litex.soc.integration.builder import *
-https://github.com/enjoy-digital/litex/blob/master/litex/soc/integration/builder.py
from litex.soc.interconnect.axi import *
-https://github.com/enjoy-digital/litex/tree/master/litex/soc/interconnect/axi
from litex.soc.interconnect.csr import *
-https://github.com/enjoy-digital/litex/blob/master/litex/soc/interconnect/csr.py
from litex.soc.cores.ram.xilinx_usp_hbm2 import USPHBM2
-https://github.com/enjoy-digital/litex/blob/master/litex/soc/cores/ram/xilinx_usp_hbm2.py
-This could be a problem because when it gets created it doesn't specify that it needs to be AXI3
from litex.soc.cores.led import LedChaser
-https://github.com/enjoy-digital/litex/blob/master/litex/soc/cores/led.py
from litedram.modules import MTA18ASF2G72PZ
-https://github.com/enjoy-digital/litedram/blob/master/litedram/modules.py
-This is for the DDR4 RDIMM
from litedram.phy import usddrphy
-https://github.com/enjoy-digital/litedram/blob/master/litedram/phy/usddrphy.py
-For Xilinx ddr4 or ddr3
from litepcie.phy.usppciephy import USPPCIEPHY
-https://github.com/enjoy-digital/litepcie/blob/master/litepcie/phy/usppciephy.py
-Add PCIe conectivity
from litepcie.software import generate_litepcie_software
-https://github.com/enjoy-digital/litepcie/tree/master/litepcie/software
-Generate_litepcie_software is in ” __init__.py”
from litedram.common import *
-https://github.com/enjoy-digital/litedram/blob/master/litedram/common.py
from litedram.frontend.axi import *
-https://github.com/enjoy-digital/litedram/blob/master/litedram/frontend/axi.py
-Holds methods to change native ports to AXI ports
from litescope import LiteScopeAnalyzer
