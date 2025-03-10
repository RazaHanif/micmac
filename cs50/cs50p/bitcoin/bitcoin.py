import requests
import sys
import json

def main():

    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        num = float(sys.argv[1])
    except ValueError:
        sys.exit("command-line argument is not a number")

    try:
        res = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        pass
    else:
        temp = res.json()
        try:
            rate_float = temp["bpi"]["USD"]["rate_float"]
        except KeyError:
            print("API integration failure")
        else:
            amount = num * rate_float
            print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
