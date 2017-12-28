#!/usr/bin/python
#


# Import required libraries
import time
import RPi.GPIO as GPIO
from Heater import Heater
from relaypipy import RelayPiPy


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

  relay4 = RelayPiPy()
  pinList = [ 6, 13, 19, 26 ]
  relay4.init( pinList )

  powerRelay = 3

  heater = Heater(powerRelay)

  print "on"
  heater.on()

  time.sleep(2)

  print "off"
  heater.off()

  time.sleep(2)





  heater.setMinAirTemp(44)
  heater.setMinWaterTemp(55)

  heater.setCurrentAirTemp(30)
  heater.setCurrentWaterTemp(60)

  heater.run()
  time.sleep(2)

  heater.setCurrentAirTemp(45)
  heater.setCurrentWaterTemp(56)

  heater.run()
  time.sleep(2)



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
