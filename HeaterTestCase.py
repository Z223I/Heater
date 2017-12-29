import unittest
from Heater import Heater
from relaypipy import RelayPiPy

class HeaterTestCase(unittest.TestCase):
    relay4 = None 

    def setUp(self):
        global relay4

        relay4 = RelayPiPy()
        pinList = [ 6, 13, 19, 26 ]
        relay4.init( pinList )

        self.powerRelay = 3

        self.heater = Heater(self.powerRelay)

    def tearDown(self):
        self.heater = None

    def test_powerRelay(self):
        self.assertEqual(self.heater.powerRelay, self.powerRelay,
                'Wrong relay port.')

    def test_isOn(self):
        self.assertFalse(self.heater.isOn, 'Heater should be off.')

    def test_on(self):
        self.assertTrue(self.heater.on(), 'Heater should be on.')

    def test_of(self):
        self.assertFalse(self.heater.off(), 'Heater should be off.')



if __name__ == '__main__':
    unittest.main()
