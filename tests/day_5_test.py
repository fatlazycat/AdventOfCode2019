import unittest
from source.day_5 import *


class TestDay5(unittest.TestCase):
    def test_part1(self):
        s = parse_file('../resources/day_5_data')[0]
        numbers = process_data(s)
        self.assertEqual(12440243, process_code(numbers, 1))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay5('test_day_5'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
