import copy
import itertools
import sys
sys.setrecursionlimit(10000)

file1 = open('puzzle24.txt', 'r')
Lines = file1.readlines()

def print_map(input_map):
    for row in input_map:
        print(row)
    print()

def solve_part_1_and_2(input_field, part2):
    points_of_interest = []
    min_distances = dict()
    for row in input_field:
        for character in row:
            if character != "#" and character != ".":
                points_of_interest.append(character)
    points_of_interest.sort()
    print(points_of_interest)
    steps = 0
    for poi in points_of_interest:
        field_copy = copy.deepcopy(input_field)
        prepare_fild(field_copy, poi)
        found_shortest_path(field_copy)
        for other_poi in points_of_interest:
            if poi != other_poi:
                if "{}->{}".format(poi, other_poi) not in min_distances.keys():
                    position = get_position(input_field, other_poi)
                    length = field_copy[position[1]][position[0]]
                    min_distances["{}->{}".format(poi, other_poi)] = length
                    min_distances["{}->{}".format(other_poi, poi)] = length
                    print("{}->{}, distance: {}".format(poi, other_poi, min_distances))
                    steps += length
    print(min_distances)

    # solve tsp brute force
    paths = list(itertools.permutations(points_of_interest))
    print("number of paths: {}".format(len(paths)))

    for path in paths:
        if path[0] != '0':
            continue
        path_length = 0
        for i in range(len(path) - 1):
            path_length += min_distances["{}->{}".format(path[i], path[i + 1])]
        if part2:
            path_length += min_distances["{}->{}".format(path[len(path) - 1], 0)]
        # print("path: {},  length: {}".format(path, path_length))
        steps = min(steps, path_length)
    return steps

def get_position(input_field, poi):
    for y in range(len(input_field)):
        for x in range(len(input_field[y])):
            if input_field[y][x] == poi:
                return (x, y)


def found_shortest_path(input_field):
    changes = True
    while changes:
        changes = False
        for i in range(len(input_field)):
            for j in range(len(input_field[i])):
                if input_field[i][j] == '#':
                    pass
                else:
                    up = 9999
                    down = 9999
                    left = 9999
                    right = 9999
                    if input_field[i - 1][j] != '#':
                        up = input_field[i - 1][j] + 1
                    if input_field[i + 1][j] != '#':
                        down = input_field[i + 1][j] + 1
                    if input_field[i][j - 1] != '#':
                        left = input_field[i][j - 1] + 1
                    if input_field[i][j + 1] != '#':
                        right = input_field[i][j + 1] + 1
                    min_value = min(up, down, right, left)
                    if min_value < input_field[i][j]:
                        input_field[i][j] = min_value
                        changes = True

def prepare_fild(input_field, search_character):
    for i in range(len(input_field)):
        for j in range(len(input_field[i])):
            if input_field[i][j] == '#':
                pass
            elif input_field[i][j] == search_character:
                input_field[i][j] = 0
            else:
                input_field[i][j] = 9999
count = 0

field = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    row = []
    for character in input_line:
        row.append(character)
    field.append(row)
    count += 1


print_map(field)

solution_part_1 = solve_part_1_and_2(field, False)
solution_part_2 = solve_part_1_and_2(field, True)
print("TASK 1 - solution: {}".format(solution_part_1))

print("TASK 2 - solution: {}".format(solution_part_2))
