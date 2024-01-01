import unittest
from source.day_1 import *

class TestDay1(unittest.TestCase):

    def test_positive_mass(self):
        self.assertEqual(fuel(12), 2)
        self.assertEqual(fuel(14), 2)
        self.assertEqual(fuel(1969), 654)
        self.assertEqual(fuel(100756), 33583)

    def test_fuel_summed(self):
        input = array_of_int("../resources/day_1_data")
        self.assertEqual(3382284, calculate_total_fuel(input))


    def test_fuel_for_fuel_summed(self):
        input = array_of_int("../resources/day_1_data")
        self.assertEqual(5070541, calculate_total_fuel_with_extra_fuel(input))


    def test_fuel_for_fuel(self):
        self.assertEqual(50346, fuel_for_fuel(100756))
        self.assertEqual(966, fuel_for_fuel(1969))
        self.assertEqual(2, fuel_for_fuel(14))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay1('test_process_code'))
    return suite


if __name__ == '__main__':
    unittest.main()