def captcha(numbers):
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


assert captcha('1122') == 3
assert captcha('1111') == 4
assert captcha('1234') == 0
assert captcha('91212129') == 9

file = open('input.txt')
numbers = file.read()
file.close()

print(captcha(numbers))
