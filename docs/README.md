# Documentation
## FDB273BD-66BB-4464-9FAC-8E479D60BDC9.jpeg
- JPEG of DRGBL logo
## logo.svg
- SVG of the DRGBL logo (without background)
## pg276-axi-hbm-en-us-1.0.pdf
### Overview
- This is the Documentation for the HBM2 that is on the Alveo U280 board
### Important info from document
#### Under HBM Topology
> The Xilinx HBM solutions are available in either 4 GB or 8 GB per stack options, with nearly all configurations containing two stacks per FPGA. This means there is a total of 8 GB or 16 GB of available memory for these dual stack devices.

>The total data-bit width of an HBM stack is 1024 bits divided across eight channels of 128 bits each. Each channel is serviced by a single memory controller which accesses the HBM in pseudo channel mode, meaning two semi-independent 64-bit data channels with a shared command/address/control (CAC) bus. A 4 GB per stack device has 4 Gb per channel, and each channel has two 2 Gb or 256 MB pseudo channels. An 8 GB per stack device has 8 Gb per channel, and each channel has two 4 Gb or 512 MB pseudo channels.

#### HBM Address Map and Protocol Considerations
| HBM Arrangement | 4H Device (4 GB per Stack)|
| --- | :---: |
|Density per Channel| 4 Gb|
|Density per Pseudo Channel| 2Gb|
|Row Address| RA[13:0] |
|Column Address| CA[5:1] |
|Bank Group Address| BA[3:0] |
|Bank Arrangement| 16 Banks <br/> 4 Bank Groups with 4 Banks |
|Total User Address Bits| 23 |

#### AXI Addressing for 4H
| HBM Arrangement | 4H Device (4 GB per Stack)|
| --- | :---: |
|Total Address Bits| 33 total as 32:0|
|Stack Select: 0 = Left 1 = Right| 32|
|Destination AXI Port: 0 – 15| 31:28 |
|HBM Address Bits| 27:5 |
|Unused Address Bits| 4:0 |
