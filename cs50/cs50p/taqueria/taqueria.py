def main():

    items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0

    while True:

        try:
            type = input("Item: ").lower().title()
        except EOFError:
            print()
            break
        else:
            if type in items:
                total += items[type]
                print("$%.2f" % total, sep="")
            else:
                pass

main()
