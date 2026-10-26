"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Martha Cawood
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("Enter number stages: "))  # read an integer number of steps (>0)

#state = "red"

while systime <= maxtime:
    for key, value in states.items():
        length = int(value)
        state = key


        for j in range(length):
            if systime <= maxtime:
                print(f"Time {systime:03} State {state}")
                systime = systime + 1
            else:
                break


    

# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14

