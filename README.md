# The FPGA High Bandwith Memory Interfacing and Monitoring Project

![DRGBL Logo](/docs/Photos/Drgbl_Logo.jpeg)

Hi! We are BYU Capstone Team 17 (DRGBL)!

We are working on the FPGA High Badwitdth Memory Interfacing and Monitoring Project!

If you have any questions please reach out at capstone2022.team17@gmail.com.

Feel free to look at our background and project info [Here!](/docs/background.md)

## Project Requirements
* Create a BIST module that can be applied to each of the 28 available AXI interfaces to the HBM
* Create a Python script that communicates with the board over JTAG to activate the BISTs
* Replace the AXI-Lite Interfaces with AXI-Full Interfaces

As part of this we have forked 3 diffrent repositories for this project.
## Forked Repositories
[Forked LiteX](https://github.com/Capstone2022Team17/litex)

* This is where most of the SOC/AXI stuff is located.

[LiteHBM](https://github.com/Capstone2022Team17/litehbm)

* Forked from the LiteDram to see if we can buid a BIST from the liteDram BIST.

[Forked litex-boards](https://github.com/Capstone2022Team17/litex-boards)

* This is where most of our code is. [Here](https://github.com/Capstone2022Team17/litex-boards/blob/master/litex_boards/targets/xilinx_alveo_u280.py) is the exact file that is being updated for this project. its called the `xilinx_alveo_u280.py`.

## What we are working on

### Zepram
* Focus: Migen
* Task: Simplified HBM writer in Migen (ignoring system/verilog)

### Pablo/Grant
* Focus: Verilog AXI + HBM Simulation
* Grant Task: Simulate HBM (not liteX) 
  * How does axi work with the HBM?
* Pablo Task: State machine memory reader/writer
  * Create basic read/write state machine in Verilog that could be created in LiteX.

### Hayden
* Fucus: Litex
* Task: Build ability to simulate Litex AXI

### Tyler
* Focus: Litex system integration + Architecture
* Task: ILA to probe design
#### Tasks
- [ ] Add ILA to LiteX project.


## What is in this Repository
* rgb_pwm has a basic migen script that gradually changes the rgb leds to different colors.
* rgb_pwm_withSoC is a basic SoC used to control the rgb leds.
