states_seen = set()

# part one


def count_redistribution_cycles(memory_banks, total_redistribution_cycles):
    memory_banks_copy = memory_banks[:]
    total_memory_banks = len(memory_banks_copy)

    while True:
        if tuple(memory_banks_copy) in states_seen:
            return (total_redistribution_cycles, memory_banks_copy)
        else:
            states_seen.add(tuple(memory_banks_copy))

            max_blocks = max(memory_banks_copy)
            next_index = get_next_memory_bank_index(
                memory_banks_copy, max_blocks)
            state = redistribute_cycle(
                memory_banks_copy, next_index, total_memory_banks)

            total_redistribution_cycles += 1
            memory_banks_copy = state


def get_next_memory_bank_index(memory_banks, max_blocks):
    enum_banks = enumerate(memory_banks)
    max_indexes = [index for index, total in enum_banks if total == max_blocks]
    return min(max_indexes)


def redistribute_cycle(memory_banks, max_index, total_memory_banks):
    max_blocks = memory_banks[max_index]
    memory_banks[max_index] = 0
    max_index += 1

    for _ in range(0, max_blocks):
        next_index = max_index % total_memory_banks
        memory_banks[next_index] = memory_banks[next_index] + 1
        max_index += 1

    return memory_banks


assert redistribute_cycle([0, 2, 7, 0], 2, len([0, 2, 7, 0])) == [2, 4, 1, 2]

assert get_next_memory_bank_index([0, 2, 7, 0], 7) == 2
assert get_next_memory_bank_index([3, 1, 2, 3], 3) == 0
assert get_next_memory_bank_index([1, 3, 2, 3], 3) == 1


input = [2,	8, 8,	5, 4,	2, 3,	1, 5, 5, 1,	 2,	15,	13,	5, 14]
total_cycles, loop_state = count_redistribution_cycles(input, 0)

# part two


def count_when_loop_state_first_seen(memory_banks, loop_count):
    total_memory_banks = len(memory_banks)

    while True:
        if memory_banks == loop_state:
            return loop_count
        else:
            states_seen.add(tuple(memory_banks))

            max_blocks = max(memory_banks)
            next_index = get_next_memory_bank_index(memory_banks, max_blocks)
            state = redistribute_cycle(
                memory_banks, next_index, total_memory_banks)

            loop_count += 1
            memory_banks = state


loop_till_loop_state = count_when_loop_state_first_seen(input, 0)

part_two = total_cycles - loop_till_loop_state
assert part_two == 1610
