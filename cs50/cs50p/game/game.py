import random
import sys

def main():

    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            try:
                num = random.randint(1, level)
            except ValueError:
                pass
            else:
                break

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            pass
        else:
            if guess <= 0:
                pass
            elif guess > num:
                print("Too large!")
            elif guess < num:
                print("Too small!")
            else:
                sys.exit("Just right!")

if __name__ == "__main__":
    main()
