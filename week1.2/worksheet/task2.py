# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers


numbers = read_numbers()

#####need to ensure that all items in the list are numbers##################

total = sum(numbers)
count = len(numbers)

mean = total / count


ordered_numbers = sorted(numbers)


if count % 2 == 0:
    count = count + 1

else:
    count = count
    
middleIndex = count // 2
median = ordered_numbers[middleIndex]
    

maximum = ordered_numbers[len(ordered_numbers)-1]

minimum = ordered_numbers[0]

print(f"Minimum = {minimum}")
print(f"Maximum = {maximum}")
print(f"Mean = {mean}")
print(f"Median = {median}")