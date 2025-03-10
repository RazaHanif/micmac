def main():
    yell("This", "is", "cs50")

# map(function, list) = applys that function to each item in that list
def yell(*words):
    uppercased = [word.upper() for word in words]
    '''
    above replaces

    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    '''
    print(*uppercased)

if __name__ == "__main__":
    main()