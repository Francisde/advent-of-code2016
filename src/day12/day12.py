
def run_assembunny_code(a, b, c, d ):
    registers = dict()
    registers["a"] = a
    registers["b"] = b
    registers["c"] = c
    registers["d"] = d
    next_instruction_pointer = 0
    instruction_counter = 0
    while True:
        instruction_counter += 1
        instruction = instructions[next_instruction_pointer]
        if instruction == "END" or next_instruction_pointer > len(instructions):
            break
        elif instruction.startswith("inc"):
            register = instruction.split(" ")[1]
            registers[register] += 1
            next_instruction_pointer += 1
        elif instruction.startswith("dec"):
            register = instruction.split(" ")[1]
            registers[register] -= 1
            next_instruction_pointer += 1
        elif instruction.startswith("cpy"):
            register = instruction.split(" ")[2]
            value = instruction.split(" ")[1]
            value_int = 0
            if value == "a" or value == "b" or value == "c" or value == "d":
                value_int = registers[value]
            else:
                value_int = int(value)
            registers[register] = value_int
            next_instruction_pointer += 1
        elif instruction.startswith("jnz"):
            register = instruction.split(" ")[1]
            if register == "a" or register == "b" or register == "c" or register == "d":
                if registers[register] != 0:
                    next_instruction_pointer += int(instruction.split(" ")[2])
                else:
                    next_instruction_pointer += 1
            else:
                int_value = int(register)
                if int_value != 0:
                    next_instruction_pointer += int(instruction.split(" ")[2])
                else:
                    next_instruction_pointer += 1
    return (registers["a"], instruction_counter)

file1 = open('puzzle12.txt', 'r')
Lines = file1.readlines()

count = 0

instructions = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    instructions.append(input_line)

instructions.append("END")

task_a = run_assembunny_code(0,0,0,0)

print("TASK 1 - value of register a: {}, total instructions: {}".format(task_a[0], task_a[1]))

task_b = run_assembunny_code(0,0,1,0)
print("TASK 2 - value of register a: {}, total instructions: {}".format(task_b[0], task_b[1]))
