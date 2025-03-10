from emoji import emojize

def main ():
    print("Output:", emojize(input("Input: "), language='alias'))

if __name__ == "__main__":
    main()