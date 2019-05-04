def parse(file_name):
    file = open(file_name)
    rows = file.read().splitlines()
    file.close()
    return [int(row) for row in rows]


def steps_to_reach_exit(jump_offsets):
    step_counter = 0
    next_index = 0

    while True:
        previous_index = next_index
        try:
            next_index = previous_index + jump_offsets[next_index]
            step_counter += 1
        except IndexError:
            return step_counter

        jump_offsets[previous_index] += 1


assert steps_to_reach_exit([0, 3, 0, 1, -3]) == 5

jump_offsets = parse('input.txt')
print(steps_to_reach_exit(jump_offsets))
