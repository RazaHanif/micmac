import re

def main():
    #re.serach(pattern, string, flags=0)

    """
    re pattern symbols
    .       any char except a newline
    *       0 or more repetitions
    +       1 or more repetitions
    ?       0 or 1 repetition
    {n}     n repetitions
    {n,m}   n - m repetitions
    ^       specifiy start of the string
    $       specifiy end of the string, or before the newline
    []      specify the string that must match
    [^]     specify the string that cannot match

    \d      decimal digit 0-9
    \D      not a decimal digit
    \s      white space
    \S      not a white space
    \w      alphanumeric + underscore
    \W      not a alphanumeric

    A|B     OR operator
    (...)   a group
    (?:...) not this group
    """

    """
    re flags

    re.IGNORECASE
    re.MULTILINE
    re.DOTALL
    """

    email = input("Whats your email? ").strip()

    # r"______" is a raw string, can use \ to use any of the special chars
    # [^@., ]
    # [A-Za-z0-9_]
    # \w (all 'words')
    if re.search(r"^\w+@(\w+\.)?\w+\.(com|edu|org|ca|net)$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("Invalid")





"""
    email = input("Whats your email? ").strip()

    username, domain = email.split("@")

    if username and domain.endswith(".com"):
        print("Valid")
    else:
        print("Invalid")
"""

"""     if "@" in email and "." in domain:
        print("Valid")
    else:
        print("Invalid")
 """

if __name__ == "__main__":
    main()

""" re (regular expression) library lets you define,
check and replace regular patterns in python,
you can then validate user input against those patterns """