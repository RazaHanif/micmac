def main():
    h = int(input("height: "))
    w = int(input("width: "))
    printBlock(h,w)
    print()
    printSquare(h)

def printBlock(height, width):
    for _ in range(height):
        print("#" * width)

def printSquare(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()