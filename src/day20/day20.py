
def find_smallest_open_ip(blacklist):
    ip = 0
    allowed_ips = 0
    while ip < 4294967296:
        print(ip)
        blacklisted_ip = False
        for entry in blacklist:
            if ip >= entry[0] and ip > entry[1]:
                pass
            if ip >= entry[0] and ip <= entry[1]:
                ip = entry[1] + 1
                blacklisted_ip = True
        if not blacklisted_ip:
            return ip
    return ip

def number_of_allowed_ips(blacklist):
    ip = 0
    allowed_ips = 0
    while ip < 4294967296:
        print(ip)
        blacklisted_ip = False
        for entry in blacklist:
            if ip >= entry[0] and ip > entry[1]:
                pass
            if ip >= entry[0] and ip <= entry[1]:
                ip = entry[1] + 1
                blacklisted_ip = True
        if not blacklisted_ip:
            allowed_ips += 1
            ip += 1
    return allowed_ips

file1 = open('puzzle20.txt', 'r')
Lines = file1.readlines()

count = 0
blacklist = []

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    split_string = input_line.split("-")
    blacklist.append((int(split_string[0]), int(split_string[1])))

solution_1 = find_smallest_open_ip(blacklist)
solution_2 = number_of_allowed_ips(blacklist)
print("TASK 1 - smallest possible ip not blacklisted: {}".format(solution_1))

print("TASK 2 - number of allowed ips: {}".format(solution_2))
