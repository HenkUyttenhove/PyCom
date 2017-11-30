##########################################
#                                        #
#   Build for fun NTC-103 procedure      #
#                                        #
#   Author: Henk Uyttenhove              #
#   Date: 30 Nov 2017                    #
#   License: MIT License                 #
#                                        #
##########################################

# Load the required libraries + configure the required pin
from machine import ADC    # Import the ADC convertor library
import time
adc = ADC()

# Set the other variables
#    We use the 3.3V from pin 3 right connected to a resistance 10k ohm, the NTC-103 10k and ground pin 2 right
#    The input is P13 connected between resistance and NTC-103
Resistance = 10000   # The value of the resistance
Voltage = 3270       # Measured mV of the pin 3 to guarantee calibration


# Calibrate the Pycom
#    The Pycom is not calibrated from factory so this needs to be done to be correct
#    This is done by activating the reference power to a Pin (example P22)
#         adc.vref_to_pin('P22')
#    Measure the power with external Volt meter and put mV into Pycom
adc.vref(1150)

# Input for the ADC controller
#     The Pycom can only support up to 1.1V input, to support more, the ATTN_11DB is to be activated
SensorInput = adc.channel(pin='P13',attn=ADC.ATTN_11DB)  # set P13 to support 3,3V

def ConvertTemp(resistance):   # function translating resistance into temperature
    ConvertTable=[[67740,'-20'],[64540,'-19'],[61520,'-18'],[58660,'-17'],[53390,'-16'],[53390,'-15'],[50960,'-14'],[48650,'-13'],[46480,'-12'],[44410,'-11'],[42250,'-10'],[40560,'-9'],[38760,'-8'],[37050,'-7'],[35430,'-6'],[33890,'-5'],[32430,'-4'],[31040,'-3'],[29720,'-2'],[28470,'-1'],[27280,'0'],[26130,'1'],[25030,'2'],[23990,'3'],[22990,'4'],[22050,'5'],[21150,'6'],[20290,'7'],[19400,'8'],[18700,'9'],[17960,'10'],[17240,'11'],[16550,'12'],[15900,'13'],[15280,'14'],[14680,'15'],[14120,'16'],[13570,'17'],[13060,'18'],[12560,'19'],[12090,'20'],[11630,'21'],[11200,'22'],[10780,'23'],[10380,'24'],[10000,'25'],[9630,'26'],[9280,'27'],[8940,'28'],[8620,'29'],[8310,'30'],[8010,'31'],[7720,'32'],[7450,'33'],[7190,'34'],[6940,'35'],[6690,'36'],[6460,'37'],[6240,'38'],[6030,'39'],[5820,'40']]

    teller = len(ConvertTable)
    for x in range(0,teller):     # Find the required value in the above list
        Actual = ConvertTable[x]
        if Actual[0] < resistance:
            break
    return(Actual[1])

while True:
    MeasuredList = []
    for y in range(9):           #  We measure every 3 sec x 10 = 30 sec
        SensorVoltage = SensorInput.voltage()
        MeasuredList.append(SensorVoltage)
        time.sleep(3)

    AverageList = sum(MeasuredList)/len(MeasuredList)       # Get the average over 30 sec
    SensorResistance = Resistance/((Voltage/AverageList)-1) # Formula to convert measure voltage to resistance
    print("Volt:",SensorVoltage," Weerstand:", SensorResistance, " Temp:",ConvertTemp(SensorResistance)," graden")
