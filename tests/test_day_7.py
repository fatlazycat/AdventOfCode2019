import unittest
from source.day_7 import process_amps, process_amp
from source.day_5 import process_data, parse_file


class TestDay7(unittest.TestCase):
    def test_part1_dummy(self):
        numbers = process_data("3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0")
        self.assertEqual(43210, process_amp(numbers, 0, [4, 3, 2, 1, 0]))
        numbers = process_data("3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0")
        self.assertEqual(54321, process_amp(numbers, 0, [0, 1, 2, 3, 4]))

    def test_part1(self):
        s = parse_file('../resources/day_7_data')[0]
        numbers = process_data(s)
        self.assertEqual(38834, process_amps(numbers))

    # def test_part2_dummy(self):
    #     numbers = process_data("3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5")
    #     self.assertEqual(139629729, process_amp(numbers, 0, [9,8,7,6,5]))



def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay7('test_day_7'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()