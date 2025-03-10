name = input("Whats your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        house = "Gryffindor"
    case "Draco":
        house = "Slytherin"
    case _:
        house = "N/A"

print("House:",house)

