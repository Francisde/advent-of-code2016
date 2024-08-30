
def init_data(input_data):
    b = input_data[::-1]
    b = b.replace("1", "2")
    b = b.replace("0", "1")
    b = b.replace("2", "0")
    return "{}{}{}".format(input_data, "0", b)

def generate_checksum(input_data):
    checksum = ""
    for i in range(0, len(input_data), 2):
        if input_data[i:i+2] == "11" or input_data[i:i+2] == "00":
            checksum += "1"
        else:
            checksum += "0"
    return checksum

def solve_puzzle(length_needed, input_sequence):
    new_sequence = input_sequence
    while len(new_sequence) < length_needed:
        new_sequence = init_data(new_sequence)

    new_sequence = new_sequence[0:length_needed]
    check_sum = new_sequence
    while len(check_sum) % 2 == 0:
        check_sum = generate_checksum(check_sum)
    return check_sum

file1 = open('puzzle16.txt', 'r')
Lines = file1.readlines()

count = 0

start_sequence = ""

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    start_sequence = input_line
    count += 1



print("TASK 1 - checksum: {}".format(solve_puzzle(272, start_sequence)))

print("TASK 2 - checksum: {}".format(solve_puzzle(35651584, start_sequence)))
