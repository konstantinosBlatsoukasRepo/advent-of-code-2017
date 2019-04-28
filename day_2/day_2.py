import sys


def parse(file_name):
    file = open(file_name)
    rows = file.read().splitlines()
    file.close()

    splitted_rows = [row.split('\t') for row in rows]

    parsed_rows = []
    for splitted_row in splitted_rows:
        parsed_rows.append([int(element) for element in splitted_row])

    return parsed_rows


def check_sum(input):
    return sum([min_max_diff(row) for row in input])


def min_max_diff(row):
    max = -sys.maxsize
    min = sys.maxsize

    for element in row:
        if element > max:
            max = element
        if element < min:
            min = element

    return max - min


assert min_max_diff([5, 1, 9, 5]) == 8
assert min_max_diff([7, 5, 3]) == 4
assert min_max_diff([2, 4, 6, 8]) == 6

input = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]

assert check_sum(input) == 18

input = parse('input.txt')
print(check_sum(input))
