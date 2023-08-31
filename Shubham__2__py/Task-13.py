# Task-13 Write a Python program to count the number of characters (character frequency) in a string

string = input ("Enter the String =")

freq = {}

for i in string:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

print("frequency of string is = ", str(freq))
