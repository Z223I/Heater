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




    
    self.powerRelay = _powerRelay



#TODO tell relay to reserve one relay



# End method __init__




########################################################
# method off
########################################################

  def off(self):

    # Power off
    Heater.relay.off(self.powerRelay)


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


########################################################
# End method on
########################################################



########################################################
#
# End class Heater
#
########################################################
