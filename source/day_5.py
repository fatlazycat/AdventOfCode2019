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


def jump_if(code: List[int], param1, param2, param_mode1, param_mode2, conditional_test):
    v1 = read_process_mode(code, param1, param_mode1)
    v2 = read_process_mode(code, param2, param_mode2)
    if conditional_test(v1):
        return v2
    else:
        return None


def opcode5_conditional(val: int):
    return val != 0


def opcode6_conditional(val: int):
    return val == 0


def opcode7_conditional(v1: int, v2: int):
    return 1 if v1 < v2 else 0


def opcode8_conditional(v1: int, v2: int):
    return 1 if v1 == v2 else 0


def process_index(index, result):
    if result is not None:
        index = result
    else:
        index += 3
    return index


def write_process_mode(code: List[int], parameter_index: int, value: int):
    code[code[parameter_index]] = value


def process_code(code: List[int], starting_input: List[int]):
    index: int = 0
    output: int = 0
    input_index: int = 0

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
            assert input_index < len(starting_input)
            code[code[index + 1]] = starting_input[input_index]
            index += 2
            input_index += 1
        elif opcode == 4:
            output = read_process_mode(code, code[index + 1], first_mode)
            # print(output)
            index += 2
        elif opcode == 5:
            result = jump_if(code, code[index + 1], code[index + 2], first_mode, second_mode, opcode5_conditional)
            index = process_index(index, result)
        elif opcode == 6:
            result = jump_if(code, code[index + 1], code[index + 2], first_mode, second_mode, opcode6_conditional)
            index = process_index(index, result)
        elif opcode == 7:
            result = opcode7_conditional(read_process_mode(code, code[index + 1], first_mode),
                                         read_process_mode(code, code[index + 2], second_mode))
            code[code[index + 3]] = result
            index += 4
        elif opcode == 8:
            result = opcode8_conditional(read_process_mode(code, code[index + 1], first_mode),
                                         read_process_mode(code, code[index + 2], second_mode))
            code[code[index + 3]] = result
            index += 4
        else:
            raise Exception("Unknown opcode " + str(opcode))

    return output


__all__ = ['parse_file', 'process_code', 'process_data']
