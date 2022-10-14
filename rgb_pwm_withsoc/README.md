## Beginnings of PWM SoC program

Alrighty guys, this is how you run this super basic SoC.

1. Navigate into this directory, source vivado and run 'python3 rgb_soc.py'. A build directory will be created. Make sure Openocd is installed, this program will load the bitstream onto the board.
3. Navigate into the 'program' directory, run 'make all'
4. Run 'litex_term /dev/ttyUSBX --kernel=rgb.bin' where 'X' is replaced with the correct dev port number. The bios will run (the automatic app that runs when a litex design is loaded to the board.) You may have to press enter a couple times to get a litex prompt. To change the app, simply type 'reboot' and press enter, or press the button 'CPU reset'.

Note: 
* You can look at all the functions controlling the csr registers (such as the rgb functions being used in this app) in build/software/include/generated/csr.h. Also, the build function currently generates a list of all the csr registers you are able to manipulate in the csr.csv. 
