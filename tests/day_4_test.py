import unittest
from source.day_4 import *

# lower_val = 382345
# lower_val_adjusted = "388888"
# upper_val = 843167
# upper_val_adjusted = "799999"


class TestDay4(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(460, valid_passwords(3, 8, 7, has_adjacent_same))

    def test_part2(self):
        self.assertEqual(290, valid_passwords(3, 8, 7, has_adjacent_same_but_not_more))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay4('test_day_4'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
