# User input and print it out without any whitepsaces and correctly capitalized

'''
name = input("Whats your name? ").strip().title()
first, last = name.split(" ")
print("Hello, " + first)
'''

print("Hello,", input("Whats your name? ").strip().title())

