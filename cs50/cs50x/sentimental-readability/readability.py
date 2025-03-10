from cs50 import get_string


def main():
    # index = 0.0588 * L - 0.296 * S - 15.8
    # Find Letters, Sentences, & Words
    # L = letters / words * 100
    # S = sentences / words * 100

    text = get_string("Text: ")

    letter = count_letters(text)
    # print(letter)
    word = count_words(text)
    # print(word)
    sentence = count_sentences(text)
    # print(sentence)

    l = letter / word * 100
    # print(l)
    s = sentence / word * 100
    # print(s)
    index = 0.0588 * l - 0.296 * s - 15.8
    # print(index)

    if index >= 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print("Grade", round(index))


def count_letters(text):
    letters = 0
    for char in text:
        if char.isalpha():
            letters += 1
    return letters


def count_words(text):
    words = 1
    for char in text:
        if char.isspace():
            words += 1
    return words


def count_sentences(text):
    scentence = 0

    for char in text:
        if char == "!" or char == "." or char == "?":
            scentence += 1
    return scentence


main()
