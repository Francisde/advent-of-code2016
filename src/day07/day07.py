
def check_for_abba(input_string):
    for i in range(len(input_string)-3):
        if input_string[i] == input_string[i + 3] and input_string[i + 1] == input_string[i + 2] and input_string[i] != input_string[i + 1]:
            return True
    else:
        return False

def get_abas(input_string):
    abas = []
    for i in range(len(input_string)-2):
        if input_string[i] == input_string[i + 2] and input_string[i] != input_string[i + 1]:
            abas.append(input_string[i:i+3])
    return abas

def solve_part_one(input_list):
    ip_with_tls_support = 0
    for line in input_list:
        ip_v7_line = line.replace("[", "-")
        ip_v7_line = ip_v7_line.replace("]", "-")
        ip_v7_components = ip_v7_line.split("-")
        hypernet_sequences = False
        found_abba = False
        for component in ip_v7_components:
            abba = check_for_abba(component)
            if abba and not hypernet_sequences:
                found_abba = True
            if abba and hypernet_sequences:
                found_abba = False
                break
            hypernet_sequences = not hypernet_sequences
        if found_abba:
            ip_with_tls_support += 1
    return ip_with_tls_support

def solve_part_two(input_list):
    ip_with_ssl_support = 0
    for line in input_list:
        ip_v7_line = line.replace("[", "-")
        ip_v7_line = ip_v7_line.replace("]", "-")
        ip_v7_components = ip_v7_line.split("-")
        supernet_sequences = []
        hypernet_sequences = []
        hypernet_sequence = False
        for component in ip_v7_components:
            if hypernet_sequence:
                hypernet_sequences.append(component)
            else:
                supernet_sequences.append(component)
            hypernet_sequence = not hypernet_sequence
        list_of_abas = []
        for component in supernet_sequences:
            list_of_abas = list_of_abas + get_abas(component)
        ssl_support = False
        for aba in list_of_abas:
            for component in hypernet_sequences:
                if "{}{}{}".format(aba[1],aba[0], aba[1]) in component:
                    ssl_support = True
        if ssl_support:
            ip_with_ssl_support += 1

    return ip_with_ssl_support




file1 = open('puzzle07.txt', 'r')
Lines = file1.readlines()

count = 0

ip_addresses = []

for line in Lines:
    input_line= line.strip()
    count += 1
    ip_addresses.append(input_line)

print("TASK 1 - How many IPs in your puzzle input support TLS?: {}".format(solve_part_one(ip_addresses)))

print("TASK 2 - How many IPs in your puzzle input support SSL?: {}".format(solve_part_two(ip_addresses)))
