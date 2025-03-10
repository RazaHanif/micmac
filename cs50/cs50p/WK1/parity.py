# is it even or odd
def main():
    n = int(input("What is your number "))
    if isEven(n):
        print("Even")
    else:
        print("Odd")

def isEven(num):
    # return True if num % 2 == 0 else False
    return num % 2 == 0

main()