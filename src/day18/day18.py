def print_field(input_field):
    for row in input_field:
        print(row)
    print()

def generate_rows(field, n):
    counter = 0
    while counter < n - 1:
        counter += 1
        new_row = []
        last_row = field[len(field) - 1]
        for i in range(len(last_row)):
            left_save = True
            right_save = True
            center_save = last_row[i] == "."
            if i != 0 and last_row[i - 1] == "^":
                left_save = False
            if i < len(last_row) -1 :
                if last_row[i + 1] == "^":
                    right_save = False
            is_trap = False
            if not left_save and not center_save and right_save:
                is_trap = True
            elif left_save and not center_save and not right_save:
                is_trap = True
            elif left_save and center_save and not right_save:
                is_trap = True
            elif not left_save and center_save and right_save:
                is_trap = True
            if is_trap:
                new_row.append("^")
            else:
                new_row.append(".")
        field.append(new_row)
    return field

file1 = open('puzzle18.txt', 'r')
Lines = file1.readlines()

count = 0

field = []
start_row = []
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    for character in input_line:
        start_row.append(character)
field.append(start_row)
print_field(field)
new_field = generate_rows(field, 400000)
print_field(new_field)
number_of_save_tiles = 0
for row in new_field:
    for character in row:
        if character == ".":
            number_of_save_tiles += 1
print("TASK 1 - number of save tiles: {}".format(number_of_save_tiles))

print("TASK 2 - ")
