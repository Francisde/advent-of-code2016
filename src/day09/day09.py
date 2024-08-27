
def expand_string(input_string):
    result = ""
    index = 0
    while index < len(input_string):
        if input_string[index] != "(":
            result += input_string[index]
            index += 1
        else:
            # check if it is a valid marker
            is_marker = False
            marker_end = 0
            marker_index = index
            while marker_index < len(input_string):
                if input_string[marker_index] != ")":
                    marker_index += 1
                else:
                    is_marker = True
                    marker_end = marker_index
                    break
            if is_marker:
                # print("is marker: {}".format(input_string[index+1 :marker_end]))
                params = input_string[index+1 :marker_end].split("x")
                param_a = int(params[0])
                param_b = int(params[1])
                for i in range(param_b):
                    result += input_string[marker_end + 1: marker_end + param_a + 1]
                index = marker_end + param_a + 1

            else:
                result += input_string[index]
                index += 1
    return result


file1 = open('puzzle09.txt', 'r')
Lines = file1.readlines()

count = 0
total_length = 0
total_length_2 = 0
last_total_length = 0

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    expanded_string = expand_string(input_line)

    total_length += len(expanded_string)
    total_length_2 += len(expanded_string)
    while total_length_2 != last_total_length:
        print("loop")
        last_total_length = total_length_2
        expanded_string = expand_string(expanded_string)
        total_length_2 += len(expanded_string)
        print("current length: {}".format(total_length_2))
        print("count of compress instructions: {}".format(expanded_string.count("(")))



print("TASK 1 - Total length of file: {}".format(total_length))

print("TASK 2 - ")
