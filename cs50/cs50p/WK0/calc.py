def main():
    x = int(input("x :"))
    print("x squared is", square(x))

def square(num):
    # or pow(num, 2)
    return num ** 2

main()