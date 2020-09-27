from cs50 import get_int


def main():
    height = get_height()
    for row in range(height):
        for space in range(height - row - 1):
            print(" ", end="")
        for column in range(row + 1):
            print("#", end="")
        for space1 in range(2):
            print(" ", end="")
        for column in range(row + 1):
            print("#", end="")
        print()


def get_height():
    while True:
        n = get_int("Height: ")
        if n >= 1 and n <= 8:
            break
    return n
    
    
main()