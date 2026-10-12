# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers



numbers = read_numbers()

if numbers == []:
    sys.exit("Error: no numbers provided")

else:
    total = sum(numbers)
    count = len(numbers)

    mean = total / count

    #MEDIAN
    ordered_numbers = sorted(numbers)

    if count % 2 == 0:
        left_middle_index = int((count / 2) -1)
        right_middle_index = ((count+2) // 2) -1

        median = (ordered_numbers[left_middle_index] + ordered_numbers[right_middle_index]) / 2

    else:
        middleIndex = count // 2
        median = ordered_numbers[middleIndex]
        

    maximum = ordered_numbers[len(ordered_numbers)-1]

    minimum = ordered_numbers[0]

    print(f"Minimum = {minimum}")
    print(f"Maximum = {maximum}")
    print(f"Mean = {mean}")
    print(f"Median = {median}")



    

#####need to ensure that all items in the list are numbers##################



    