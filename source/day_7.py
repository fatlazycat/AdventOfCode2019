from typing import List
from itertools import permutations
from source.day_5 import process_code


def process_amps(code: List[int]):
    current_max = 0
    nums = [0, 1, 2, 3, 4]
    perms = permutations(nums)
    for perm in perms:
        output = 0
        output = process_amp(code, output, perm)
        current_max = max(current_max, output)

    return current_max


def process_amp(code, output, phase):
    for phase_setting in phase:
        output = process_code(code, [phase_setting, output])
    return output
