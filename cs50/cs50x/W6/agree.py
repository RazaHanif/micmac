def main():

    while (True):
        s = input("Do you agree? Y or N :").lower()
        if s == "y":
            print("Agree")
            break
        elif s == "n":
            print("Disagree")
            break
        else:
            print("Invalid Input")


if __name__ == "__main__":
    main()