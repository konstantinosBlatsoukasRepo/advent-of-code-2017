def count_groups(input):
    in_garbage = False
    in_ignore = False
    depth = 0
    total_score = 0

    total_garbage_chars = 0
    total_ignored = 0

    for c in input:
        if in_ignore:
            in_ignore = False
        elif c == "!":
            in_ignore = True
        elif in_garbage:
            if c == ">":
                in_garbage = False
            else:
                total_garbage_chars += 1
        elif c == "<":
            in_garbage = True
        elif c == "{" and not in_garbage:
            depth += 1
            total_score += depth
        elif c == "}" and not in_garbage:
            depth -= 1

    return (total_score, total_garbage_chars)


file = open("input.txt")
rows = file.read()

total_score, total_garbage_chars = count_groups(rows)
print(total_score)
print(total_garbage_chars)
assert total_score == 9662


total_score, total_garbage_chars = count_groups("<>")
assert total_garbage_chars == 0
total_score, total_garbage_chars = count_groups("<random characters>")
assert total_garbage_chars == 17
total_score, total_garbage_chars = count_groups("<<<<>")
assert total_garbage_chars == 3
total_score, total_garbage_chars = count_groups("<{!>}>")
assert total_garbage_chars == 2
total_score, total_garbage_chars = count_groups("<!!>")
assert total_garbage_chars == 0
total_score, total_garbage_chars = count_groups("<!!!>>")
assert total_garbage_chars == 0
total_score, total_garbage_chars = count_groups("<{o\"i!a,<{i<a>")
assert total_garbage_chars == 10
