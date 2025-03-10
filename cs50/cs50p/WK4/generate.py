# import random // gives you all fucnitons from random, must then use function as random.____()
# instead can do specifilly the funciton you want to use and then use function as ____()
from random import choice
from random import randint
from random import shuffle

def main():

    coin = choice(["heads", "tails"])
    print(coin)

    num = randint(1, 10)
    print(num)

    cards = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
    shuffle(cards)
    for card in cards:
        print(card)


main()