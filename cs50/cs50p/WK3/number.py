#ValueError user inputs a value that breaks program
# using try/except/else to catch errors
# similar to try catch final

x = input("What is x? ")
try:
    x = int(x)
except ValueError:
    print("x is not an int")
else:
    print(f"x is {x}")