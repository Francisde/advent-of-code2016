
file1 = open('puzzle01.txt', 'r')
Lines = file1.readlines()

count = 0

instructions = []

for line in Lines:
    input_line= line.strip()
    input_line = input_line.replace(",", "")
    count += 1
    instructions = input_line.split(" ")

location_visited_twice = (0,0)
locations_visited = []
found_part_2_solution = False
print(instructions)
start_x = 0
start_y = 0
facing = "N"

def goSteps(current_x, current_y, x, y, steps):
    global found_part_2_solution
    global location_visited_twice
    global locations_visited
    if x != 0:
        for i in range(steps):
            if x > 0:
                current_x +=1
            else:
                current_x -=1
            current_location = (current_x, current_y)
            if current_location in locations_visited and not found_part_2_solution:
                location_visited_twice = current_location
                found_part_2_solution = True
            else:
                locations_visited.append(current_location)
    else:
        for i in range(steps):
            if y > 0:
                current_y +=1
            else:
                current_y -=1
            current_location = (current_x, current_y)
            if current_location in locations_visited and not found_part_2_solution:
                location_visited_twice = current_location
                found_part_2_solution = True
            else:
                locations_visited.append(current_location)


for instruction in instructions:

    direction = instruction[0:1]
    print(instruction)
    print(instruction[1:])
    steps = int(instruction[1:])

    if facing == "N":
        if direction == "R":
            facing = "E"
            goSteps(start_x, start_y, steps, 0, steps)
            start_x += steps
        else:
            facing = "W"
            goSteps(start_x, start_y, 0 -steps, 0, steps)
            start_x -= steps
        continue
    if facing == "E":
        if direction == "R":
            facing = "S"
            goSteps(start_x, start_y, 0, 0 -steps, steps)
            start_y -= steps
        else:
            facing = "N"
            goSteps(start_x, start_y, 0, steps, steps)
            start_y += steps
        continue
    if facing == "W":
        if direction == "R":
            facing = "N"
            goSteps(start_x, start_y, 0, steps, steps)
            start_y += steps
        else:
            facing = "S"
            goSteps(start_x, start_y, 0, 0-steps, steps)
            start_y -= steps
        continue
    if facing == "S":
        if direction == "R":
            facing = "W"
            goSteps(start_x, start_y, 0-steps, 0, steps)
            start_x -= steps
        else:
            facing = "E"
            goSteps(start_x, start_y, steps, 0, steps)
            start_x += steps
        continue

distance = abs(0 - start_x) + abs(0 - start_y)

print("final position: x= {}, y= {}".format(start_x, start_y))
print("TASK 1 - Distance: {}".format(distance))

print("first location visited twice position: x= {}, y= {}".format(location_visited_twice[0], location_visited_twice[1]))
distance_2 = abs(0 - location_visited_twice[0]) + abs(0 - location_visited_twice[1])
print(locations_visited)
print("TASK 2 - Distance: {}".format(distance_2))