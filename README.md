## OH_Temperature_Demo ##

Author: Patrick Daniel, Moss Landing Marine Labs

Date: 2017-04-21

### Introduction ###

This demo is used to illustrate the application and afforadability of digital electronics in science and research. The Raspberry Pi being a key example of a cheap (~$35) computers that runs a full Linux distribution is internet enabled and has been adapted for all kinds of 'maker' projects. 

In this demo, two 1-wire digital temperature sensors are placed cups of water with different temperatures and the corresponding temperature values are plotted in real time to a plot on computer.

### Hardware setup ###

1-wire probes use the 3.3V power line (RP3 = pin 1) for power (red line), GND (RP3 pin 9) to the black line, and the data line to GPIO4 (RP3 = pin 7). A 4.7K ohm resistor is placed between the dataline and the power line as a pull up resistor.

### Software setup ###

The main program tmp_probe_OH17.py runs creates a Tmp_Probe object of each attached sensor, finding the serial numbers and running some of the setup scripts required for the 1-wire protocol. A simple plot is made using the QT library, as the time this was made there were some issues running more standard plotting libraries like matplotlib on a raspberry pi. 