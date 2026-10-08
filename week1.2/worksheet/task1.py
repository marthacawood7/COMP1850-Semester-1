# Worksheet 1.2: Task 1 Solution
import sys

while True:
    try:
        grade = int(input("Enter the grade: "))
        break 
    except ValueError:
        sys.exit("Error: Grade must be an integer between 0 and 100!")


if grade >= 0 and grade <= 100:
    if grade >= 70:
        result = "Distinction"
    elif grade >= 40 and grade < 70:
        result = "Pass"

    else:
        result = "Fail"

else:
    sys.exit("Error: Grade must be an integer between 0 and 100!")


print(f"{grade} is a {result}")