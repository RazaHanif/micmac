import cs50

while True:
    n = cs50.get_int("Height: ")
    if 0 < n < 9:
        break

for i in range(n):
    s = i + 1
    print(" " * (n - s), "#" * (s), sep="")
