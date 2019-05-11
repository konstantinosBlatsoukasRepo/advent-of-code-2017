states_seen = set()


def count_redistribution_cycles(memory_banks, total_redistribution_cycles):
    total_memory_banks = len(memory_banks)

    while True:
        if tuple(memory_banks) in states_seen:
            return total_redistribution_cycles
        else:
            states_seen.add(tuple(memory_banks))

            max_blocks = max(memory_banks)
            next_index = get_next_memory_bank_index(memory_banks, max_blocks)
            state = redistribute_cycle(
                memory_banks, next_index, total_memory_banks)

            total_redistribution_cycles += 1
            memory_banks = state


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

assert count_redistribution_cycles([0, 2, 7, 0], 0) == 5


input = [2,	8, 8,	5, 4,	2, 3,	1, 5, 5, 1,	 2,	15,	13,	5, 14]
print(count_redistribution_cycles(input, 0))
