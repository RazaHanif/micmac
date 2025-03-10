def main():
    print("$" + str(value(input("Greeting: "))))


def value(greeting):
    greet = greeting.lower().strip()
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
