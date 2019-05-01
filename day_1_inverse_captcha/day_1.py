def part_1(numbers):
    final_numbers = []
    total_numbers = len(numbers)

    for index in range(0, total_numbers):
        current_number = numbers[index]
        next_number = get_next_number(index, total_numbers, numbers)

        if current_number == next_number:
            final_numbers.append(int(current_number))

    return sum(final_numbers)


def get_next_number(index, total_numbers, numbers):
    if index == total_numbers - 1:
        return numbers[0]
    else:
        return numbers[index + 1]


def part_2(numbers):
    total_numbers = len(numbers)

    upper_bound = int(total_numbers / 2)

    final_numbers = []
    for index in range(0, upper_bound):
        current_number = int(numbers[index])
        next_number = int(numbers[index + upper_bound])

        if current_number == next_number:
            final_numbers.append(current_number)
            final_numbers.append(next_number)

    return sum(final_numbers)


assert part_2('1212') == 6
assert part_2('1221') == 0
assert part_2('123425') == 4
assert part_2('123123') == 12
assert part_2('12131415') == 4

assert part_1('1122') == 3
assert part_1('1111') == 4
assert part_1('1234') == 0
assert part_1('91212129') == 9

file = open('input.txt')
numbers = file.read()
file.close()

print(part_1(numbers))
print(part_2(numbers))
