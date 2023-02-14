# Info

This is a copy of the working/nonworking read and write ILA runs. The nonworking read and write were obtained by first running a write with data 0x11111111, strb 0x2 (thus making data written the 2nd byte) and then an immediate read to see if the data had changed, which it did not. The working read and write were obtained by making ILA's of reads and writes and checking the data over and over again until after a write, the data read changed to the correct value.
