from operator import truediv


a="ssss"
b=12
c=3.5
print(a)
print(b)
print(b+c)
bool1=True
bool2=False

print("bool1 & bool2", (bool1 and bool2))
print("bool1 or bool2", (bool1 or bool2))
# datatype conversion
d="31"
e=int(d)
print(float(d))
print(e)
# input() funcn allows to take input from the keyboard as a string
g=input("Enter a name :")
print(g)
# to take integers from user and perform operations on it
a=input("Enter first number")
b=input("Enter second number")
a=int(a)
b=int(b)
avg=(a+b)/2
print("Average of no.'s",avg)