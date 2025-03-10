def main():
    fuel_in = convert(input("Fraction: "))
    print(fuel_in)
    print(gauge(fuel_in))

def convert(fraction):
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
        except (AttributeError, ValueError):
            raise ValueError("Value must be of INT type")
        else:
            if y == 0:
                raise ZeroDivisionError("Cannot divide by Zero")
            if x > y:
                raise ValueError("X cannot be greater than Y")
            try:
                fraction = (x / y) * 100
            except ZeroDivisionError:
                raise ZeroDivisionError("Cannot divide by Zero")
            else:
                return round(fraction)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif 99 <= percentage:
        return "F"
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()