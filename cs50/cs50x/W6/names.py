import sys

names = ["Bill", "Charlie", "Fred", "George", "Ginny", "Percy", "Ron"]

name = input("Name: ")

if name.strip() in names:
    print("Found")
    sys.exit()
else:
    print("Not Found")
    sys.exit(1)