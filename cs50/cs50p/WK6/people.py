import csv

name = input("Whats your name? ")
home = input("Whats your name? ")

with open("people.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})