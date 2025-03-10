def main():
    hello()
    first = input("Whats your name? ")
    hello(first)

def hello(name="dummy"):
    print("Hello,", name.strip().title())

main()
