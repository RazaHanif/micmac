import inflect

# Main method to run program
def main():

    # empty list to store user input
    words = []
    run = inflect.engine()

    # while loop until user breaks out using Ctrl-D
    while True:
        try:
            # Asks user for names
            words.append(input("Name: ").title().rstrip())
        except EOFError:
            # prints out message before breaking out of loop
            print("Adieu, adieu, to " + run.join((words)))
            break

if __name__ == "__main__":
    main()