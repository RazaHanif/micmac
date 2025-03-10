import csv
from cs50 import SQL
'''
with open("favorites.csv") as file:
    reader = csv.DictReader(file)
    count = {}
    for row in reader:
        fav = row["problem"]
        if fav in count:
            count[fav] += 1
        else:
            count[fav] = 1

# for key in sorted(count, key=lambda problem: count[problem], reverse=True):
#     print(f"{key}: {count[key]}")

fav = input("Fav: ")
if fav in count:
    print(f"{fav}: {count[fav]}")
'''

# using sql in python

db = SQL("sqlite:///favorites.db")

fav = input("Fav problem: ")

# Dont do this, can lead to sql attacks
# rows = db.execute(f"SELECT COUNT(*) AS num FROM favorites WHERE problem = '{fav}';")

# Do this
rows = db.execute("SELECT COUNT(*) AS num FROM favorites WHERE problem = ?;", fav)

for row in rows:
    print(f"People who like {fav}: {row['num']}")
