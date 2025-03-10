score = int(input("What is your score? "))

if 0 <= score <= 49:
    grade = "F"
elif 50 <= score <= 59:
    grade = "D"
elif 60 <= score <= 69:
    grade = "C"
elif 70 <= score <= 79:
    grade = "B"
elif 80 <= score <= 100:
    grade = "A"
else:
    grade = "N/A"

print("Grade: " + grade)