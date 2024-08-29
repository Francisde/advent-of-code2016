from itertools import combinations

class Item:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __repr__(self):
        return self.name


file1 = open('puzzle11.txt', 'r')
Lines = file1.readlines()

count = 0
already_visited_configurations = []

def breath_search_solution(start_sequence):
    current_step = [start_sequence]


    step_counter = 0
    found_solution = False
    while not found_solution:
        next_step = []
        print("step: {}, possible solutions: {}".format(step_counter, len(current_step)))
        for solution in current_step:
            if solution in already_visited_configurations:
                continue
            else:
                already_visited_configurations.append(solution)

            configuration = parse_configuration(solution)

            elevator = configuration[0]
            items = configuration[1]
            if not configuration_valid(items):
                continue
            finish = True
            for item in items:
                if item.floor != 3:
                    finish = False
            if finish:
                found_solution = True
                break

            if elevator == 0:
                new_elevator = 1
                moveable_items = []
                for item in items:
                    if item.floor == elevator:
                        moveable_items.append(item)
                possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
                for entry in possible_movements:
                    next_step.append(generate_new_config(new_elevator, entry, items))

            elif elevator == 3:
                new_elevator = 2
                moveable_items = []
                for item in items:
                    if item.floor == elevator:
                        moveable_items.append(item)
                possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
                for entry in possible_movements:
                    next_step.append(generate_new_config(new_elevator, entry, items))
            else:
                new_elevator = elevator + 1
                moveable_items = []
                for item in items:
                    if item.floor == elevator:
                        moveable_items.append(item)
                possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
                for entry in possible_movements:
                    next_step.append(generate_new_config(new_elevator, entry, items))

                new_elevator = elevator - 1
                moveable_items = []
                for item in items:
                    if item.floor == elevator:
                        moveable_items.append(item)
                possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
                for entry in possible_movements:
                    next_step.append(generate_new_config(new_elevator, entry, items))
        step_counter += 1
        current_step = next_step



def generate_new_config(new_elevator, moving_items, items):
    result = "{}".format(new_elevator)
    moving_set = set(moving_items)
    item_set = set(items).difference(moving_set)
    for item in moving_set:
        result += "-{}.{}".format(item.name, new_elevator)
    for item in item_set:
        result += "-{}.{}".format(item.name, item.floor)

    return result


def parse_configuration(input_string):
    split_string = input_string.split("-")
    elevator = int(split_string[0])
    items = []
    for i in range(1,len(split_string)):
        items.append(Item(split_string[i].split(".")[0], int(split_string[i].split(".")[1])))
    return (elevator, items)

def configuration_valid(item_list):
    valid_config = True
    for item in item_list:
        if "M" in item.name:
            item_on_same_floor_as_gen = False
            for item_g in item_list:
                if item_g.name == "{}G".format(item.name[0:1]):
                    if item_g.floor == item.floor:
                        item_on_same_floor_as_gen = True
            if item_on_same_floor_as_gen:
                continue
            else:
                for item_g in item_list:
                    if "G" in item_g.name:
                        if item_g.floor == item.floor:
                            valid_config = False
                            break
    return valid_config



start_config = ""
for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    start_config = input_line

breath_search_solution(start_config)

print("TASK 1 - ")

print("TASK 2 - ")
