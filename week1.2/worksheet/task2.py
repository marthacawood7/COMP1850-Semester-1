# Worksheet 1.2: Task 2 Solution

floatNumbers = [] 

while True:
    try:
        numbers = int(input("How many float numbers do you want to add to the list?: "))
        break 
    except ValueError:
        sys.exit("Error: You must enter a number")

for i in range(numbers):
    try:
        floatInput = float(input("Enter the float number: "))
        floatNumbers.append(floatInput)

    except ValueError:
        sys.exit("ErrorL You must enter a float number")