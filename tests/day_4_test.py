import unittest
from source.day_4 import *

# lower_val = 382345
# lower_val_adjusted = "388888"
# upper_val = 843167
# upper_val_adjusted = "799999"


class TestDay4(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(460, valid_passwords(3, 8, 7))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay4('test_day_4'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
