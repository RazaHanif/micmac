# Turn camel case names into snake case firstName -> first_name
def main():
    # Get input from user
    camel = input("camelCase: ")
    snake = cam_to_snake(camel)
    snake = input("")

    # Output to user
    print("snake_case:", snake)

# Convert from camel to snake
def cam_to_snake(name):
    text = name
    for char in text:
        if char.isupper():
            text = text.replace(char, "_" + char.lower())
    return text

# Run program
main()