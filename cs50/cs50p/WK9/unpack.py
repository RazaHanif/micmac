# unpack

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

'''
coins = [100, 50, 25]

# *var unpacks a list and passes the inside values to function
print(total(*coins), "Knuts")
'''

coins = {
    "galleons" : 100,
    "sickles" : 50,
    "knuts" : 25
}

# to pass in a dict into the function and unpack it you use **var
#  will pass in galleions=100 ...
print(total(**coins), "Knuts")

# *args = multiple args left to right
# **kwargs = key word args - a dict galleons=100
def f(*args):
    for i in range(len(args)):
        print(f"Position {i+1}: {args[i]}")

f(100, 50, 25, 10, 5)