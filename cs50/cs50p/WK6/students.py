import csv

students = []

with open("students.csv") as page:
    reader = csv.DictReader(page)
    for row in reader:
        students.append({"name":row["name"], "home":row["home"]})

"""
    reader = csv.reader(page)
    for name, home in reader:
        students.append({"name":name, "home":home})
"""
"""
    for line in page:
        name, home = line.rstrip().split(",")
        student = {"name":name, "home":home}
        students.append(student)
"""
"""
        student = {}
        student["name"] = name
        student["house"] = house
"""
"""
    def get_name(student):
        return student["name"]

    SAME AS

    lambda studnet: student["name"]
"""

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} from {student['home']}")

