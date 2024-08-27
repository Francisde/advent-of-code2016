import copy


def print_display(matrix):
    for row in matrix:
        print(row)
    print()

def count_pixel_lit(matrix):
    counter = 0
    for row in matrix:
        for pixel in row:
            if pixel == "#":
                counter += 1
    return counter


def perform_rect(matrix, a, b):
    for i in range(b):
        for j in range(a):
            matrix[i][j] = "#"

def perform_rotate_col(matrix, a, b):
    print("perform rotate col: a= {}, b= {}".format(a, b))
    old_matrix = copy.deepcopy(matrix)
    for i in range(b):
        for j in range(tall):
            matrix[(j + 1) % tall][a] = old_matrix[j][a]
        old_matrix = copy.deepcopy(matrix)

def perform_rotate_row(matrix, a, b):
    print("perform rotate row: a= {}, b= {}".format(a, b))
    old_matrix = copy.deepcopy(matrix)
    for i in range(b):
        for j in range(wide):
            matrix[a][(j + 1) % wide] = old_matrix[a][j]
        old_matrix = copy.deepcopy(matrix)


file1 = open('puzzle08.txt', 'r')
Lines = file1.readlines()

count = 0
wide = 50
tall = 6

display = [["." for i in range(wide)] for j in range(tall)]
print_display(display)
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    if "rect" in input_line:
        param = input_line.split(" ")[1]
        param = param.split("x")
        perform_rect(display, int(param[0]), int(param[1]))
    elif "rotate row" in input_line:
        split_line = input_line.split(" ")
        param_a = int(split_line[2].split("=")[1])
        param_b = int(split_line[4])
        perform_rotate_row(display, param_a, param_b)
    elif "rotate column" in input_line:
        split_line = input_line.split(" ")
        param_a = int(split_line[2].split("=")[1])
        param_b = int(split_line[4])
        perform_rotate_col(display, param_a, param_b)
    print_display(display)



print("TASK 1 - how many pixels should be lit?: {}".format(count_pixel_lit(display)))

print("TASK 2 - ")
