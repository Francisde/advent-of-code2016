from itertools import combinations

class Item:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __repr__(self):
        return self.name


def deep_search_solution(start_sequence, steps):
    global max_steps
    global config_cache

    if steps > max_steps:
        return
    if start_sequence == stop_sequence:
        print("Found solution after: {} steps".format(steps))
        max_steps = steps
        return

    configuration = parse_configuration(start_sequence)

    elevator = configuration[0]
    items = configuration[1]
    if not configuration_valid(items):
        return

    if start_sequence in config_cache.keys():
        if config_cache[start_sequence] < steps:
            return
        else:
            config_cache[start_sequence] = steps
    else:
        config_cache[start_sequence] = steps

    if elevator == 0:
        new_elevator = 1
        moveable_items = []
        for item in items:
            if item.floor == elevator:
                moveable_items.append(item)
        possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
        for entry in possible_movements:
            deep_search_solution(generate_new_config(new_elevator, entry, items), steps + 1)

    elif elevator == 3:
        new_elevator = 2
        moveable_items = []
        for item in items:
            if item.floor == elevator:
                moveable_items.append(item)
        possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
        for entry in possible_movements:
            deep_search_solution(generate_new_config(new_elevator, entry, items), steps + 1)
    else:
        new_elevator = elevator + 1
        moveable_items = []
        for item in items:
            if item.floor == elevator:
                moveable_items.append(item)
        possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
        for entry in possible_movements:
            deep_search_solution(generate_new_config(new_elevator, entry, items), steps + 1)

        new_elevator = elevator - 1
        moveable_items = []
        for item in items:
            if item.floor == elevator:
                moveable_items.append(item)
        possible_movements = list(combinations(moveable_items, 1)) + list(combinations(moveable_items, 2))
        for entry in possible_movements:
            deep_search_solution(generate_new_config(new_elevator, entry, items), steps + 1)



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


def generate_new_config(new_elevator, moving_items, items):
    result = "{}".format(new_elevator)
    moving_set = set(moving_items)
    item_set = set(items).difference(moving_set)
    for element in elements:
        for type in ['G', 'M']:
            key_value = "{}{}".format(element, type)
            for item in moving_set:
                if item.name == key_value:
                    result += "-{}.{}".format(item.name, new_elevator)
            for item in item_set:
                if item.name == key_value:
                    result += "-{}.{}".format(item.name, item.floor)
    return result

# Task 1
elements = ['P', 'T', 'K', 'R', 'C']
start_sequence = "0-PG.0-PM.1-TG.0-TM.0-KG.0-KM.1-RG.0-RM.0-CG.0-CM.0"
stop_sequence = "3-PG.3-PM.3-TG.3-TM.3-KG.3-KM.3-RG.3-RM.3-CG.3-CM.3"

# Task 2
# elements = ['P', 'T', 'K', 'R', 'C', 'E', 'D']
# start_sequence = "0-PG.0-PM.1-TG.0-TM.0-KG.0-KM.1-RG.0-RM.0-CG.0-CM.0-EG.0-EM.0-DG.0-DM.0"
# stop_sequence = "3-PG.3-PM.3-TG.3-TM.3-KG.3-KM.3-RG.3-RM.3-CG.3-CM.3-EG.3-EM.3-DG.3-DM.3"

# Test
# elements = ['H', 'L']
# start_sequence = "0-HG.0-HM.1-LG.0-LM.2"
# stop_sequence = "3-HG.3-HM.3-LG.3-LM.3"
max_steps = 10

config_cache = dict()

deep_search_solution(start_sequence, 0)

print("TASK 1 - max_steps = {}".format(max_steps))

print("TASK 2 - ")
