import hashlib

file1 = open('puzzle05.txt', 'r')
Lines = file1.readlines()

count = 0
index = 0
door_id = ""
password = ""

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    door_id = input_line

while len(password) < 8:
    hash = hashlib.md5("{}{}".format(door_id, index).encode('utf-8')).hexdigest()
    # print(hash)
    if hash.startswith("00000"):
        password += hash[5:6]
    index += 1

index = 0
password_door2 = "????????"
while "?" in password_door2:
    hash = hashlib.md5("{}{}".format(door_id, index).encode('utf-8')).hexdigest()
    # print(hash)
    if hash.startswith("00000"):
        position = hash[5:6]
        if position in "01234567":
            int_position = int(position)
            if password_door2[int_position] == "?":
                password_door2 = password_door2[:int_position] + hash[6:7] + password_door2[int_position + 1:]
                print(password_door2)

    index += 1


print("TASK 1 - password: {}".format(password))

print("TASK 1 - password: {}".format(password_door2))