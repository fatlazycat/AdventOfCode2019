from source.utils import parse_file


def array_of_int(filename):
    data = parse_file(filename)
    return list(map(int, data))


def fuel(mass):
    # Your function implementation here
    return mass // 3 - 2


def calculate_total_fuel(data):
    fuel_data = list(map(fuel, data))
    total_fuel = sum(fuel_data)
    return total_fuel


def calculate_total_fuel_with_extra_fuel(data):
    modules = list(map(fuel, data))
    extra_fuel = list(map(fuel_for_fuel, modules))
    return sum(modules) + sum(extra_fuel)


def fuel_for_fuel(starting_fuel):
    result = 0
    new_fuel = starting_fuel
    while True:
        new_fuel = fuel(new_fuel)

        if new_fuel <= 0:
            break

        result += new_fuel

    return result


input = array_of_int("../resources/day_1_data")

print(calculate_total_fuel(input))
print(calculate_total_fuel_with_extra_fuel(input))

__all__ = ['parse_file', 'fuel', 'calculate_total_fuel', 'fuel_for_fuel', 'calculate_total_fuel_with_extra_fuel', 'array_of_int']
