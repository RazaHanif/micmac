def main():
    while True:
        fuel_in = input("Fraction: ")
        try:
            x, y = fuel_in.split("/")
            x = int(x)
            y = int(y)
        except ValueError:
            pass
        else:
            try:
                fuel_out = (x / y) * 100
            except ZeroDivisionError:
                pass
            else:
                fuel_out = round(fuel_out)
                if 0 <= fuel_out <= 1:
                    fuel_out = "E"
                    print(fuel_out)
                    break
                elif 99 <= fuel_out <= 100:
                    fuel_out = "F"
                    print(fuel_out)
                    break
                elif 2 <= fuel_out <= 98:
                    fuel_out = str(fuel_out)+ "%"
                    print(fuel_out)
                    break
                else:
                    pass

main()