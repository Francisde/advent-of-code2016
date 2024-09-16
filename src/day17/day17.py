import hashlib

def solve_puzzle_part_1(current_position, passcode, path):
    global global_shortest_path
    global global_longest_path
    if current_position == (3,3):
        if global_shortest_path == -1 or global_shortest_path > len(path):
            global_shortest_path = len(path)
            print(path)
        if global_longest_path < len(path):
            global_longest_path = len(path)
        return
    #if global_shortest_path != -1 and global_shortest_path < len(path):
    #    return
    next_hash = hashlib.md5("{}{}".format(passcode, path).encode('utf-8')).hexdigest()
    #print("current path: {}, next hash: {}".format(path, next_hash))
    open_doors = ['b', 'c', 'd', 'e', 'f']
    # go down
    if next_hash[1] in open_doors and current_position[1] < 3:
        solve_puzzle_part_1((current_position[0], current_position[1] + 1 ), passcode, path + "D")
    # go up
    if next_hash[0] in open_doors and current_position[1] > 0:
        solve_puzzle_part_1((current_position[0], current_position[1] - 1 ), passcode, path + "U")
    # go left
    if next_hash[2] in open_doors and current_position[0] > 0:
        solve_puzzle_part_1((current_position[0] - 1, current_position[1] ), passcode, path + "L")
    #go right
    if next_hash[3] in open_doors and current_position[0] < 3:
        solve_puzzle_part_1((current_position[0] + 1, current_position[1] ), passcode, path + "R")
    return


global_shortest_path = -1
global_longest_path = 0

file1 = open('test.txt', 'r')
Lines = file1.readlines()

dungeon = [[0 for i in range(4)] for j in range(4)]
current_position = (0,0)
count = 0
passcode = ""
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    passcode = input_line

solve_puzzle_part_1(current_position, passcode, "")

print("TASK 1 - shortest path through the dungeon: {}".format(global_shortest_path))

print("TASK 2 - longest path: {}".format(global_longest_path))
