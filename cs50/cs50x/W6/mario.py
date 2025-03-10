def main():
    print_column(get_size())
    print_row(get_size())
    print_block(get_size())
    print_stair(get_size())


def get_size():
    while True:
        try:
            n = int(input("Size: "))
        except (ValueError):
            pass
        else:
            if n > 0:
                return n


def print_column(num):
    for _ in range(num):
        print("#")

def print_row(num):
    print("#" * num)


def print_block(num):
    for _ in range(num):
        print_row(num)


def print_stair(num):
    for i in range(num):
        print_row(i+1)


if __name__ == "__main__":
    main()