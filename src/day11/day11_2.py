from itertools import combinations

class Item:
    def __init__(self, name, floor):
        self.name = name
        self.floor = floor

    def __repr__(self):
        return self.name

def parse_configuration(input_string):
    split_string = input_string.split("-")
    elevator = int(split_string[0])
    items = []
    for i in range(1,len(split_string)):
        items.append(Item(split_string[i].split(".")[0], int(split_string[i].split(".")[1])))
    return (elevator, items)

def generate_all_configurations(elements, floors):
    count = 0
    configuarations = []
    for i in range(floors):
        current_configurations = ["{}".format(i)]
        for element in elements:
            old_configurations = current_configurations
            current_configurations = []
            for j in range(floors):
                for k in range(floors):
                    for old_configuration in old_configurations:
                        current_configurations.append("{}-{}{}.{}-{}{}.{}".format(old_configuration, element, 'G', j, element, 'M', k))
        configuarations = configuarations + current_configurations

    print("{} options".format(len(configuarations)))
    return configuarations

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


def reachable_solution_in_one_step(start_sequence):

    next_step = []

    configuration = parse_configuration(start_sequence)

    elevator = configuration[0]
    items = configuration[1]

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
    return next_step

file1 = open('test.txt', 'r')
Lines = file1.readlines()


count = 0


elements = ['P', 'T', 'K', 'R', 'C', 'E', 'D']
start_sequence = "0-PG.0-PM.1-TG.0-TM.0-KG.0-KM.1-RG.0-RM.0-CG.0-CM.0-EG.0-EM.0-DG.0-DM.0"
stop_sequence = "3-PG.3-PM.3-TG.3-TM.3-KG.3-KM.3-RG.3-RM.3-CG.3-CM.3-EG.3-EM.3-DG.3-DM.3"
# elements = ['H', 'L']
# start_sequence = "0-HG.0-HM.1-LG.0-LM.2"
# stop_sequence = "3-HG.3-HM.3-LG.3-LM.3"
min_dist = {}
seq_validated = {}

confs = generate_all_configurations(elements, 4)
valid_conf = 0
valid_confs= []
for i in range(len(confs)):
    if i % 100000 == 0:
        print(i)
    if configuration_valid(parse_configuration(confs[i])[1]):
        valid_conf += 1
        valid_confs.append(confs[i])
        min_dist[confs[i]] = 100000
        seq_validated[confs[i]] = False

print("valid configs: {}".format(valid_conf))


min_dist[stop_sequence] = 0
while min_dist[start_sequence] == 100000:
    checked = False
    for sequence in valid_confs:
        if min_dist[sequence] != 100000:
            if seq_validated[sequence] == False:
                reachable_sequences = reachable_solution_in_one_step(sequence)
                # print("reachable seq: {}".format(len(reachable_sequences)))
                seq_validated[sequence] = True
                checked = True
                for rech_seq in reachable_sequences:
                    # print(rech_seq)
                    if rech_seq in valid_confs:
                        min_dist[rech_seq] = min(min_dist[rech_seq], min_dist[sequence] + 1)
    print("checked something: {}".format(checked))

print("TASK 1 - min dist: {}".format(min_dist[start_sequence]))

print("TASK 2 - ")
