import csv
import sys
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if check_file(sys.argv[1]):
            if is_file(sys.argv[1]):
                print_lines(sys.argv[1])

def check_file(file):
    if str(file).endswith(".csv"):
        return True
    else:
        sys.exit("Not a CSV file")

def is_file(file):
    try:
        text = open(file)
        text.close()
        return True
    except FileNotFoundError:
        sys.exit("File does not exist")

def print_lines(file):
    table = []
    count = 0

    with open(file) as reader:
        for line in reader:
            row = line.rstrip().split(",")
            if count == 0:
                try:
                    headers = [row[0], row[1], row[2]]
                except IndexError:
                    sys.exit("Incorrect File Format")
            else:
                try:
                    table.append([row[0], row[1], row[2]])
                except IndexError:
                    sys.exit("Incorrect File Format")
            count += 1

    print(tabulate(table, headers, tablefmt="grid"))


if __name__ == "__main__":
    main()