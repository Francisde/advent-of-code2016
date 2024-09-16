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

number_of_elves = 3012210
start_list = []
for i in range(1, number_of_elves + 1, 1):
    start_list.append(Elv(i, 1))

while len(start_list) > 1:
    new_list = []
    print("new round")
    print(start_list)
    for elv_index in range(len(start_list)):
        if start_list[elv_index].presents == 0:
            print("skip elv: {}".format(start_list[elv_index].id))
            continue
        elif elv_index != len(start_list) -1:
            start_list[elv_index].add_presents(start_list[elv_index + 1].presents)
            start_list[elv_index + 1].presents = 0
            print("elv {} takes all presents from elv {}".format(start_list[elv_index].id, start_list[elv_index + 1].id))
        else:
            start_list[elv_index].add_presents(start_list[0].presents)
            print("elv {} takes all presents from elv {}".format(start_list[elv_index].id, start_list[0].id))
            start_list[0].presents = 0
    print("generate new list")
    for elv in start_list:

        if elv.presents > 0:
            print(elv.id)
            new_list.append(elv)
    start_list = new_list


print("TASK 1 - winning elv: {}".format(start_list[0].id))

print("TASK 2 - ")
