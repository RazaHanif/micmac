import sys
import cowsay

def main():
    if len(sys.argv) == 2:
        cowsay.cow("hello, " + sys.argv[1])
    elif len(sys.argv) == 3:
        cowsay.dragon("Hello, " + sys.argv[1] + " " + sys.argv[2])
    elif len(sys.argv) == 4:
        cowsay.trex("Hello, " + sys.argv[1] + " " + sys.argv[2] + " " + sys.argv[3])
    else:
        print("BRUH")

main()