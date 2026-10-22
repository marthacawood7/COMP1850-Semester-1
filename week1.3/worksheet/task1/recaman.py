# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # this should be your only input


# Your code for the Recaman Sequence
# You should store the sequence in an appropriate data structure named 'sequence'
#####subtract if possible and if not add#####

count = 0
value = 0
sequence = []
for i in range(L):
    if count < value and (value - count) not in sequence:
        value = value - count
        count = count + 1
        
    else:
        value = value + count
        count = count + 1

    sequence.append(value)



# You may wish to use further output for testing purposes while you develop your code

[print(item) for item in sequence]    # this method is reasonably independent of the choice of data structure

# The web page https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence shows about 80 numbers in the sequence