# About

Each of these .vcd files contain signals for 512 clock cycles while running a read or write command and can be viewed in gtkwave. The signals for the alveo board are named after the commands run during a read or write to the hbm memory. For example, ```mem_write_0x40000000_0x12345678``` is an ILA run looking at signals for the axi interface and cpu busses while running the command ```mem_write``` with address 0x40000000 and data 0x12345678. The trigger was set for the dbus\_dat\_w signal to turn to 0x12345678. ```mem_read_0x40000000_soc_cpu_dbus_adr_0x10000000``` is an ILA run with the same signals while running ```mem_read``` with address 0x40000000 with the trigger set for the signal soc_cpu_dbus_adr to turn to 0x10000000, the address that appears when reading or writing from address 0x40000000, and 0x10400000 with address 0x41000000. The others are run with the same ```mem_read``` command while waiting for the ```ar_valid``` signal to go high.

## Signals
All of these files have the following signals:

* A scope clock, the same as the system clock signal.
* A scope trigger signal. (I believe this is related to whatever variable triggers the run to start.)
* A set of cpu signals for the dbus and ibus. These are litex wishbone interfaces.
* A set of signals for the wishbone slave port eventually connecting to the AXI interface of the hbm module. These all begin with ```soc_interface0```. In this design, the wishbone interface for the cpu dbus and ibus have the same datawidth and address width of the wishbone interface of this slave.
* The set of AXI interface signals connected to this wishbone. These all begin with ```soc_usphbm2```.

