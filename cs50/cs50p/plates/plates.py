def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = True

    if not check_length(s):
        valid = False
    else:
        if not starts_with_two_letters(s):
            valid = False
        else:
            if s.isalpha():
                if not s.isalnum():
                    valid = False
            elif s.isalnum():
                if not char_after_num(s):
                    valid = False
                else:
                    if not first_num_zero(s):
                        valid = False
                    else:
                        if not s.isalnum():
                            valid = False
            else:
                valid = False

    return valid


def check_length(string):
    # chack for length, min 2 max 6
    length = len(string)
    if length >= 7 or length <= 1:
        return False
    else:
        return True

def starts_with_two_letters(string):
    # must start with 2 letters
    valid = True

    if not string[0].isalpha():
        valid = False

    if not string[1].isalpha():
        valid = False

    return valid

def char_after_num(string):
    # no letters after numbers
    index = -1
    length = len(string)
    valid = True
    for i in range(length):
        index += 1
        if string[i].isdigit():
            for j in range(length - index):
                if string[i + j].isalpha():
                    valid = False
    return valid

def first_num_zero(string):
    valid = True
    check = True
    for i in range(len(string)):
        if check:
            if string[i].isnumeric():
                check = False
                if string[i] == "0":
                    valid = False
    return valid

main()