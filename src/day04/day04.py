
file1 = open('puzzle04.txt', 'r')
Lines = file1.readlines()

def encrypt_room_name(room_name, id):
    result = ""
    for letter in room_name:
        if letter == "-":
            result += " "
        else:
            letter_int = ord(letter)
            letter_int -= 97
            letter_int += id
            letter_int = letter_int % 26
            letter_int += 97
            result += chr(letter_int)
    return result

def get_most_common_letters(encrypted_name):
    letter_counter = dict()
    for word in encrypted_name:
        for character in word:
            if character in letter_counter:
                letter_counter[character] = letter_counter[character] + 1
            else:
                letter_counter[character] = 1
    result = ""
    old_max = 100
    while len(result) < 5:
        current_max = 0
        for letter in letter_counter:
            if letter_counter[letter] < old_max:
                current_max = max(current_max, letter_counter[letter])
        result_letters = []
        for letter in letter_counter:
            if letter_counter[letter] == current_max:
                result_letters.append(letter)

        result_letters.sort()

        for letter in result_letters:
            if len(result) < 5:
                result += letter
        old_max = current_max

    return result

count = 0
id_sum = 0
north_pole_object_id = 0
for line in Lines:
    input_line= line.strip()

    count += 1
    input_line = input_line.replace("]", "")
    split_string = input_line.split("-")
    calculated_checksum = get_most_common_letters(split_string[0:-1])
    checksum = split_string[-1]
    room_id = int(checksum.split("[")[0])
    if checksum.split("[")[1] == calculated_checksum:
        id_sum += room_id
        print("Line {}: {} - real room".format(count, input_line))
        room_name = ""
        for i in split_string[0:-1]:
            room_name += i
            room_name += "-"
        encryped_room_name = encrypt_room_name(room_name[0:-1], room_id)
        print("encrypted room name: {}".format(encryped_room_name))
        if "northpole" in encryped_room_name:
            north_pole_object_id = room_id

    else:
        print("Line {}: {} - not real room".format(count, input_line))



print("TASK 1 - Sum of real room IDs: {}".format(id_sum))

print("TASK 2 - Nort pole object room: {}".format(north_pole_object_id))
