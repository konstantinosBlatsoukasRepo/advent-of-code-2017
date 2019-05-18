class Condition(object):
    def __init__(self, first_operand, second_operand, operator):
        self.first_operand = first_operand
        self.second_operand = second_operand
        self.operator = operator

    def perform_operation(self):
        if self.operator == ">":
            return self.first_operand > self.second_operand
        elif self.operator == "<":
            return self.first_operand < self.second_operand
        elif self.operator == "<=":
            return self.first_operand <= self.second_operand
        elif self.operator == ">=":
            return self.first_operand >= self.second_operand
        elif self.operator == "==":
            return self.first_operand == self.second_operand
        elif self.operator == "!=":
            return self.first_operand != self.second_operand


assert Condition(4, 5, ">").perform_operation() == False
assert Condition(40, 5, ">").perform_operation() == True
assert Condition(4, 4, "==").perform_operation() == True


class Command(object):
    def __init__(self, first_operand, second_operand, command):
        self.first_operand = first_operand
        self.second_operand = second_operand
        self.command = command

    def execute(self):
        if self.command == "inc":
            self.first_operand += self.second_operand
            return self.first_operand
        elif self.command == "dec":
            self.first_operand -= self.second_operand
            return self.first_operand


assert Command(1, 1, "inc").execute() == 2
assert Command(5, 1, "dec").execute() == 4


class Instruction(object):
    def __init__(self, command, condition):
        self.command = command
        self.condition = condition


def parse(input):
    unparsed_instructions = input.splitlines()

    initial_registers_values = {}
    for unparsed_instruction in unparsed_instructions:
        register = unparsed_instruction.split()[0]
        initial_registers_values[register] = 0

    initial_instructions = []
    for unparsed_instruction in unparsed_instructions:
        unparsed_instruction = unparsed_instruction.split()

        second_op = int(unparsed_instruction[2])
        first_op = unparsed_instruction[0]
        command = unparsed_instruction[1]
        current_command = Command(first_op, second_op, command)

        second_con_op = int(unparsed_instruction[6])
        first_con_op = unparsed_instruction[4]
        condition = unparsed_instruction[5]
        current_condition = Condition(first_con_op, second_con_op, condition)

        initial_instructions.append(Instruction(
            current_command, current_condition))

    return (initial_instructions, initial_registers_values)


def condition_result(instruction, registers_values):
    cond_num = instruction.condition.first_operand
    first_cond_operand = registers_values[cond_num]
    second_cond_operand = instruction.condition.second_operand
    cond_operator = instruction.condition.operator
    condition = Condition(first_cond_operand,
                          second_cond_operand, cond_operator)
    return condition.perform_operation()


def execute_command(instruction, registers_values):
    op_num = instruction.command.first_operand
    first_op_operand = registers_values[op_num]
    second_op_operand = instruction.command.second_operand
    comm = instruction.command.command
    command = Command(first_op_operand,
                      second_op_operand, comm)
    result = command.execute()
    registers_values[op_num] = result


input = """b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
"""
instructions, registers_values = parse(input)

max_of_maxs = []
for instruction in instructions:
    if condition_result(instruction, registers_values):
        execute_command(instruction, registers_values)
        max_of_maxs.append(max(registers_values.values()))

print(max(registers_values.values()))
print(max(max_of_maxs))
