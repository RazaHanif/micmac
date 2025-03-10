def main():
    num = int(input("Num: "))
    meow(num)

def meow(n):
    for _ in range(n):
        print("meow")


if __name__ == "__main__":
    main()