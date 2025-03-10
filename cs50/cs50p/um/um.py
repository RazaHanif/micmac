import re

# Gets input from user and outputs result back into terminal
def main():
    print(count(input("Text: ")))

# Takes user input, firstly pads it with whitespace to correct potentiol errors
# Then uses findall() to get all instances of a string and return it as an int
def count(s):
    s = f" {s} "
    num = re.findall(r"[^\w]um[^\w]", s, re.IGNORECASE)
    return len(num)


if __name__ == "__main__":
    main()
