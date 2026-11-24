# apna college # exercise 1
#1. Q1: Ask the user for their name and age, then print a sentence like:
# "Hello Shradha, you are 21 years old!"
name=input('pls enter your name: ')
age=int(input("please enter your age; "))

print("hello"+" "+name,","+" you are ",age,"years old")
 #using f-string
print(f"hellow {name}, you are {age} years old !")



# Q2: Take two numbers as input from the user and print their
# sum, difference, product, and quotient.
a=int(input("enter number 1;"))
b=int(input("enter number 2;"))

print("sum=",a+b)
print("diff=",a-b)
print("product=",a*b)
print("quotient=",a%b)

# Q3: Ask the user to enter two integers and one float.
# Convert them all to floats and print their average.

a=0
for i in range  (1,3):
   
    a+=float (input("enter your number"))

print(a/i)


# Q4: The user enters a string containing a number (e.g., "45").
# Convert it to:
#   • an integer
#   • a float
#   • a string again
# Print all three values with their types.
a=input("enter your number ")
b=int(a)
c=float(a)

print(b,type(b))
print(c,type(c))
print(a,type(a))

print("next type")

if(1==1):
    b=int(a)
    print(b,type(b))
if(1==1):
    c=float(a)
    print(c,type(c))
if(1==1):
    d=str(a)
    print(d,type(d))

# Q5: Evaluate and print the result of the following expression:
# x = 10 + 3 * 2**2
# Based on what you learnt in the lecture, explain why the output is what it is.
#x =10+3*2**2
#22

#Q6: Write a program to swap values of two numbers entered by the user.

a=int(input("enter your number 1 "))
b=float(input("enter your number 1 "))


#1
temp=a
a=b
b=temp

print(a,b)


a=int(input("enter your number 1 "))
b=int(input("enter your number 1 "))

a,b=b,a

print(a,b)

# Q7: Ask the user for a temperature in Celsius (string input).
# Convert it to float, then calculate and print temperature in Fahrenheit.
# Conversion formula: FahrenheitTemp = (CelsiusTemp * (9/5)) + 32


a=input("enter temeperature ")

CelsiusTemp=int(a)
FahrenheitTemp =(CelsiusTemp * (9/5)) + 32

print(FahrenheitTemp,type(FahrenheitTemp))

# Q8: Take the radius (r) as user input and print the area.
# Use the formula: Area = π * r^2 (value of π = 3.14)

a=int(input("enter your raidus "))

print("area " , 3.14*a**2)

# Q9: Ask the user for Principal (P), Rate (R), Time (T).
# Convert all to float and compute simple interest:
# SI = (P * R * T) / 100

p=int(input("enter your principal amount "))
r=int(input("enter your rate"))
t=int(input("time"))

SI = (p * r * t) / 100

print(SI)

# Q10: Take a decimal number as input (like 45.78) and output its:
#   • integer part → 45
#   • fractional part → .78


a=45.78

f= a-int(a)

print(f,int(a))

#2

a=46.56

print(a//10)




