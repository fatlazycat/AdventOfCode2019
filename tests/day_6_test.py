import unittest
from source.day_6 import *


class TestDay6(unittest.TestCase):
    def test_part1(self):
        s = parse_file('../resources/day_6_data')
        orbits = parse_orbits(s)
        self.assertEqual(227612, get_orbit_counts(orbits))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay6('test_day_6'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
