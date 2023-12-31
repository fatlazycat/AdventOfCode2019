def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

__all__ = ['parse_file']