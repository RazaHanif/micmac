name = input("Whats your name? ")

# write to file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# read from file
with open("names.txt", "r") as file1:
    for line in sorted(file1):
        print("Hello,", line.rstrip())
