
file1 = open('test.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1


print("TASK 1 - ")

print("TASK 2 - ")
