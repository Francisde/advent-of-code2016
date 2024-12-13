import time

class Elv:
    def __init__(self, id, presents):
        self.id = id
        self.presents = presents

    def sub_presents(self, number):
        self.presents -= number

    def add_presents(self, number):
        self.presents += number
    def __repr__(self):
        return str(self.id)

def solve_part_one(number_of_elves):
    start_list = []
    for i in range(1, number_of_elves + 1, 1):
        start_list.append(Elv(i, 1))

    while len(start_list) > 1:
        new_list = []
        # print("new round")
        # print(start_list)
        for elv_index in range(len(start_list)):
            if start_list[elv_index].presents == 0:
                # print("skip elv: {}".format(start_list[elv_index].id))
                continue
            elif elv_index != len(start_list) -1:
                start_list[elv_index].add_presents(start_list[elv_index + 1].presents)
                start_list[elv_index + 1].presents = 0
                # print("elv {} takes all presents from elv {}".format(start_list[elv_index].id, start_list[elv_index + 1].id))
            else:
                start_list[elv_index].add_presents(start_list[0].presents)
                # print("elv {} takes all presents from elv {}".format(start_list[elv_index].id, start_list[0].id))
                start_list[0].presents = 0
        # print("generate new list")
        for elv in start_list:

            if elv.presents > 0:
                # print(elv.id)
                new_list.append(elv)
        start_list = new_list
    return start_list[0].id

def solve_part_two(number_of_elves):
    start_time = time.time()
    start_list = []
    elv_dict = dict()
    current_list = []
    # generate all elves
    for i in range(1, number_of_elves + 1, 1):
        elv = Elv(i, 1)
        start_list.append(elv)
        elv_dict["{}".format(i)] = elv
        current_list.append(elv)


    round = 1
    last_index = -1
    while len(start_list) > 1:
        start_time = time.time()

        # generate current_list
        current_list = []
        for elv in start_list:
            if elv.presents > 0:
                current_list.append(elv)
        for elv in current_list:
            if elv.presents == 0:
                continue
            elv_index = -1
            # build circle:
            circle = []
            for circle_elv in start_list:
                if circle_elv.presents > 0:
                    circle.append(circle_elv)
                if circle_elv == elv:
                    elv_index = circle.index(circle_elv)
            if elv_index == -1:
                return -1

            half_index = (int(len(circle) / 2)  + elv_index) % len(circle)
            elv_to_steal_from = circle[half_index]
            # print("elv {} get item from elv {}".format(elv.id , elv_to_steal_from.id))
            start_list.remove(elv_to_steal_from)
            elv_to_steal_from.presents = 0
            # print("elv {} takes all presents from elv {}".format(start_list[elv_index].id, start_list[elv_index + 1].id))

        end_time = time.time()
        print("finish round {} in {}, {} elves to go".format(round, end_time - start_time, len(start_list)))
        round += 1
    print(start_list)
    return start_list[0]


number_of_elves = 3012210

print("TASK 1 - winning elv: {}".format(solve_part_one(number_of_elves)))

print("TASK 2 - winning elv: {}".format(solve_part_two(number_of_elves)))
