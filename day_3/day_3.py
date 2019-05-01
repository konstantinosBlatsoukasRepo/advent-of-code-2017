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


# part one unit tests
assert steps_from(1) == 0
assert steps_from(12) == 3
assert steps_from(23) == 2
assert steps_from(1024) == 31


def generate_sums(number):
    square_length = 3

    x = 0
    y = 0

    nums_coordinates = {}
    nums_coordinates[(0, 0)] = 1

    while True:
        nums_coordinates[(x, y)] = compute_value(nums_coordinates, x, y)
        if nums_coordinates[(x, y)] > number:
            return nums_coordinates[(x, y)]

        y += 1
        nums_coordinates[(x, y)] = compute_value(nums_coordinates, x, y)
        if nums_coordinates[(x, y)] > number:
            return nums_coordinates[(x, y)]

        for _ in range(0, square_length - 2):
            x += 1
            nums_coordinates[(x, y)] = compute_value(nums_coordinates, x, y)
            if nums_coordinates[(x, y)] > number:
                return nums_coordinates[(x, y)]

        for _ in range(0, square_length - 1):
            y -= 1
            nums_coordinates[(x, y)] = compute_value(nums_coordinates, x, y)
            if nums_coordinates[(x, y)] > number:
                return nums_coordinates[(x, y)]

        for _ in range(0, square_length - 1):
            x -= 1
            nums_coordinates[(x, y)] = compute_value(nums_coordinates, x, y)
            if nums_coordinates[(x, y)] > number:
                return nums_coordinates[(x, y)]

        for _ in range(0, square_length - 1):
            y += 1
            nums_coordinates[(x, y)] = compute_value(nums_coordinates, x, y)
            if nums_coordinates[(x, y)] > number:
                return nums_coordinates[(x, y)]

        square_length += 2

    return nums_coordinates


def compute_value(nums_coordinates, x, y):
    if x == 0 and y == 0:
        return 1

    value = 0

    if (x + 1, y) in nums_coordinates:
        value += nums_coordinates[(x + 1, y)]

    if (x - 1, y) in nums_coordinates:
        value += nums_coordinates[(x - 1, y)]

    if (x, y + 1) in nums_coordinates:
        value += nums_coordinates[(x, y + 1)]

    if (x, y - 1) in nums_coordinates:
        value += nums_coordinates[(x, y - 1)]

    if (x - 1, y - 1) in nums_coordinates:
        value += nums_coordinates[(x - 1, y - 1)]

    if (x + 1, y + 1) in nums_coordinates:
        value += nums_coordinates[(x + 1, y + 1)]

    if (x + 1, y - 1) in nums_coordinates:
        value += nums_coordinates[(x + 1, y - 1)]

    if (x - 1, y + 1) in nums_coordinates:
        value += nums_coordinates[(x - 1, y + 1)]

    return value


# part two unit tests
assert generate_sums(747) == 806
assert generate_sums(23) == 25
assert generate_sums(54) == 57

print(generate_sums(368078))
