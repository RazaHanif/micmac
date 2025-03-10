import cs50


def main():
    # Get input from user
    while True:
        dollars = cs50.get_float("Change Owed: ")
        dollars = dollars * 100
        if dollars > 0:
            break

    coins = 0

    # Get number of quarters
    quarter = quarters(dollars)
    dollars -= quarter * 25
    coins += quarter

    # Get number of dimes
    dime = dimes(dollars)
    dollars -= dime * 10
    coins += dime

    # Get number of nickels
    nickel = nickels(dollars)
    dollars -= nickel * 5
    coins += nickel

    # Get number of pennies
    penny = pennies(dollars)
    dollars -= penny * 1
    coins += penny

    print(coins)


def quarters(num):
    count = 0
    while num >= 25:
        num -= 25
        count += 1
    # print("25:",count)
    return count


def dimes(num):
    count = 0
    while num >= 10:
        num -= 10
        count += 1
    # print("10:",count)
    return count


def nickels(num):
    count = 0
    while num >= 5:
        num -= 5
        count += 1
    # print("5:",count)
    return count


def pennies(num):
    count = 0
    while num >= 1:
        num -= 1
        count += 1
    # print("1:",count)
    return count


main()
