
file1 = open('puzzle03.txt', 'r')
Lines = file1.readlines()

count = 0
number_list = []
possible_triangles = 0
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    split_string = input_line.split(" ")
    number_array = []
    for entry in split_string:
        if entry.isdecimal():
            number_array.append(entry)
    if int(number_array[0]) + int(number_array[1]) > int(number_array[2]):
        if int(number_array[0]) + int(number_array[2]) > int(number_array[1]):
            if int(number_array[1]) + int(number_array[2]) > int(number_array[0]):
                possible_triangles += 1
    number_list.append(number_array)
print(number_list)
possible_triangles_part_2 = 0
for i in range(len(number_list))[::3]:
    for j in range(3):
        if int(number_list[i][j]) + int(number_list[i + 1][j]) > int(number_list[i + 2][j]):
            if int(number_list[i][j]) + int(number_list[i + 2][j]) > int(number_list[i + 1][j]):
                if int(number_list[i + 1 ][j]) + int(number_list[i + 2][j]) > int(number_list[i][j]):
                    possible_triangles_part_2 +=1

print("TASK 1 - Number of possible triangles: {}".format(possible_triangles))

print("TASK 2 - Number of possible triangles: {}".format(possible_triangles_part_2))