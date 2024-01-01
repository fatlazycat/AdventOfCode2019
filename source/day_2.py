from source.utils import parse_file
from typing import List


def process_data(s):
    numbers = [int(n) for n in s.split(',')]
    return numbers


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

__all__ = ['parse_file', 'process_code', 'process_data']

# s = parse_file('../resources/day_2_data')[0]
#
# numbers = processData(s)
#
# numbers[1] = 12
# numbers[2] = 2
#
#
# # numbers = processData('1,0,0,0,99')
# # numbers = processData('1,1,1,4,99,5,6,0,99')
#
# process_code(numbers)
#
# print(numbers[0])
