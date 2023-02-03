# Problem and Solutions

### Simulation problem

One problem we had was trying to figure out how to simulate our designs with the alveo board. We had a single serial connection, and Litex did not clearly explain how to run the bios while using Litex's simulation tool. Eventually, in the logs of the irc chat, we found the following written by florent:

12:40 <florent> so build with --uart-name=crossover+uartbone
12:40 <florent> then open litex_server with --uart --uart-port=/dev/ttyUSBX
12:41 <florent> then litex_term crossover

After running these commands (litex_term command has to be run in a different terminal while litex_server is running), we can open a new terminal, go to the same directory, and all the litescope_cli commands are available for use (while litex_server is running).

https://github.com/enjoy-digital/litex/wiki/Use-LiteScope-To-Debug-A-SoC
  
In this way, we were able to run a simulation of all our bus, hbm, fsm, and litedram signals.
