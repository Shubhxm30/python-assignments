# Task-16 Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

a = "Shubham"
b = "Tanish"

print("before swapping =",a," ",b)

a1 = b[ :2] + a[2: ]
b1 = a[ :2] + b[2: ]

print("After swapping =",a1," ",b1)