import sys

if len(sys.argv) == 2:
    print(f"Hello, {sys.argv[1]}")
    sys.exit(1)
else:
    print("Hello, world")
    sys.exit(0)
    # echo $? in terminal to check exit status


# from sys import argv
# then can do just argv instead of sys.argv


# for i in list[1:]. -- goes from 1 to the end of the list