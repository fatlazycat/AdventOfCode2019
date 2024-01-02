from source.utils import parse_file
from enum import Enum
from shapely.geometry import Point, LineString
from shapely import intersection_all


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
    line_string = []
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


__all__ = ['parse_file', 'process_data', 'min_distance']
