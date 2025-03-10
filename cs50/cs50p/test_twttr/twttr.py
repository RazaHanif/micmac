def main():
    text = input("Input: ")
    txt = shorten(text)
    print("Output:", txt)

def shorten(word):
    sentence = word
    for char in sentence:
        if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U":
            sentence = sentence.replace(char, "")
    return sentence

if __name__ == "__main__":
    main()