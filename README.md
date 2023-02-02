# The FPGA High Bandwith Memory Interfacing and Monitoring Project

![DRGBL Logo](/docs/Photos/Drgbl_Logo.jpeg)

Hi! We are BYU Capstone Team 17 (DRGBL)!

We are working on the FPGA High-Bandwidth Memory Interfacing and Monitoring Project!

## Documentation / Background Info
Our Project **Documentation** and **Background** information can be found [Here!](/docs)

## Contact us
If you have any questions, please reach out at capstone2022.team17@gmail.com.

## Project Requirements
* Create a BIST module that can be applied to each of the 28 available AXI interfaces to the HBM
* Create a Python script that communicates with the board over JTAG to activate the BISTs
* Replace the AXI-Lite Interfaces with AXI-Full Interfaces

As part of this, we have forked 3 different repositories for this project.
## Forked Repositories
[Forked LiteX](https://github.com/Capstone2022Team17/litex)

* This is where most of the SOC/AXI implementation is located.

[LiteHBM](https://github.com/Capstone2022Team17/litehbm)

* Forked from the LiteDram to see if we can build a BIST from the liteDram BIST.

[Forked litex-boards](https://github.com/Capstone2022Team17/litex-boards)

* This is where most of our code is. [Here](https://github.com/Capstone2022Team17/litex-boards/blob/master/litex_boards/targets/xilinx_alveo_u280.py) is the exact file that is being updated for this project. It's called the `xilinx_alveo_u280.py`.

## What we are working on

We are working on geting the axi interface to work with the HBM and creating a simulation of the LiteX project in LiteX. In order to do that we are working on diffrent aspects in parallel. 

To see a more detailed and individualized tasks check out our project [Here](https://github.com/users/Capstone2022Team17/projects/1).


## What is in this Repository
* rgb_pwm has a basic Migen script that gradually changes the RGB leds to different colors.
* rgb_pwm_withSoC is a basic SoC used to control the rgb leds.
