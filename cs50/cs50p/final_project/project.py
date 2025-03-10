# Program that does currency exhange in CLI
# Use https://api.exchangeratesapi.io/v1/ to get current (relative) exchange rates

import pytz
import requests
import time
from datetime import datetime


# API key and global response, limiting currencies for testing
API_KEY = "8c320f362211eeec45a71caaa5b08d42"
info = requests.get(
    "http://api.exchangeratesapi.io/v1/latest",
    params={"access_key": API_KEY, "symbols": "CAD,EUR,GBP,JPY,USD"},
)
response = info.json()

"""
reponse format for reference

response = {'success': True,
            'timestamp': 1698946444,
            'base': 'EUR',
            'date': '2023-11-02',
            'rates': {'CAD': 1.461603,
                    'EUR': 1,
                    'GBP': 0.871545,
                    'JPY': 159.839027,
                    'USD': 1.062756}}
                    """

# List of active currencies & stored response from API call to limit api usage
currencies = ["cad", "eur", "gbp", "jpy", "usd"]
cad = {"rate": response["rates"]["CAD"], "symbol": "$"}
euro = {"rate": response["rates"]["EUR"], "symbol": "€"}
pound = {"rate": response["rates"]["GBP"], "symbol": "£"}
yen = {"rate": response["rates"]["JPY"], "symbol": "¥"}
usd = {"rate": response["rates"]["USD"], "symbol": "$"}


# Main method to start program
def main():
    # Launch program in CLI
    print("************************************************************")
    print("Welcome to Money Exchange")
    print("************************************************************")
    print(f"\u001b[7m Rates last updated : {est_timestamp()} \u001b[0m]")
    print("************************************************************")
    run()


# Bulk of program function
def run():
    # True loop so program only ends when user wants to exit
    while True:
        # Initalize value, get user input with error handling
        start = 2
        try:
            print("Please make a selection")
            start = int(input("1 for currency exchange, 0 for exit: "))
        except ValueError:
            pass

        # Run all needed functions to get values to make calculations and output reponse to user,
        # Formatted and with a time delay until they can make another request (in future this may prevent multiple api calls idk)
        if start == 1:
            # From currency values
            starting_currency = currency("starting")
            starting_rate = rate(starting_currency)
            starting_symbol = symbol(starting_currency)

            # Amount to be converted
            amount = get_amount()

            # To currency values
            ending_currency = currency("ending")
            ending_rate = rate(ending_currency)
            ending_symbol = symbol(ending_currency)

            # Math to convert and format correctly
            total = (amount / starting_rate) * ending_rate
            total = "{:.2f}".format(total)
            amount = "{:.2f}".format(amount)

            # Gotta make this better
            print(
                f"\u001b[1m{starting_symbol}{amount} {starting_currency.upper()} converts to {ending_symbol}{total} {ending_currency.upper()}\u001b[0m"
            )
            print("************************************************************")
            time.sleep(3)

        # If user wants to exit display thank you message and exit
        elif start == 0:
            print("Thank you for using Money Exchange")
            exit("************************************************************")


# Gets amount to convert from user with some error handling
def get_amount():
    amount = -5
    while amount < 0:
        try:
            amount = float(input("Amount to convert: "))
        except ValueError:
            pass
    return amount


# Returns the rate from the api for the selected currency
def rate(curr):
    if curr == "cad":
        return cad["rate"]
    if curr == "eur":
        return euro["rate"]
    if curr == "gbp":
        return pound["rate"]
    if curr == "jpy":
        return yen["rate"]
    if curr == "usd":
        return usd["rate"]


# Returns the symbol from the global dict for the selected currency
def symbol(curr):
    if curr == "cad":
        return cad["symbol"]
    if curr == "eur":
        return euro["symbol"]
    if curr == "gbp":
        return pound["symbol"]
    if curr == "jpy":
        return yen["symbol"]
    if curr == "usd":
        return usd["symbol"]


# Asks user for selection and checks if it is a valid response
def currency(state):
    currency = "oops"
    while currency.strip().lower() not in currencies:
        print(f"CAD, EUR, GBP, JPY, USD")
        currency = input(f"Please choose the {state.title()} currency from the list: ").lower().strip()
    return currency


# Converts unix datetime from API to a readable format in EST
def est_timestamp():
    return datetime.fromtimestamp(
        int(response["timestamp"]), pytz.timezone("US/Eastern")
    ).strftime("%Y-%m-%d %I:%M %p")


if __name__ == "__main__":
    main()
