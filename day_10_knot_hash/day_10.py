def get_reversal_indexes(my_list, current_position, length):
    max_index = len(my_list) - 1
    last_index = current_position + length

    indexes = []
    for index in range(current_position, last_index):
        if index > max_index:
            indexes.append(index % len(my_list))
        else:
            indexes.append(index)

    return indexes


def is_length_valid(my_list, length):
    return length <= len(my_list)


def reverse(my_list, reversal_indexes):
    second_swap_index = -1
    for first_swap_index in range(0, len(reversal_indexes) / 2):
        temp = my_list[reversal_indexes[first_swap_index]]
        my_list[reversal_indexes[first_swap_index]
                ] = my_list[reversal_indexes[second_swap_index]]
        my_list[reversal_indexes[second_swap_index]] = temp
        second_swap_index -= 1


def day_ten(my_list, lengths):
    current_position = 0
    skip_size = 0

    for length in lengths:
        if is_length_valid(my_list, length):
            reversal_indexes = get_reversal_indexes(
                my_list, current_position, length)
            reverse(my_list, reversal_indexes)

        current_position = current_position + length + skip_size
        if current_position >= len(my_list):
            current_position = current_position % len(my_list)
        skip_size += 1


my_list = [num for num in range(0, 256)]
lengths = [197, 97, 204, 108, 1, 29, 5, 71, 0, 50, 2, 255, 248, 78, 254, 63]
day_ten(my_list, lengths)
print(my_list[0] * my_list[1])
# my_list = [0, 1, 2, 3, 4]
# lengths = [3, 4, 1, 5]
# day_ten(my_list, lengths)
# print(my_list[0] * my_list[1])
