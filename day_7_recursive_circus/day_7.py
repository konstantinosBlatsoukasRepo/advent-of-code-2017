import re
import collections


class Program(object):

    def __init__(self, name, weight, programs_above):
        self.name = name
        self.weight = weight
        self.programs_above = programs_above

    def __repr__(self):
        return "name: " + self.name + "\n" + "weight: " + str(self.weight) + "\n"


def parse(file_name):
    file = open(file_name)
    rows = file.read().splitlines()
    file.close()

    programs = []
    for row in rows:
        no_needed_chars_removed = re.split("[ ,()>-]", row)
        empty_chars_removed = [
            char for char in no_needed_chars_removed if char != '']

        name = empty_chars_removed[0]
        weight = empty_chars_removed[1]
        if len(empty_chars_removed) == 2:
            programs.append(Program(name, int(weight), []))
        else:
            programs.append(
                Program(name, int(weight), empty_chars_removed[2:]))

    return programs


def get_bottom_program_name(input):
    programs = parse(input)

    all_programs_set = set()
    for program in programs:
        all_programs_set.add(program.name)

    all_programs_above = [program.programs_above for program in programs]

    flattened_programs_above = set()
    for program_above in all_programs_above:
        if program_above != []:
            for name in program_above:
                flattened_programs_above.add(name)

    root = [
        program for program in all_programs_set if program not in flattened_programs_above]

    return root[0]


assert get_bottom_program_name('test.txt') == 'tknk'


def calculate_program_weight(program, programs):
    if program.programs_above == []:
        return program.weight
    else:
        other_programs = []
        for program_above_name in program.programs_above:
            program_above = [
                programz for programz in programs if programz.name == program_above_name][0]
            other_programs.append(program_above)

        return sum([calculate_program_weight(other, programs) for other in other_programs]) + program.weight


programs = parse('input.txt')
root = 'vvsvez'
broken_node = None

while True:
    root = [program for program in programs if program.name == root][0]

    root_childs = []
    for program_above_name in root.programs_above:
        program_above = [
            programz for programz in programs if programz.name == program_above_name][0]
        root_childs.append(program_above)

    child_weights = [calculate_program_weight(
        child, programs) for child in root_childs]

    if len(set(child_weights)) == 1:
        broken_node = root
        break
    else:
        unbalanced_weight = [weight for weight, occurrence in collections.Counter(
            child_weights).items() if occurrence == 1][0]

        unbalanced_child = None
        for a in zip(root_childs, child_weights):
            current_child, weight = a
            if weight == unbalanced_weight:
                unbalanced_child = current_child

        root = unbalanced_child.name


print(broken_node)

# print([calculate_program_weight(
#     child, programs) for child in unbalanced_child.programs_above])
# weight_for_loss = max(child_weights) - min(child_weights)
# print(weight_for_loss)
