from source.utils import parse_file

def fuel(mass):
    # Your function implementation here
    return mass // 3 - 2

def calculate_total_fuel(filename):
    data = parse_file(filename)
    data = map(int, data)
    # mapping fuel function over data
    fuel_data = map(fuel, data)

    # Summing the values
    total_fuel = sum(fuel_data)

    return total_fuel

print(calculate_total_fuel("../resources/day_1_data"))

__all__ = ['parse_file', 'fuel', 'calculate_total_fuel']