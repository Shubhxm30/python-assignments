# Task-10 Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

x = int(input("Enter the First Num ="))
y = int(input("Enter the Second Num ="))

if x == y:
    print(True)
if (x - y) == 5:
    print(True)
if (x + y) == 5:
    print(True)
else:
    print(False)
