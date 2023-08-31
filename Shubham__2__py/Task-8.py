# Task-8 Write a Python program to test whether a passed letter is a vowel or not.

list = ['a','e','i','o','u','A','E','I','O','U']

char = str(input("enter the character = "))

if char in list:
    print("The char is vowel.")
else:
    print ("it is not vowel.")