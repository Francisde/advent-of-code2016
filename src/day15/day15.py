class Disc:
    def __init__(self, name, positions, current_position):
        self.name = name
        self.positions = positions
        self.current_position = current_position

    def move(self):
        new_position = self.current_position + 1
        self.current_position = new_position % self.positions

    def position_in_x_sec(self, sec):
        return (self.current_position + sec) %self.positions




file1 = open('puzzle15.txt', 'r')
Lines = file1.readlines()

count = 0

disc_list = []



for line in Lines:
    input_line= line.strip()
    input_line = input_line.replace(".", "")
    print("Line {}: {}".format(count, input_line))
    split_string = input_line.split(" ")
    disc_list.append(Disc(split_string[1], int(split_string[3]), int(split_string[11])))
    count += 1

# simulate task
current_sec = 0
while True:
    possible = True
    for i in range(len(disc_list)):
        if disc_list[i].position_in_x_sec(i+1) != 0 and possible:
            possible = False
    if possible:
        print("Press butten at sec: {}".format(current_sec))
        break
    else:
        current_sec += 1
        for disc in disc_list:
            disc.move()


print("TASK 1 - ")

print("TASK 2 - ")
