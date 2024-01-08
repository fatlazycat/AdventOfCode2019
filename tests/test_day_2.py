import unittest
from source.day_2 import *


class TestDay2(unittest.TestCase):
    def test_process_code(self):
        numbers = process_data('1,0,0,0,99')
        process_code(numbers)
        self.assertEqual(numbers, [2, 0, 0, 0, 99])

        numbers = process_data('2,3,0,3,99')
        process_code(numbers)
        self.assertEqual(numbers, [2, 3, 0, 6, 99])

        numbers = process_data('2,4,4,5,99,0')
        process_code(numbers)
        self.assertEqual(numbers, [2, 4, 4, 5, 99, 9801])

    def test_part1(self):
        s = parse_file('../resources/day_2_data')[0]
        numbers = process_data(s)
        numbers[1] = 12
        numbers[2] = 2
        process_code(numbers)
        self.assertEqual(3760627, numbers[0])

    def test_part2(self):
        s = parse_file('../resources/day_2_data')[0]
        numbers = process_data(s)
        actual = find_codes(numbers)
        self.assertEqual(7195, actual)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay2('test_day_2'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
