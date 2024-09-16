class Node:

    def __init__(self, name, size, used, avail):
        self.name = name
        self.size = size
        self.used = used
        self.avail = avail

def get_count_of_viable_pairs(node_list):
    pairs = 0
    for node1 in node_list:
        for node2 in node_list:
            if node1 != node2 and node1.used != 0:
                if node2.avail >= node1.used:
                    pairs += 1
    return pairs


file1 = open('puzzle22.txt', 'r')
Lines = file1.readlines()

count = 0
nodes = []
for line in Lines:
    input_line= line.strip()
    #print("Line {}: {}".format(count, input_line))

    if input_line.startswith("/dev/"):
        while True:
            if "  " in input_line:
                input_line = input_line.replace("  ", " ")
            else:
                break
        input_line = input_line.replace("T", "")
        split_string = input_line.split(" ")
        nodes.append(Node(split_string[0], int(split_string[1]), int(split_string[2]), int(split_string[3])))

    count += 1


print("TASK 1 - viable pairs: {}".format(get_count_of_viable_pairs(nodes)))

print("TASK 2 - ")
