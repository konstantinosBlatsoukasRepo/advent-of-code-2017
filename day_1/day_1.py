file = open('input.txt')
numbers = file.read()
file.close()


def captcha(numbers):
    final_numbers = []
    total_numbers = len(numbers)

    for index in range(0, total_numbers):
        if index == total_numbers - 1:
            current_number = numbers[index]
            next_number = numbers[0]
        else:
            current_number = numbers[index]
            next_number = numbers[index + 1]

        if current_number == next_number:
            final_numbers.append(int(current_number))

    return sum(final_numbers)


assert captcha('1122') == 3
assert captcha('1111') == 4
assert captcha('1234') == 0
assert captcha('91212129') == 9

print(captcha(numbers))
