#!/usr/bin/python
#


# Import required libraries
import time
import RPi.GPIO as GPIO
from relaypipy import RelayPiPy



########################################################
#
# Class Heater
#
# This class uses a relay to turn on a water heater
# indirectly.  This class directly powers a water pump
# which activates the portable water heater.
#
# It takes a single pin to control the water pump.
#
########################################################

class Heater():

  # The calling script must have already established
  # a RelayPiPy object and called its init method to
  # establish the number of relays.
  relay = RelayPiPy()

########################################################
# method __init__
########################################################

  def __init__(self, _powerRelay):
    print "__init__"
    self.isOn = False



    
    self.powerRelay = _powerRelay



#TODO tell relay to reserve one relay



# End method __init__




########################################################
# method off
########################################################

  def off(self):

    # Power off
    Heater.relay.off(self.powerRelay)
    self.isOn = False

########################################################
# End method off
########################################################



########################################################
# method on
########################################################

  def on(self):

    # Power on 
    print "Relay = ", self.powerRelay
    print "pinList = ", Heater.relay.pinList
    Heater.relay.on(self.powerRelay)
    self.isOn = True

########################################################
# End method on
########################################################








########################################################
# method run
########################################################

  def run(self):

    needHeater = False

    diffWater = 1
    if self.waterTemp < self.minWaterTemp - diffWater: 
      needHeater = True
    diffAir = 1
    if self.airTemp < self.minAirTemp - diffAir: 
      needHeater = True

    if needHeater:
      self.on()

    if self.waterTemp > self.minWaterTemp and self.airTemp > self.minAirTemp: 
      self.off()



########################################################
# End method run
########################################################









########################################################
# method setCurrentAirTemp
########################################################

  def setCurrentAirTemp(self, _airTemp):
    self.airTemp = _airTemp


########################################################
# End method setCurrentAirTemp
########################################################




########################################################
# method setCurrentWaterTemp
########################################################

  def setCurrentWaterTemp(self, _waterTemp):
    self.waterTemp = _waterTemp


########################################################
# End method setCurrentWaterTemp
########################################################





########################################################
# method setMinAirTemp
########################################################

  def setMinAirTemp(self, _minAirTemp):
    self.minAirTemp = _minAirTemp


########################################################
# End method setMinAirTemp
########################################################


########################################################
# method setMinWaterTemp
########################################################

  def setMinWaterTemp(self, _minWaterTemp):
    self.minWaterTemp = _minWaterTemp


########################################################
# End method setMinWaterTemp
########################################################



########################################################
#
# End class Heater
#
########################################################
