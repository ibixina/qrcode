

def print_qrcode(grid):
    for row in grid:
        print("".join("█" if cell else " " for cell in row))


def generate_qrcode(text):
    pass
