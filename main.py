import math
"""
version H
mode indicator: first 4 bits, 
character count indicator
message
terminator: 4 0s or less to reach the capacity
"""


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
    for i in range(0, len(joined), 8):
        print(joined[i:i+8], end = " ")
    print()
    





generate_qrcode("https://atcm.mathandtech.org/")
