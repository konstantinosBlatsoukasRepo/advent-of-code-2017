def parse(input):
    lines = input.strip().split("\n")
    delimiter_removed = [line.split('<->') for line in lines]

    programs = []
    for line in delimiter_removed:
        program_id = int(line[0].strip())
        others = line[1].split(',')

        can_talk_to = set()
        for other_programs in others:
            other_program = int(other_programs.strip())
            can_talk_to.add(other_program)

        programs.append((program_id, can_talk_to))

    return programs


def count_programs_connected_to_zero(programs, connected_to_zero):
    re_check_programs = []

    for program in programs:
        program_id, connect_with = program

        for other_program in connect_with:
            if other_program > program_id and program_id != 0:
                re_check_programs.append(program_id)

            if other_program in connected_to_zero:
                connected_to_zero.add(program_id)

    return (connected_to_zero, re_check_programs)


file = open('day12_input.txt')
input = file.read()

# input = """
# 0 <-> 2
# 1 <-> 1
# 2 <-> 0, 3, 4
# 3 <-> 2, 4
# 4 <-> 2, 3, 6
# 5 <-> 6
# 6 <-> 4, 5
# """

programs = parse(input)

connected_ids = set()
total_groups = 0

for program_id in range(0, len(programs)):
    print(program_id)
    if program_id not in connected_ids:
        connected_to_zero = {program_id}
        connected_to_zero, re_check_programs = count_programs_connected_to_zero(
            programs, connected_to_zero)

        re_check_programs = {
            program_id for program_id in re_check_programs if program_id not in connected_to_zero}

        to_re_check = []
        for program_id, can_talk_to in programs:
            if program_id not in connected_to_zero and program_id in re_check_programs:
                to_re_check.append((program_id, can_talk_to))

        for _ in range(0, len(to_re_check)):
            connected_to_zero, re_check_programs = count_programs_connected_to_zero(
                programs, connected_to_zero)

        if connected_to_zero != {}:
            total_groups += 1

        for connected in connected_to_zero:
            connected_ids.add(connected)


print(total_groups)
