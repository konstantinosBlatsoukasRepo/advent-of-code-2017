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


def find_evenly_divisible(row):
    divisible_numbers = []
    for index in range(0, len(row)):
        if index == len(row) - 1:
            break

        for next in range(index + 1, len(row)):
            if row[index] % row[next] == 0 or row[next] % row[index] == 0:
                divisible_numbers.append(row[index])
                divisible_numbers.append(row[next])

    return divisible_numbers


def sum_divisibles(input):
    divisibles = [find_evenly_divisible(row) for row in input]

    division_results = []
    for divisible in divisibles:
        first = divisible[0]
        second = divisible[1]

        div_result = 0
        if first >= second:
            div_result = first / second
        else:
            div_result = second / first

        division_results.append(div_result)

    return sum(division_results)


# unit tests for the first part
assert min_max_diff([5, 1, 9, 5]) == 8
assert min_max_diff([7, 5, 3]) == 4
assert min_max_diff([2, 4, 6, 8]) == 6

input = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]

assert check_sum(input) == 18

# first part result
input = parse('input.txt')
print(check_sum(input))


# unit tests for the second part
print(find_evenly_divisible([5, 9, 2, 8]))
print(find_evenly_divisible([9, 4, 7, 3]))

input = [[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]]
assert sum_divisibles(input) == 9

# second part result
input = parse('input.txt')
print(sum_divisibles(input))
