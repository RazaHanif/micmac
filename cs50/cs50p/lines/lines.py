import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if check_file(sys.argv[1]):
            if is_file(sys.argv[1]):
                print(read_lines(sys.argv[1]))

def check_file(file):
    if str(file).endswith(".py"):
        return True
    else:
        sys.exit("Not a Python file")

def is_file(file):
    try:
        text = open(file)
        text.close()
        return True
    except FileNotFoundError:
        sys.exit("File does not exist")

def read_lines(file):
    out = []
    with open(file, "r") as text:
        for line in text:
            if line.lstrip().startswith("#"):
                pass
            elif line.isspace():
                pass
            else:
                out.append(line.rstrip())

    return len(out)

if __name__ == "__main__":
    main()