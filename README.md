# The FPGA High Bandwith Memory Interfacing and Monitoring Project

![DRGBL Logo](/docs/Photos/Drgbl_Logo.jpeg)

Hi! We are BYU Capstone Team 17 (DRGBL)!

We are working on the FPGA High-Bandwidth Memory Interfacing and Monitoring Project!

## Documentation / Background Info
Our Project **Documentation** and **Background** information can be found on our [Wiki] (https://github.com/Capstone2022Team17/drgbl/wiki)

## Contact us
If you have any questions, please reach out at capstone2022.team17@gmail.com.

## Overview of Project Implementation

![DRGBL Project](/docs/Photos/System_Design_Diagram.drawio%20(1).png)

## Project Requirements
The system requirements can be summarized as follows:
* A memory bandwidth generator module that can be applied to each of the 32 available
AXI interfaces to the HBM
* Each memory bandwidth generator module has these functionalities
  * Continuous reads to HBM of a specified number of bytes a specified number of
times.
  * Continuous writes to HBM of a specified number of bytes a specified number of
times
* A hardware counter records the number of transactions and the number of clock cycles
to determine the transaction speed
* A program that communicates with the board over UART to activate the BISTs

As part of this, we have forked 3 different repositories for this project.
## Forked Repositories
[Forked LiteX](https://github.com/Capstone2022Team17/litex)

* This is where most of the SOC/AXI implementation is located and also where we have implemented new BIOS code.

[LiteHBM](https://github.com/Capstone2022Team17/litehbm)

* This contains all of our project files as a way to put everything together as a seprate module. We ended up giving up on getting that to work becuse it would make it more difficult for the user to use our code.

[Forked litex-boards](https://github.com/Capstone2022Team17/litex-boards)

* This is where most of our code is. [Here](https://github.com/Capstone2022Team17/litex-boards/blob/master/litex_boards/targets/xilinx_alveo_u280.py) is the exact file that is being updated for this project. It's called the `xilinx_alveo_u280.py`. We have updated this file to have the cpu dependent on the DRAM and now we have full access to the 32 HBM ports.

## What we are working on

We now have working Bandwidth generators and are working on BIOS implementations of their controll. We are also working on data colection and data analysis.

To see a more detailed and individualized tasks check out our project [Here](https://github.com/users/Capstone2022Team17/projects/1).


## What is in this Repository
* rgb_pwm has a basic Migen script that gradually changes the RGB leds to different colors.
* rgb_pwm_withSoC is a basic SoC used to control the rgb leds.
