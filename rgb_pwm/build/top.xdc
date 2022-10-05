################################################################################
# IO constraints
################################################################################
# user_sw:0
set_property LOC J15 [get_ports {user_sw0}]
set_property IOSTANDARD LVCMOS33 [get_ports {user_sw0}]

# rgb_led:0
set_property LOC R12 [get_ports {rgb_led0}]
set_property IOSTANDARD LVCMOS33 [get_ports {rgb_led0}]

# user_sw:1
set_property LOC L16 [get_ports {user_sw1}]
set_property IOSTANDARD LVCMOS33 [get_ports {user_sw1}]

# rgb_led:1
set_property LOC M16 [get_ports {rgb_led1}]
set_property IOSTANDARD LVCMOS33 [get_ports {rgb_led1}]

# user_sw:2
set_property LOC M13 [get_ports {user_sw2}]
set_property IOSTANDARD LVCMOS33 [get_ports {user_sw2}]

# rgb_led:2
set_property LOC N15 [get_ports {rgb_led2}]
set_property IOSTANDARD LVCMOS33 [get_ports {rgb_led2}]

# user_sw:3
set_property LOC R15 [get_ports {user_sw3}]
set_property IOSTANDARD LVCMOS33 [get_ports {user_sw3}]

# rgb_led:3
set_property LOC G14 [get_ports {rgb_led3}]
set_property IOSTANDARD LVCMOS33 [get_ports {rgb_led3}]

# user_sw:4
set_property LOC R17 [get_ports {user_sw4}]
set_property IOSTANDARD LVCMOS33 [get_ports {user_sw4}]

# rgb_led:4
set_property LOC R11 [get_ports {rgb_led4}]
set_property IOSTANDARD LVCMOS33 [get_ports {rgb_led4}]

# user_sw:5
set_property LOC T18 [get_ports {user_sw5}]
set_property IOSTANDARD LVCMOS33 [get_ports {user_sw5}]

# rgb_led:5
set_property LOC N16 [get_ports {rgb_led5}]
set_property IOSTANDARD LVCMOS33 [get_ports {rgb_led5}]

# clk100:0
set_property LOC E3 [get_ports {clk100}]
set_property IOSTANDARD LVCMOS33 [get_ports {clk100}]

################################################################################
# Design constraints
################################################################################

set_property INTERNAL_VREF 0.900 [get_iobanks 34]

################################################################################
# Clock constraints
################################################################################


create_clock -name clk100 -period 10.0 [get_ports clk100]

################################################################################
# False path constraints
################################################################################


set_false_path -quiet -through [get_nets -hierarchical -filter {mr_ff == TRUE}]

set_false_path -quiet -to [get_pins -filter {REF_PIN_NAME == PRE} -of_objects [get_cells -hierarchical -filter {ars_ff1 == TRUE || ars_ff2 == TRUE}]]

set_max_delay 2 -quiet -from [get_pins -filter {REF_PIN_NAME == C} -of_objects [get_cells -hierarchical -filter {ars_ff1 == TRUE}]] -to [get_pins -filter {REF_PIN_NAME == D} -of_objects [get_cells -hierarchical -filter {ars_ff2 == TRUE}]]