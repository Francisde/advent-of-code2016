import hashlib

def generate_keys_part_1(salt):
    index = 0
    keys = []
    related_index = []
    while len(keys) < 64:

        value = "{}{}".format(salt, index)
        hash = hashlib.md5(value.encode('utf-8')).hexdigest()
        # print(hash)
        result = is_key(salt, index)
        if result:
            print("found key {} at index: {}".format(len(keys) + 1, index))
            related_index.append(index)
            keys.append(hash)
        index += 1
    return related_index

def generate_keys_part_2(salt):
    index = 0
    keys = []
    related_index = []
    while len(keys) < 64:
        if index % 100 == 0:
            print("current index {}".format(index))
    # while index < 5:

        value = "{}{}".format(salt, index)
        hash = hashlib.md5(value.encode('utf-8')).hexdigest()
        inner_index = 0
        final_hash = ""
        if hash in final_hash_dict:
            final_hash = final_hash_dict[hash]
        else:
            final_hash = hash
            while inner_index < 2016:
                final_hash = hashlib.md5(final_hash.encode('utf-8')).hexdigest()
                inner_index += 1
            final_hash_dict[hash] = final_hash

        # print(final_hash)
        result = is_key_part_2(salt, index)
        if result:
            print("found key {} at index: {}".format(len(keys) + 1, index))
            related_index.append(index)
            keys.append(hash)
        index += 1
    return related_index

final_hash_dict = dict()

def is_key(salt, index):
    value = "{}{}".format(salt, index)
    hash = hashlib.md5(value.encode('utf-8')).hexdigest()
    first_repeading_letter = ''
    for i in range(len(hash) - 2):
        if hash[i] == hash[i+1] == hash[i+2]:
            first_repeading_letter = hash[i]
            break
    if first_repeading_letter == '':
        return False
    else:
        new_index = index + 1
        muster = "{}{}{}{}{}".format(first_repeading_letter, first_repeading_letter, first_repeading_letter, first_repeading_letter, first_repeading_letter)
        while new_index <= index + 1000:
            value = "{}{}".format(salt, new_index)
            hash = hashlib.md5(value.encode('utf-8')).hexdigest()
            if muster in hash:
                return True
            new_index += 1
        return False

def is_key_part_2(salt, index):
    value = "{}{}".format(salt, index)
    hash = hashlib.md5(value.encode('utf-8')).hexdigest()
    inner_index = 0
    final_hash = hash
    while inner_index < 2016:
        final_hash = hashlib.md5(final_hash.encode('utf-8')).hexdigest()
        inner_index += 1
    first_repeading_letter = ''
    for i in range(len(final_hash) - 2):
        if final_hash[i] == final_hash[i+1] == final_hash[i+2]:
            first_repeading_letter = final_hash[i]
            break
    if first_repeading_letter == '':
        return False
    else:
        new_index = index + 1
        muster = "{}{}{}{}{}".format(first_repeading_letter, first_repeading_letter, first_repeading_letter, first_repeading_letter, first_repeading_letter)
        while new_index <= index + 1000:
            value = "{}{}".format(salt, new_index)
            hash = hashlib.md5(value.encode('utf-8')).hexdigest()
            inner_index = 0
            final_hash = ""
            if hash in final_hash_dict:
                final_hash = final_hash_dict[hash]
            else:
                final_hash = hash
                while inner_index < 2016:
                    final_hash = hashlib.md5(final_hash.encode('utf-8')).hexdigest()
                    inner_index += 1
                final_hash_dict[hash] = final_hash
            if muster in final_hash:
                return True
            new_index += 1
        return False


file1 = open('puzzle14.txt', 'r')
Lines = file1.readlines()

count = 0
salt = ""

for line in Lines:
    input_line= line.strip()
    print("Line {}: {}".format(count, input_line))
    count += 1
    salt = input_line

result_part_1 = generate_keys_part_1(salt)
print("TASK 1 - last index = {}".format(result_part_1[63]))

result_part_2 = generate_keys_part_2(salt)

print("TASK 2 - last index = {}".format(result_part_2[63]))
