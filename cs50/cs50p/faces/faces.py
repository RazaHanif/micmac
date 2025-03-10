def main():
    text = input()
    print(convert(text))

def convert(string):
    string = string.replace(":)", "🙂")
    string = string.replace(":(", "🙁")
    return string

main()