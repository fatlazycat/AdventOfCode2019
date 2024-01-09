from typing import List
from itertools import permutations
from source.day_5 import process_code, process_code_state, State


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


def process_loop(code: List[int], phase: [int]):
    amps = [
        State(code=code.copy(), index=0, input=[phase[0], 0], output=[]),
        State(code=code.copy(), index=0, input=[phase[1]], output=[]),
        State(code=code.copy(), index=0, input=[phase[2]], output=[]),
        State(code=code.copy(), index=0, input=[phase[3]], output=[]),
        State(code=code.copy(), index=0, input=[phase[4]], output=[])
            ]
    index = 0
    while not amps[4].terminated:
        process_code_state(amps[(index+1)%5])
        amps[(index+1)%5].input = amps[index%5].output
        index += 1

    return amps[4].output[-1]


__all__ = ['process_amp', 'process_amps', 'process_loop']
