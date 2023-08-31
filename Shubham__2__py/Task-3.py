# Task-3 Write a Python program to get the Fibonacci series of given range.

n = int(input("Enter the number = "))
n1 = 0
n2 = 1
count = 0 

if(n <= 0):
    print("Please enter the positive integer")

else:
    print("fibonacci sequence:")
    while count < n:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth 
        count += 1