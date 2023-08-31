# Task-6 Write python program that swap two number with temp variable and without temp variable.

# using temp variable

n1 = int(input("Enter the Num="))
n2 = int(input("Enter the Num="))

print ("entered two num is =",n1,",",n2)

temp = n1
n1 = n2
n2 = temp

print ("after swapping n1 is ",n1)
print ("after swapping n2 is ",n2)

# without using temp

x = 5
y = 20

x,y = y,x 
print("x=",x)
print("y=",y)