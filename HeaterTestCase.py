import unittest
from Heater import Heater


class HeaterTestCase(unittest.TestCase):

    powerRelay = 3

    def setUp(self):
        self.heater = Heater(self.powerRelay)

    def tearDown(self):
        self.heater = None

    def test_powerRelay(self):
        self.assertEqual(self.heater.powerRelay, self.powerRelay,
                'Wrong relay port.')

    def test_isOn(self):
        self.assertFalse(self.heater.isOn, 'Heater is not off')

if __name__ == '__main__':
    unittest.main()
