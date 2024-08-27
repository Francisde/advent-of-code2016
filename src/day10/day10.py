
class Bot:
    def __init__(self, number):
        self.number= number
        self.chips = []

    def set_chip(self, chip):
        if len(self.chips) < 2 and chip not in self.chips:
            self.chips.append(chip)
            return True
        return False

    def provide_chips(self):
        return len(self.chips) == 2

    def get_lower_chip(self):
        if self.chips[0] < self.chips[1]:
            return self.chips[0]
        else:
            return self.chips[1]

    def get_higher_chip(self):
        if self.chips[0] < self.chips[1]:
            return self.chips[1]
        else:
            return self.chips[0]



file1 = open('puzzle10.txt', 'r')
Lines = file1.readlines()

count = 0
part1 = False
bots = []
outputs = [None for i in range(500)]
for i in range(500):
    bots.append(Bot(i))
instructions = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    instructions.append(input_line)


while True:
    finish = False
    if part1:
        for bot in bots:
            if bot.provide_chips():
                if 61 in bot.chips and 17 in bot.chips:
                    print("Bot {}, is responsible for comparing 5 and 2".format(bot.number))
                    finish = True
    else:
        if outputs[0] is not None and outputs[1] is not None and outputs[2] is not None:
            finish = True
    if finish:
        break
    for instruction in instructions:
        if instruction.startswith("value "):
            split_list = instruction.split(" ")
            value = int(split_list[1])
            bot_number = int(split_list[5])
            bots[bot_number].set_chip(value)
        elif instruction.startswith("bot "):
            split_list = instruction.split(" ")
            bot_1_number = int(split_list[1])
            if bots[bot_1_number].provide_chips():
                low_output = int(split_list[6])
                high_output = int(split_list[11])
                if split_list[5] == "output":
                    outputs[low_output] =bots[bot_1_number].get_lower_chip()
                else:
                    bots[low_output].set_chip(bots[bot_1_number].get_lower_chip())
                if split_list[11] == "output":
                    outputs[high_output] =bots[bot_1_number].get_higher_chip()
                else:
                    bots[high_output].set_chip(bots[bot_1_number].get_higher_chip())
        else:
            print("else")

print(outputs)

print("TASK 1 - ")

print("TASK 2 - ")
