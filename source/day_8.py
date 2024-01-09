from typing import List


def split_list(input_list, size):
    return [input_list[i:i+size] for i in range(0, len(input_list), size)]


def parse_image_data(data: List[int], width: int, height: int) -> List[int]:
    return split_list(data, width*height)


def number_of_zero(ints: List[int]):
    return ints.count(0)


def part1(data: List[int]) -> int:
    layers: List[int] = parse_image_data(data, 25, 6)
    layer_with_zero = min(layers, key=number_of_zero)
    ones = layer_with_zero.count(1)
    twos = layer_with_zero.count(2)
    return ones * twos


__all__ = ['part1']
