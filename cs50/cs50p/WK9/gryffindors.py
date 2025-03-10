def is_gryf(s):
    return s["house"] == "Gryffindor"

students = [
    {"name" : "Hermione", "house" : "Gryffindor"},
    {"name" : "Harry", "house" : "Gryffindor"},
    {"name" : "Ron", "house" : "Gryffindor"},
    {"name" : "Draco", "house" : "Slytherin"}
]

# filter(function, dict) function needs to return true or false, creates a dict
gryffindors = filter(is_gryf, students)

for std in gryffindors:
    print(std["name"])