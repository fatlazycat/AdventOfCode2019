import unittest
from source.day_1 import *

class TestFuel(unittest.TestCase):

    def test_positive_mass(self):
        self.assertEqual(fuel(12), 2)
        self.assertEqual(fuel(14), 2)
        self.assertEqual(fuel(1969), 654)
        self.assertEqual(fuel(100756), 33583)

    def test_fuel_summed(self):
        self.assertEqual(3382284, calculate_total_fuel("../resources/day_1_data"))

if __name__ == '__main__':
    unittest.main()