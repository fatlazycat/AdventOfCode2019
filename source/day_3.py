from source.utils import parse_file
from enum import Enum
from shapely.geometry import Point, LineString
from shapely.measurement import length as line_length
from shapely.ops import split
from shapely import intersection_all
from typing import List


class Direction(Enum):
    UP = 'U'
    DOWN = 'D'
    LEFT = 'L'
    RIGHT = 'R'


def process_data(rows):
    parsed_data = []
    for row in rows:
        directions = row.split(',')
        parsed_line = [(Direction(ins[0]), int(ins[1:])) for ins in directions]
        parsed_data.append(parsed_line)
    return parsed_data


def create_line_string(data):
    line_string = [(0, 0)]
    current_point = (0, 0)
    for direction, distance in data:
        if direction == Direction.UP:
            current_point = (current_point[0], current_point[1] + distance)
        elif direction == Direction.DOWN:
            current_point = (current_point[0], current_point[1] - distance)
        elif direction == Direction.LEFT:
            current_point = (current_point[0] - distance, current_point[1])
        elif direction == Direction.RIGHT:
            current_point = (current_point[0] + distance, current_point[1])
        line_string.append(current_point)
    return line_string


def manhattan_distance(p: Point):
    return int(abs(p.x) + abs(p.y))


def min_distance(data):
    line_strings = list(map(create_line_string, data))
    lines = list(map(LineString, line_strings))
    intersections = intersection_all(lines)
    list_of_points = list(intersections.geoms)
    distances = list(map(manhattan_distance, list_of_points))
    return min(distances)


def shortest_path(data: List[str]):
    line_strings = list(map(create_line_string, data))
    lines = list(map(LineString, line_strings))
    intersections = intersection_all(lines)
    list_of_intersections = list(intersections.geoms)
    distances = []

    for intersection in list_of_intersections:
        line_distances = 0
        for line in lines:
            line_parts = split(line, intersection)
            line_distances += line_length(line_parts.geoms[0])
        distances.append(line_distances)
    return min(distances)


test_data = ["R75,D30,R83,U83,L12,D49,R71,U7,L72",
             "U62,R66,U55,R34,D71,R55,D58,R83"]
# test_data = ["R8,U5,L5,D3",
#              "U7,R6,D4,L4"]
data = process_data(test_data)
print(shortest_path(data))


__all__ = ['parse_file', 'process_data', 'min_distance']
