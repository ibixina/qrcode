import math
"""
version H
mode indicator: first 4 bits, 
character count indicator
message
terminator: 4 0s or less to reach the capacity
"""
def mapletFFGenerator(n):
    field = [
             [0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 1, 0, 0, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 1, 0, 1],]

    mapping = {}

    for i in range(9):
        str_key = "".join(str(i) for i in field[i])
        mapping[str_key] = i

    l_8 = field[-1]

    if n > 9:
        for index in range(9, n):
            l = field[-1]
            # shift to the right
            new_l = l[1:] + [0]
            # if l[0] was 1, then add l_8
            if l[0] == 1:
                new_l = [i + j for i, j in zip(l_8, new_l)]
            new_l = [i % 2 for i in new_l]
            field.append(new_l)
            str_key = "".join(str(i) for i in new_l)
            mapping[str_key] = index

    for key, value in mapping.items():
        print(key, value)

    return mapping




field_mapping = mapletFFGenerator(255)

def print_qrcode(grid):
    for row in grid:
        print("".join("█" if cell else " " for cell in row))


def generate_qrcode(text):
    capacity_left = 288
    final_bytes = []

    binary_msg = []
    for char in text:
        print(ord(char), end = " ")
        binary_msg += [bin(ord(char))[2:].zfill(8)]
    print()

    mode_indicator = "0100"
    capacity_left -= len(mode_indicator)
    final_bytes.append(mode_indicator)

    character_count = len(text)
    binary_character_count = bin(character_count)[2:].zfill(8)
    capacity_left -= len(binary_character_count)
    final_bytes.append(binary_character_count)

    final_bytes += binary_msg
    capacity_left -= len(binary_msg) * 8

    terminator = "0" * min(capacity_left - len(final_bytes), 4)
    capacity_left -= len(terminator)
    final_bytes.append(terminator)

    if capacity_left > 0:
        mod_8 = capacity_left % 8
        pad_0 = mod_8 * "0"
        if pad_0: final_bytes.append(pad_0)
        capacity_left -= mod_8

    alternate_bytes = ["11101100", "00010001"]
    for i in range(capacity_left // 8):
        final_bytes.append(alternate_bytes[i % 2])



    print(final_bytes)

    joined = "".join(final_bytes)

    bytes_rearranged = []
    for i in range(0, len(joined), 8):
        print(joined[i:i+8], end = " ")
        bytes_rearranged.append(joined[i:i+8])
    print()


    for byte in bytes_rearranged:
        print(field_mapping[byte], end = " ")
    print()
    






# generate_qrcode("https://atcm.mathandtech.org/")

def gf256_generator(n):
    poly = 0b100011011
    state = 1
    mapping = {}
    for i in range(n):
        mapping[state] = i
        state <<= 1
        if state & 0x100:  # if overflow beyond 8 bits
            state ^= poly
    return mapping

field_mapping = gf256_generator(256)

for key, value in field_mapping.items():
    print(key, value)
