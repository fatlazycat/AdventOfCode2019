import unittest
from source.day_3 import *


class TestDay3(unittest.TestCase):
    def test_min_distance(self):
        test_data = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
                     "U62,R66,U55,R34,D71,R55,D58,R83"]
        data = process_data(test_data)
        self.assertEqual(159, min_distance(data))

    def test_part1(self):
        raw_data = parse_file("../resources/day_3_data")
        data = process_data(raw_data)
        self.assertEqual(1983, min_distance(data))

    def test_part2(self):
        raw_data = parse_file("../resources/day_3_data")
        data = process_data(raw_data)
        self.assertEqual(107754, shortest_path(data))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestDay3('test_day_3'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()