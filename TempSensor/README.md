# Temperature sensor with Pycom

The Pycom is a small IOT device with MicroPython.  It can be bought with the default expansion board, with the Pysense board or the Pytrack board.  
This project is based upon the default expansion board connected to a NTC-103 10k ohm thermal sensor.  

## Getting Started

This project only requires:
- Pycom device
- NTC-103 thermal sensor
- 10 k Ohm resistor
- Breadboard or can be soldered
- Volt meter for calibration (during initial set-up)

### Prerequisites

The coding has been done in Atom and uploaded via the default FTP client as part of the Pycom device

### Installing

Please refer to the schematics for the physical topology

[Schematics](https://github.com/HenkUyttenhove/PyCom/blob/master/TempSensor/TempSensorPycom.png)

### How does it work?
The Pycom has different ADC ports. These Analog-Digital Convertor ports can be used to read the incoming voltage.

> Special notice: As a default, the Pycom ADC ports are only able to support up to 1.1V.  See the code how to support an input up to 3.3V

> Also notice that the Pycom is not calibrated from the factory so this should be done via the procedure mentioned in the code.  

The Pycom will take a sample every 3 seconds.  After 10 samples, the average is taken and using a formula, the measured voltage is converted to resistance.  
This resistance value is then converted into Celsius using a translation table (hardcoded).  The Pycom will show the outcome via the telnet or tty console.  Integration into a IOT environment is not scope of this project.

## Authors

* **Henk Uyttenhove**   Github:[HenkUyttenhove](https://github.com/HenkUyttenhove)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
