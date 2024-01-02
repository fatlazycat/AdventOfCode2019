from source.utils import parse_file
from typing import List


def process_data(s):
    return [int(n) for n in s.split(',')]


def process_code(code: List[int]):
    index = 0

    while code[index] != 99:
        opcode = code[index]
        if opcode == 1:
            operand1 = code[code[index+1]]
            operand2 = code[code[index+2]]
            result_index = code[index+3]
            code[result_index] = operand1 + operand2
        elif opcode == 2:
            operand1 = code[code[index+1]]
            operand2 = code[code[index+2]]
            result_index = code[index+3]
            code[result_index] = operand1 * operand2
        index += 4


def find_codes(code: List[int]):
    for noun in range(100):
        for verb in range(100):
            temp_code = code.copy()
            temp_code[1] = noun
            temp_code[2] = verb
            process_code(temp_code)
            if temp_code[0] == 19690720:
                return 100 * noun + verb


__all__ = ['parse_file', 'process_code', 'process_data', 'find_codes']
