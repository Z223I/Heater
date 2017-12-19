#!/usr/bin/python
#


# Import required libraries
import time
import RPi.GPIO as GPIO
from relaypipy.relaypipy import RelayPiPy



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


########################################################
# Function __init__
########################################################

  def __init__(self, _powerPin):
    print "__init__"
    
    self.powerPin = _powerPin
# End Function __init__


########################################################
# Function init
########################################################

  def init(self):
    print "init"
  
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Set pin to output and initialize it to false.
    GPIO.setup(self.powerPin, GPIO.OUT)
    GPIO.output(self.powerPin, False)

# End Function init



########################################################
# Function off
########################################################

  def off(self):

    # Power off pin
    GPIO.output(self.powerPin, False)


########################################################
# End Function off
########################################################



########################################################
# Function on
########################################################

  def on(self):

    # Power on pin
    GPIO.output(self.powerPin, True)


########################################################
# End Function on
########################################################



########################################################
#
# End class Heater
#
########################################################
