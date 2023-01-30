# Our Project

The purpose of LiteX, an open-source program by enjoy-digital, is to “provide a convenient and efficient infrastructure to create FPGA Cores/SoCs, to explore various digital design architectures and create full FPGA based systems.” LiteX supports many boards and their various capabilities. However, LiteX does not support all boards and must continue to be developed over time. 

We have proposed to add to the existing implementation of the Alveo U280 board to support all AXI interfaces of the HBM (high bandwidth memory) memory controller and test/validate its support. We will do this by adding a BIST (built-in self test) to each of the 28 AXI interfaces of the HBM controller. Each BIST will write and read data to addresses and check that the implementation of the HBM controller indeed works. The current implementation of the HBM controller reads and writes to addresses with a burst length of 1. Optionally, we can add functionality to support higher burst lengths.
Our project statement says the following: Implement the existing core, develop additional tests for the AXI interface, and extend the capabilities of LiteX for the Alveo board.

Here is an idea of what will be added:[Needs updating]

![What will be added](https://drive.google.com/uc?export=view&id=1aRLhPtZqdgbAqefOp2Rm0oeTggE13nZW)

Please note that even though this is for a `Forest Kitten 33 / VU33P` the underliying code for the Alveo U280 board has the same interface except for the fact that we can talk to the host through the JTAG Bone or through a PCIE interface.

# Background

<details><summary> Given Background Info</summary>
<p>

## Project Description:

On this team, you’ll help design FPGA circuitry using Migen/Litex for the Alveo U280 board, extend board support for the Alveo board to support all AXI interfaces, and write software for the processor operating on this board. In the process, you’ll be creating open-source intellectual property for Google to enhance current support for High-Bandwidth Memory (HBM) interfaces on Xilinx FPGAs. Experience with FPGA design, SoC technologies, and embedded systems needed for this project. 

## Background Information:

This project will develop open source intellectual property (IP) to enhance the current open source support for the HBM interfaces on Xilinx FPGAs within the Litex environment. In particular, this project will add additional AXI interfaces to the board platform, provide HBM memory testing modules for these interfaces, and create tests that demonstrate the maximum bandwidth under a variety of conditions. This project will also contribute to the documentation of the Litex open source project.

## What Do You Anticipate the Student Team Will Design & Build?

Students will design FPGA circuitry using Migen/Litex for the Alveo board, extend the board support for the Alveo U280 board, and write software for the processor operating on this board. Students will run experiments on this board with their FPGA hardware and software to determine bandwidth limits of the HBM memory. Students will also create and expand documentation for the Migen/Litex environment to facilitate contributions by other students.

## Summary of Most Important Functional Requirements for Proposed Project:

Implement the existing board support in Litex for the Alveo U280 board containing HBM memory
Extend the board support in Litex for this board to support all AXI interfaces to the HBM memory
Develop memory bandwidth generators for this board to exercise the HBM memory under a number of conditions
Provide documentation for the board and Litex environment
All work completed on this project must be made available open source using open source best practices
Special Concerns or Other Information Related to the Proposed Project
Students assigned to this project should have familiarity with FPGA design, system-on-chip (SOC) technologies, and embedded systems.

### Company Sponsoring Project:

![Google Logo](./Photos/Google_2015_logo.svg)

### Company Sponsor

<details><summary> Tim Ansell</summary>
<p>

|  |  |
| ---: | --- |
| Company: | Google|
| Email: | tansell@google.com |

</p>
</details>

### Comapny Liaison

<details><summary> Mike Wirthlin</summary>
<p>

|  |  |
| ---: | --- |
| Company: | BYU Electrical and Computer Engineering |
| Email: | wirthlin@byu.edu |

</p>
</details>

</p>
</details>