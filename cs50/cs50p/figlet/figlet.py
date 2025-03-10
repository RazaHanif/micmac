from pyfiglet import Figlet
import sys
import random

def main ():
    msg = "Invalid Usage"

    if len(sys.argv) == 1:
        friglet_std()
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-f" or sys.argv[1] == "--font":
            friglet_custom(sys.argv[2])
        else:
            sys.exit(msg)
    else:
        sys.exit(msg)

def friglet_std():
    phrase = Figlet()
    names = phrase.getFonts()
    num = random.randint(0, len(names))
    phrase.setFont(font=names[num])
    print("Output:\n" + phrase.renderText(input("Input: ")))

def friglet_custom(string):
    phrase = Figlet()
    names = phrase.getFonts()
    if string in names:
        phrase.setFont(font=string)
        print("Output:\n" + phrase.renderText(input("Input: ")))
    else:
        sys.exit("Invalid Font Name")


if __name__ == "__main__":
    main()