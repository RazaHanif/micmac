# constants in python

# python doesnt have a "constants" just on honor that all caps vars are constant

"""
MEOWS = 3

for _ in range(MEOWS):
    print("Meow")
"""

# Can add "type hints" var: datatype to tell user/mypy what is expected to ensure no errors
# after function decleration, use -> to hint what the return value is

''' 3 quotes, single or double, will be block line comments,
and can be extracted to documents '''


# Block comment is convention on how to document function comments
def meow(n: int) -> str:
    """
    Meow n times

    :param n: Number of times to meow
    :type n: int
    :raise TypeError:
    :return: A string of n meows, one per line
    :rtype: str
    """
    for _ in range(n):
        return "meow\n" * n

num: int = int(input("Number: "))
print(meow(num), end="")