#same as number, except run until value is correct
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(string):
    while True:
        try:
            return int(input(string))
        except ValueError:
            #print("", end="")
            pass

main()