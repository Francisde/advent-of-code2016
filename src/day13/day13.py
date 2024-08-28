
def print_room(room):
    for row in room:
        for entry in row:
            if entry == 0:
                print("#", end='')
            elif entry == 1:
                print(".", end='')
            elif entry == 2:
                print("O", end='')
            elif entry == 5000:
                print("X", end='')
            else:
                print("O", end='')
        print()
    print()

def generate_room(n, fav_number, default_wall, default_path):
    room =[[0 for i in range(n)] for j in range(n)]
    for x in range(len(room)):
        for y in range(len(room[0])):
            value = x * x + 3 * x + 2 * x * y + y + y * y
            value += fav_number
            one_bits = value.bit_count()
            if one_bits % 2 == 1:
                room[y][x] = default_wall
            else:
                room[y][x] = default_path
    return room

def generate_solution_part_1(room, current_x, current_y, final_x, final_y, current_length, min_found_length):
    if current_x == final_x and current_y == final_y:
        print_room(room)
        return current_length
    if current_length + 1 >= min_found_length:
        return None

    # go all four steps
    # go left
    if current_x > 0:
        if room[current_x - 1][current_y] != 0 and room[current_x - 1][current_y] != 2:
            room[current_x - 1][current_y] = 2
            length = generate_solution_part_1(room, current_x - 1, current_y, final_x, final_y, current_length + 1, min_found_length)
            room[current_x - 1][current_y] = 1
            if length is not None and length < max_length:
                if length < min_found_length:
                    min_found_length = length
    # go right
    if current_x < len(matrix) - 1:
        if room[current_x + 1][current_y] != 0 and room[current_x + 1][current_y] != 2:
            room[current_x + 1][current_y] = 2
            length = generate_solution_part_1(room, current_x + 1, current_y, final_x, final_y, current_length + 1, min_found_length)
            room[current_x + 1][current_y] = 1
            if length is not None and length < max_length:
                if length < min_found_length:
                    min_found_length = length
    # go down
    if current_y < len(matrix) - 1:
        if room[current_x][current_y + 1] != 0 and room[current_x][current_y + 1] != 2:
            room[current_x][current_y + 1] = 2
            length = generate_solution_part_1(room, current_x, current_y + 1, final_x, final_y, current_length + 1, min_found_length)
            room[current_x ][current_y + 1] = 1
            if length is not None and length < max_length:
                if length < min_found_length:
                    min_found_length = length
    # go up
    if current_y > 0:
        if room[current_x][current_y - 1] != 0 and room[current_x][current_y - 1] != 2:
            room[current_x][current_y - 1] = 2
            length = generate_solution_part_1(room, current_x, current_y - 1, final_x, final_y, current_length + 1, min_found_length)
            room[current_x ][current_y - 1] = 1
            if length is not None and length < max_length:
                if length < min_found_length:
                    min_found_length = length
    return min_found_length

def generate_solution_part_2(room, current_x, current_y, current_length):
    print("x: {}, y: {}, length: {}, current_value: {}".format(current_x, current_y, current_length, global_matrix[current_x][current_y]))
    # print(global_matrix)
    # input("bla")
    if current_length == 51:
        if global_matrix[current_x][current_y] == 1:
            global_matrix[current_x][current_y] = 50
        return
    if global_matrix[current_x][current_y] == 5000:
        global_matrix[current_x][current_y] = current_length
    elif global_matrix[current_x][current_y] > current_length:
        global_matrix[current_x][current_y] = current_length
    elif global_matrix[current_x][current_y] < current_length:
        return

    # go all four steps
    # go left
    if current_x > 0:
        if room[current_x - 1][current_y] != -1:
            generate_solution_part_2(room, current_x - 1, current_y, current_length + 1)

    # go right
    if current_x < len(matrix) - 1:
        if room[current_x + 1][current_y] != -1:
            generate_solution_part_2(room, current_x + 1, current_y, current_length + 1)
    # go down
    if current_y < len(matrix) - 1:
        if room[current_x][current_y + 1] != -1:
            generate_solution_part_2(room, current_x, current_y + 1, current_length + 1)

    # go up
    if current_y > 0:
        if room[current_x][current_y - 1] != -1:
            generate_solution_part_2(room, current_x, current_y - 1, current_length + 1)



max_length = 1000
file1 = open('puzzle13.txt', 'r')
Lines = file1.readlines()
fav_number = 0

count = 0

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    fav_number = int(input_line)

matrix = generate_room(100, fav_number, 0, 1)
print_room(matrix)
result = generate_solution_part_1(matrix, 1, 1, 39, 31, 0, 1000)
print("TASK 1 - min steps = {}".format(result))

matrix = generate_room(100, fav_number, -1, 5000)
global_matrix = generate_room(100, fav_number, -1, 5000)
generate_solution_part_2(matrix, 1, 1, 0 )
print_room(global_matrix)

count_reached_fields = 0
for row in global_matrix:
    for entry in row:
        if entry != -1 and entry != 5000:
            count_reached_fields += 1
print("TASK 2 - reached fields: {}".format(count_reached_fields))
