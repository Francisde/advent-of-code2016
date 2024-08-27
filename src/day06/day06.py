
file1 = open('puzzle06.txt', 'r')
Lines = file1.readlines()

count = 0
data_lines = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    data_lines.append(input_line)

error_corrected_message = ""
error_corrected_message2 = ""
for i in range(len(data_lines[0])):

    character_frequency_dict = {}
    for line in data_lines:
        if line[i] in character_frequency_dict:
            character_frequency_dict[line[i]] += 1
        else:
            character_frequency_dict[line[i]] = 1
    max_value = 0
    min_value = 100
    least_common_character = ''
    most_frequent_character = ''
    for character in character_frequency_dict:
        if character_frequency_dict[character] > max_value:
            max_value = character_frequency_dict[character]
            most_frequent_character = character
        if character_frequency_dict[character] < min_value:
            min_value = character_frequency_dict[character]
            least_common_character = character
    error_corrected_message += most_frequent_character
    error_corrected_message2 += least_common_character



print("TASK 1 - error corrected message: {}".format(error_corrected_message))

print("TASK 2 - error corrected message: {}".format(error_corrected_message2))
