# Omit vowels from text
def main():
    # Get input from user
    text = input("Input: ")
    txt = omit(text)
    print("Output:", txt)

# Convert from camel to snake
def omit(phrase):
    sentence = phrase
    for char in sentence:
        if char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U":
            sentence = sentence.replace(char, "")
    return sentence

# Run program
main()