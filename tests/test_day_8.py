import unittest

from source.day_8 import part1
from source.utils import parse_file


class TestDay8(unittest.TestCase):
    def test_part1_dummy(self):
        s = parse_file('../resources/day_8_data')
        data = list(map(int, s[0]))
        self.assertEqual(1862, part1(data))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay8('test_day_8'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
