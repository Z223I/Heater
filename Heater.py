#!/usr/bin/python
#


# Import required libraries
import time
import RPi.GPIO as GPIO




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

  def __init__(self, _powerLockPinA, _powerLockPinB):
    print "__init__"

    # Define GPIO signals to use
    # Physical pins 11,15,16,18
    # GPIO17, GPIO18, GPIO22, GPIO23
    
    self.powerLockPinA = _powerLockPinA
    self.powerLockPinB = _powerLockPinB

    self.powerDelay = .2
# End Function __init__


########################################################
# Function init
########################################################

  def init(self):
    print "init"
  
    # Use BCM GPIO references
    # instead of physical pin numbers
    GPIO.setmode(GPIO.BCM)

    # Set pins to output and initialize them to false.
    GPIO.setup(self.powerLockPinA, GPIO.OUT)
    GPIO.output(self.powerLockPinA, False)
    GPIO.setup(self.powerLockPinB, GPIO.OUT)
    GPIO.output(self.powerLockPinB, False)

# End Function init



########################################################
# Function powerOff
########################################################

  def powerOff(self):

    # Power off both pins
    GPIO.output(self.powerLockPinA, False)
    GPIO.output(self.powerLockPinB, False)


########################################################
# End Function powerOff
########################################################



########################################################
#
# End class Heater
#
########################################################
