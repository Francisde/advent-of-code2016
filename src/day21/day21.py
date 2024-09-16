import itertools


def perform_transitions(initial_string, operations):
    result = initial_string
    for line in operations:
        operation = line.strip()
        if operation.startswith("swap position"):
            split_string = operation.split(" ")
            index_one = int(split_string[2])
            index_two = int(split_string[5])
            position_one = min(index_one, index_two)
            position_two = max(index_one, index_two)
            result = "{}{}{}{}{}".format(result[0:position_one], result[position_two], result[position_one + 1: position_two], result[position_one], result[position_two + 1:])
        elif operation.startswith("swap letter"):
            split_string = operation.split(" ")
            letter_one = split_string[2]
            letter_two = split_string[5]
            result = result.replace(letter_two, ".")
            result = result.replace(letter_one, letter_two)
            result = result.replace(".", letter_one)
        elif operation.startswith("reverse positions"):
            split_string = operation.split(" ")
            index_one = int(split_string[2])
            index_two = int(split_string[4])
            substring = result[index_one:index_two+1]
            result = "{}{}{}".format(result[:index_one], substring[::-1], result[index_two + 1:])
        elif operation.startswith("rotate left"):
            split_string = operation.split(" ")
            steps = int(split_string[2])
            result = rotate_string(result, steps)
        elif operation.startswith("rotate right"):
            split_string = operation.split(" ")
            steps = int(split_string[2])
            result = rotate_string(result, 0 - steps)
        elif operation.startswith("rotate based on"):
            split_string = operation.split(" ")
            letter = split_string[6]
            index_one = result.index(letter)
            if index_one < 4:
                result = rotate_string(result, 0 - (index_one + 1))
            else:
                result = rotate_string(result, 0 - (index_one + 2))
        elif operation.startswith("move position"):
            split_string = operation.split(" ")
            index_one = int(split_string[2])
            index_two = int(split_string[5])
            letter = result[index_one]
            result = result[:index_one] + result[index_one + 1:]
            result = result[:index_two] + letter + result[index_two:]
        else:
            print("cant parse: {}".format(operation))
        #(result)
    return result

def rotate_string(input_string, steps):
    result = input_string
    if steps < 0:
        for i in range(abs(steps)):
            result = rotate_string_one_step(result, -1)
    elif steps > 0:
        for i in range(abs(steps)):
            result = rotate_string_one_step(result, 1)
    return result

def rotate_string_one_step(input_string, step):
    return input_string[step:] + input_string[:step]


file1 = open('puzzle21.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1

final_word = perform_transitions("abcdefgh", Lines)

print("TASK 1 - {}".format(final_word))

list_of_possible_passwords = list(itertools.permutations("abcdefgh", 8))
for possible_password in list_of_possible_passwords:
    password = ""
    for character in possible_password:
        password += character
    scrambled_password = perform_transitions(password, Lines)
    if scrambled_password == "fbgdceah":
        print("TASK 2 - {}".format(password))
