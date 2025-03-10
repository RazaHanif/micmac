from validator_collection import validators

# Create a program that checks a users email and prints Valid or Invalid
# Cannot use re, must use validator-collection

# gets input from user, runs through validate funtion
def main():
    print(validate(input("What's your email address? ")))

# using validators, outputs correct reponse based on input string
def validate(email):
    try:
        validators.email(email)
    except (ValueError, TypeError, IOError):
        return "Invalid"
    else:
        return "Valid"


if __name__ == "__main__":
    main()
