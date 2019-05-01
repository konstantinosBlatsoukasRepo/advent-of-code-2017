import collections


def parse(file_name):
    file = open(file_name)
    rows = file.read().splitlines()
    file.close()

    splitted_rows = [row.split('\t') for row in rows]

    parsed_rows = []
    for splitted_row in splitted_rows:
        parsed_rows.append([element for element in splitted_row])

    return parsed_rows


def count_valid(passphrases, is_valid):
    total_valid_passphrases = 0
    for passphrase in passphrases:
        if is_valid(passphrase[0]):
            total_valid_passphrases += 1
    return total_valid_passphrases


def are_valid(words_occurrences):
    for value in words_occurrences:
        if value != 1:
            return False
    return True


def is_valid(passphrase):
    words = passphrase.split()
    counted_words = collections.Counter(words)
    words_occurrences = counted_words.values()
    return are_valid(words_occurrences)


def is_valid_enhanced(passphrase):
    words = passphrase.split()
    sorted_words = [''.join(sorted(word)) for word in words]
    counted_words = collections.Counter(sorted_words)
    words_occurrences = counted_words.values()
    return are_valid(words_occurrences)


# part one unit tests
assert is_valid("aa bb cc dd ee") == True
assert is_valid("aa bb cc dd aa") == False
assert is_valid("aa bb cc dd aaa") == True

input = parse('input.txt')
print("Part one result: {}".format(count_valid(input, is_valid)))

# part 2 unit tests
assert is_valid_enhanced("abcde fghij") == True
assert is_valid_enhanced("abcde xyz ecdab") == False
assert is_valid_enhanced("a ab abc abd abf abj") == True
assert is_valid_enhanced("iiii oiii ooii oooi oooo") == True
assert is_valid_enhanced("oiii ioii iioi iiio") == False

print("Part two result: {}".format(count_valid(input, is_valid_enhanced)))
