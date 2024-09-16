
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
        if next_instruction_pointer >= len(instructions):
            break
        instruction = instructions[next_instruction_pointer]
        #print("instruction: {}".format(instruction))
        # input("next")
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
            if register not in ["a", "b", "c", "d"]:
                next_instruction_pointer += 1
                continue
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
                    if instruction.split(" ")[2] in ["a", "b", "c", "d"]:
                        next_instruction_pointer += registers[instruction.split(" ")[2]]
                    else:
                        next_instruction_pointer += int(instruction.split(" ")[2])
                else:
                    next_instruction_pointer += 1
        elif instruction.startswith("tgl"):
            register = instruction.split(" ")[1]
            if register == "a" or register == "b" or register == "c" or register == "d":
                toggle_instruction(next_instruction_pointer + registers[register])
                next_instruction_pointer += 1
            else:
                print("bla")
        else:
            print("invalid instruction")
        #print("registers: {}".format(registers))
    return (registers["a"], instruction_counter)

def toggle_instruction( pointer):
    # print("toggle instruction: {}".format(instructions[pointer]))
    if pointer >= len(instructions):
        return
    if "inc" in instructions[pointer]:
        instructions[pointer] = instructions[pointer].replace("inc", "dec")
    elif "dec" in instructions[pointer] or "tgl" in instructions[pointer]:
        instructions[pointer] = instructions[pointer].replace("dec", "inc")
        instructions[pointer] = instructions[pointer].replace("tgl", "inc")
    elif "jnz" in instructions[pointer]:
        instructions[pointer] = instructions[pointer].replace("jnz", "cpy")
    elif "cpy" in instructions[pointer]:
        instructions[pointer] = instructions[pointer].replace("cpy", "jnz")

instructions = []
file1 = open('puzzle23.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    instructions.append(input_line)

task_a = run_assembunny_code(12,0,0,0)
print("TASK 1 - {}".format(task_a))

print("TASK 2 - ")
