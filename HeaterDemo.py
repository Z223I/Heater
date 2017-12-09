#!/usr/bin/python
#


# Import required libraries
import time
import RPi.GPIO as GPIO
from Heater import Heater



########################################################
# Function shutdown
########################################################


def shutdown():
  GPIO.cleanup()
  print
  print "Bye!"  

# End Function shutdown



########################################################
#
# Main
#
########################################################

try:
  powerLockPinA = 2
  powerLockPinB = 3

  powerLock = Heater(powerLockPinA, powerLockPinB)

  powerLock.init()
  powerLock.cycle()

# End try

except KeyboardInterrupt:
  # This statement is meaningless other than it allows the program to
  # drop down to the next line.
  print "Keyboard Interrupt"

# End except

shutdown()

########################################################
#
# End Main
#
########################################################
