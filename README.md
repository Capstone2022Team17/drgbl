# DRGBL
![DRGBL Logo](/docs/logo.svg)
## The FPGA High Bandwith Memory Interfacing and Monitoring Project

The purpose of Litex, an open-source program by enjoy-digital, is to “provide a convenient and efficient infrastructure to create FPGA Cores/SoCs, to explore various digital design architectures and create full FPGA based systems.” Litex supports many boards and their various capabilities. However, Litex does not support all boards and must continue to be developed over time. 

We have proposed to add to the existing implementation of the Alveo U280 board to support all AXI interfaces of the HBM (high bandwidth memory) memory controller and test/validate its support. We will do this by adding a BIST (built-in self test) to each of the 28 AXI interfaces of the HBM controller. Each BIST will write and read data to addresses and check that the implementation of the HBM controller indeed works. The current implementation of the HBM controller reads and writes to addresses with a burst length of 1. Optionally, we can add functionality to support higher burst lengths.
Our project statement says the following: Implement the existing core, develop additional tests for the AXI interface, and extend the capabilities of Litex for the Alveo board.

## Project Requierments
* A BIST module that can be applied to each of the 28 available AXI interfaces to the HBM
* A Python script that communicates with the board over JTAG to activate the BISTs
* Replace the AXI-Lite Interfaces with AXI-Full Interfaces

## What we palan to do next
* We are currently working on a custom fork of the litex-hub/litex-boards and changing the alveo u280 project to implement the new BISTs and change the AXI ports from AXI Lite to AXI full

https://github.com/Capstone2022Team17/litex-boards

## What is in this Repository
* rgb_pwm has a basic migen script that gradually changes the rgb leds to different colors.
* rgb_pwm_withSoC is a basic SoC used to control the rgb leds.
