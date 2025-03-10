def main():
    while True:
        n = int(input("n? "))
        if n > 0:
            break
    i = 0

    while i < n:
        print("meow")
        i += 1

    print(" ")

    for _ in range(n):
        print("meow")

    print(" ")

    print("meow \n" * n, end="")

main()

