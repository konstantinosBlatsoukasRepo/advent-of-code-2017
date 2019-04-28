def generate(number):
    nums_coordinates = {}
    square_length = 3

    current_number = 1

    x = 0
    y = 0

    while current_number <= number:
        nums_coordinates[current_number] = (x, y)

        y += 1
        current_number += 1
        nums_coordinates[current_number + 1] = (x, y)

        for _ in range(0, square_length - 2):
            current_number += 1
            x += 1
            nums_coordinates[current_number] = (x, y)

        for _ in range(0, square_length - 1):
            current_number += 1
            y -= 1
            nums_coordinates[current_number] = (x, y)

        for _ in range(0, square_length - 1):
            current_number += 1
            x -= 1
            nums_coordinates[current_number] = (x, y)

        for _ in range(0, square_length - 1):
            current_number += 1
            y += 1
            nums_coordinates[current_number] = (x, y)

        square_length += 2

    return nums_coordinates


def steps_from(square):
    square_coordinates = generate(square)
    (x, y) = square_coordinates[square]
    return abs(x) + abs(y)


assert steps_from(1) == 0
assert steps_from(12) == 3
assert steps_from(23) == 2
assert steps_from(1024) == 31


print(steps_from(368078))
