def count_groups(input):
    in_garbage = False
    in_ignore = False
    depth = 0
    total_score = 0

    for c in input:
        if in_ignore:
            in_ignore = False
        elif c == "!":
            in_ignore = True
        elif c == ">":
            in_garbage = False
        elif c == "<":
            in_garbage = True
        elif c == "{" and not in_garbage:
            depth += 1
            total_score += depth
        elif c == "}" and not in_garbage:
            depth -= 1
    return total_score


assert count_groups("{}") == 1
assert count_groups("{{{}}}") == 6
assert count_groups("{{},{}}") == 5
assert count_groups("{{{},{},{{}}}}") == 16
assert count_groups("{<a>,<a>,<a>,<a>}") == 1
assert count_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}") == 9
assert count_groups("{{<!!>},{<!!>},{<!!>},{<!!>}}") == 9
assert count_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}") == 3

# {{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
# {{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
# {{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.


file = open("input.txt")
rows = file.read()
print(count_groups(rows))
