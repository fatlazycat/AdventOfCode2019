from source.utils import parse_file
from typing import List


def process_data(s):
    return [int(n) for n in s.split(',')]


def read_process_mode(code: List[int], value, mode):
    if mode == 0:
        return code[value]
    elif mode == 1:
        return value
    else:
        raise Exception("Unknown read mode")


def write_process_mode(code: List[int], parameter_index: int, value: int):
    code[code[parameter_index]] = value


def process_code(code: List[int], starting_input):
    index: int = 0
    output: int = 0

    while code[index] != 99:
        s = str(code[index]).rjust(5, '0')
        opcode = int(s[3:5])
        # third_mode = int(s[0:1])
        second_mode = int(s[1:2])
        first_mode = int(s[2:3])

        if opcode == 1:
            operand1 = read_process_mode(code, code[index + 1], first_mode)
            operand2 = read_process_mode(code, code[index + 2], second_mode)
            code[code[index + 3]] = operand1 + operand2
            index += 4
        elif opcode == 2:
            operand1 = read_process_mode(code, code[index + 1], first_mode)
            operand2 = read_process_mode(code, code[index + 2], second_mode)
            code[code[index + 3]] = operand1 * operand2
            index += 4
        elif opcode == 3:
            code[code[index + 1]] = starting_input
            index += 2
        elif opcode == 4:
            output = read_process_mode(code, code[index + 1], first_mode)
            print(output)
            index += 2
        else:
            raise Exception("Unknown opcode " + str(opcode))

    return output


__all__ = ['parse_file', 'process_code', 'process_data']
