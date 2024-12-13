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

def print_grid(node_list):
    current_index = 0
    for node in node_list:
        if "x{}".format(current_index) in node.name:
            print("{}/{}".format(node.used, node.size), end='')
            print(", ", end='')
        else:
            current_index += 1
            print()
            print("{}/{}".format(node.used, node.size), end='')
            print(", ", end='')

def pprint_grid(node_list):
    current_index = 0
    for node in node_list:
        if "x{}".format(current_index) in node.name:
            if node.size > 200:
                print("X".format(node.used, node.size), end='')
                print(" ", end='')
            elif node.used == 0:
                print("0".format(node.used, node.size), end='')
                print(" ", end='')
            else:
                print(".".format(node.used, node.size), end='')
                print(" ", end='')
        else:
            current_index += 1
            print()
            if node.size > 200:
                print("X".format(node.used, node.size), end='')
                print(" ", end='')
            elif node.used == 0:
                print("0".format(node.used, node.size), end='')
                print(" ", end='')
            else:
                print(".".format(node.used, node.size), end='')
                print(" ", end='')

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
pprint_grid(nodes)

print()
print("TASK 1 - viable pairs: {}".format(get_count_of_viable_pairs(nodes)))

print("TASK 2 - sol: 28 - solved it per pen and paper")
