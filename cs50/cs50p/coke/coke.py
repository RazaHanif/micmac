# vending machine program
# run down value as coins entered, display change at end

def main():
    due = 50
    while True:
        if due > 0:
            print("Amount Due:", due)
            due = pay(due)
        else:
            print("Change Owed:", (due * -1))
            break

def pay(amount):
    coin = int(input("Insert Coin: "))

    if coin == 5 or coin == 10 or coin == 25:
        return amount - coin
    else:
        return amount

main()