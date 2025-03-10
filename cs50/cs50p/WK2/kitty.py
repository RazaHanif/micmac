def main():
    number = getNumber()
    meow(number)

def getNumber():
    while True:
        n = int(input("Enter Number: "))

        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()