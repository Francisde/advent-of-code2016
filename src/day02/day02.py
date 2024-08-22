
file1 = open('puzzle02.txt', 'r')
Lines = file1.readlines()

count = 0

number_pad = dict()
number_pad["02"] = "1"
number_pad["12"] = "2"
number_pad["22"] = "3"
number_pad["01"] = "4"
number_pad["11"] = "5"
number_pad["21"] = "6"
number_pad["00"] = "7"
number_pad["10"] = "8"
number_pad["20"] = "9"

valid_number_pad = ["20", "11", "21", "31", "02", "12", "22", "32", "42", "13", "23", "33", "24"]
number_pad_part_2 = dict()
number_pad_part_2["24"] = "1"
number_pad_part_2["13"] = "2"
number_pad_part_2["23"] = "3"
number_pad_part_2["33"] = "4"
number_pad_part_2["02"] = "5"
number_pad_part_2["12"] = "6"
number_pad_part_2["22"] = "7"
number_pad_part_2["32"] = "8"
number_pad_part_2["42"] = "9"
number_pad_part_2["11"] = "A"
number_pad_part_2["21"] = "B"
number_pad_part_2["31"] = "C"
number_pad_part_2["20"] = "D"


def decode_line(input_code, x, y):
    for character in input_code:
        if character == "D" and y - 1 >=0:
            y -= 1
        elif character == "U" and y + 1 <=2:
            y += 1
        elif character == "L" and x - 1 >=0:
            x -= 1
        elif character == "R" and x + 1 <=2:
            x += 1
    return [number_pad["{}{}".format(x, y)], x, y]

def decode_line_part2(input_code, x, y):
    for character in input_code:
        if character == "D" and "{}{}".format(x, y - 1) in valid_number_pad:
            y -= 1
        elif character == "U" and "{}{}".format(x, y + 1) in valid_number_pad:
            y += 1
        elif character == "L" and "{}{}".format(x - 1, y ) in valid_number_pad:
            x -= 1
        elif character == "R" and "{}{}".format(x + 1, y) in valid_number_pad:
            x += 1
    return [number_pad_part_2["{}{}".format(x, y)], x, y]


start_x = 1
start_y = 1
start_x_part2 = 1
start_y_part2 = 1
bathroom_code = ""
bathroom_code_part2 = ""

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    result = decode_line(input_line, start_x, start_y)
    print(result)
    bathroom_code += result[0]
    start_x = result[1]
    start_y = result[2]
    result2 = decode_line_part2(input_line, start_x_part2, start_y_part2)
    bathroom_code_part2 += result2[0]
    start_x_part2 = result2[1]
    start_y_part2 = result2[2]
    count += 1


print("TASK 1 - bathroom code: {}".format(bathroom_code))

print("TASK 2 - bathroom code: {}".format(bathroom_code_part2))
