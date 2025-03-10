import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        ans = x + y
        count = 0

        while count < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                count += 1
            else:
                if guess == ans:
                    score += 1
                    break
                else:
                    print("EEE")
                    count += 1
        if count == 3:
            print(f"{x} + {y} = {ans}")

    print(f"Score: {score}")





def get_level():
    while True:
        try:
            num = int(input("Level: "))
        except ValueError:
            pass
        else:
            if num == 1 or num == 2 or num == 3:
                return num
            else:
                pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")

if __name__ == "__main__":
    main()

    
