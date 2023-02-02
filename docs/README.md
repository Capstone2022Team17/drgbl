# pg276-axi-hbm-en-us-1.0.pdf

## Overview
- This is the Documentation for the HBM2 that is on the Alveo U280 board

## Important info from document

<details><summary> Click to view important info from document</summary>
<p>

### Core Overview
> The AXI High Bandwidth Memory Controller provides access to one or both the 1024-bit wide HBM stacks depending on the selected device; 64 Gb for 4H devices or 128 Gb for 8H devices. Each stack is split into eight independent memory channels, each of which is further divided into two 64-bit pseudo channels. Pseudo channel memory access is limited to its own section of the memory (1/16 of the stack capacity). Furthermore, each memory channel can operate at an independent clock rate that is an integer divide of a global reference clock.

>The AXI HBM Controller has simplified the interface between HBM and CLB-based user logic in several ways. The AXI3 protocol is selected to provide a proven standardized interface. The 16 AXI ports provided match the total throughput of the HBM. Each port operates at a 4:1 ratio to lower the clock rate required in the user logic. This ratio requires a port width of 256-bits (4 × 64). Each AXI3 channel has 6-bit AXI ID port which helps in reordering transactions to achieve the required bandwidth. On the selected AXI3 channel, if the transactions are triggered using a different ID tag, then the transactions are reordered as per the AXI3 protocol. Conversely, if the selected AXI3 channel transactions are triggered using same ID tag, then the transactions are executed sequentially in the order they are triggered.

>The ports are distributed across the general interconnect to reduce congestion and each port is based on an independent clock domain. This flexibility, along with each AXI port attached to its own registered column interface, reduces congestion and eases timing closure.

>The 16 × 16 AXI crossbar switch is included in this core which allows each memory port to access the full HBM space by addressing all 16 pseudo channels. In the case of a two-stack system, this is extended to a 32 × 32 crossbar to allow direct access across both HBM stacks as shown in the following 4H device figure.

### Under HBM Topology

> The Xilinx HBM solutions are available in either 4 GB or 8 GB per stack options, with nearly all configurations containing two stacks per FPGA. This means there is a total of 8 GB or 16 GB of available memory for these dual stack devices.

>The total data-bit width of an HBM stack is 1024 bits divided across eight channels of 128 bits each. Each channel is serviced by a single memory controller which accesses the HBM in pseudo channel mode, meaning two semi-independent 64-bit data channels with a shared command/address/control (CAC) bus. A 4 GB per stack device has 4 Gb per channel, and each channel has two 2 Gb or 256 MB pseudo channels. An 8 GB per stack device has 8 Gb per channel, and each channel has two 4 Gb or 512 MB pseudo channels.

### HBM Address Map and Protocol Considerations
| HBM Arrangement | 4H Device (4 GB per Stack)|
| --- | :---: |
|Density per Channel| 4 Gb|
|Density per Pseudo Channel| 2Gb|
|Row Address| RA[13:0] |
|Column Address| CA[5:1] |
|Bank Group Address| BA[3:0] |
|Bank Arrangement| 16 Banks <br/> 4 Bank Groups with 4 Banks |
|Total User Address Bits| 23 |

### AXI Addressing for 4H
| HBM Arrangement | 4H Device (4 GB per Stack)|
| --- | :---: |
|Total Address Bits| 33 total as 32:0|
|Stack Select: 0 = Left 1 = Right| 32|
|Destination AXI Port: 0 – 15| 31:28 |
|HBM Address Bits| 27:5 |
|Unused Address Bits| 4:0 |

</p>
</details>

# ProjectFile.md

[This](ProjectFile.md) file that explaines the `xilinx_alveo_u280.py` project file.

This project file holds links to the sources of each import and generaly what is being used by each import.

Then we go over how the file runes and adds all the hardware.

# RelevantLinks-Notes.md

[This](RelevantLinks-Notes.md) file is a one stop shop for all the Information you need to get started on the project.

TODO: Needs to still be filled out.

# ProblemsAndSolutions.md

[This](ProblemsAndSolutions.md) file holds the problems we ran into and the solutions we found. 

TODO: This is still needs to be populated with information. 