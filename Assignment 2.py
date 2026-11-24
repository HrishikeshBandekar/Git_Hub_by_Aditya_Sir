# Assignment 2: Python Fundamentals
# Note: Each question is written as a comment so you can solve them step by step.

# Q1. Write a program that takes salary as input.
# Using conditional statements, calculate the final tax rate based on these rules:
# • If salary < 30,000 → 5%
# • If salary is 30,000–70,000 → 15%
# • If salary > 70,000 → 25%

salary=int(input('enter your salary'))

if salary < 30000:
    print(5 * salary/ 100)
elif salary >=30000 and salary <=70000:
    print((15/100) * salary)
elif salary >70000 :
    print((25/100) * salary)



# Q2. Write a function that takes two integers a and b,
# and prints all even numbers between them (inclusive).

a=int(input('enter your starting number'))
b=int(input('enter your end number'))

for i in range(a,b+1):

    if i % 2 ==0:
     print(i)





# Q3. Write a function that prints the digits of a number n.
# Example: n = 312 → digits are 3, 1, and 2.
# Hint: The rightmost digit of a number N is N % 10.
# To remove the rightmost digit, do N = N // 10.


#1

n=int(input('enter your number '))


l=[]
def seprator(n):

   if n ==0:
      return
   
   l.append(n % 10)
   seprator(n // 10)

seprator(n)

l.reverse()
print(l)


#2

n=int(input('enter your number '))
l=[]
def seprator(n):

   if n ==0:
      return
   
   seprator(n // 10)
   l.append(n % 10)

seprator(n)
print(l)


# 3 best way

l=[]
def sep(n):
   
   if n==0:
      return 0
   
   return l.append(n%10),sep(n//10)

sep(12345)
print(l)

# Q4. Write a function to return the count of digits in a number n.


#1

n=int(input('enter your number'))

def count(n):

   if n ==0:

      return 0
   
   return 1 + count(n //10)

print(count(n))

#2

n=int(input('enter your number'))
counter=0
for i in str(n):
   counter+=1

print('from loop',counter)


#3

counter=0
n=123456
def coun(n):
   global counter
   if n==0:
      return
   
   coun(n//10)
   counter+=1
   print('hello from function')

   return "from function",counter

print(coun(n))


# Q5. Write a function to return the sum of digits of a number n.


#1 best way

n=int(input('enter your number'))

def sum(n):

   if n ==0:
      return 0
   
   digit= n % 10

   return digit + count(n // 10)

print(sum(n))


#2
n=int(input("enter your number"))
a=0
for i in str(n):
   a+=int(i)

print(a)


# 3

a=0
n=123
def su(n):
   global a
   if n==0:
      return
   
   su(n//10)
   
   a+=n%10
  

   return a

print(su(n))



# Q6. Write a program to print all numbers from 1 to 100
# that are divisible by both 3 and 5.

for i in range(1,101):
   if i % 3 ==0 and i % 5 == 0:
      print(i)


# Q7. Design a program to continuously input a number from the user
# and print if it is positive or negative,
# until the user enters "Quit".

while True:
   n=input('enter your number')
   

   if n =='quit' :
      break
   elif n< '0':              # here we directly comparing string with string
      print('negative')
   else:
      print('positive number')

# Q8. Let’s create a Simple Calculator.
# Create a function calculator(a, b, operation) that performs:
# • Addition if operation = '+'
# • Subtraction if operation = '-'
# • Multiplication if operation = '*'
# • Division if operation = '/'

a=int(input('enter 1st number'))
b=int(input('enter 1st number'))
operation=input('operation')


def calculator(a,b,operation):
   if operation == '+':
      print(a+b)
   elif operation == '-':
      print(a-b)
   elif operation == '*':
      print(a*b)
   elif operation == '/':
      print(a/b)

calculator(a,b,operation)


# Q9. Write a function is_prime(n) that returns True if n is a prime number,
# and False otherwise, using a loop.
# Hint:
# • Prime check only for numbers >= 2.
# • 2 is the smallest prime number.
# • A number n will always get divided by at least one number in range [2, n-1].
# Example: For 9, check range(2, 8). It gets divided by 3 → non-prime.
# Example: For 7, check range(2, 6). No divisors → prime.


n=int(input('enter your number'))

def is_prime(n):
   for i in range (2,n):
      if n % i == 0:
         return 'non-prime'
   return 'prime'
   
print(is_prime(n))
      


# check for 0-N numbers prime or not

n=int(input('enter your number '))

for number in range (2,n+1):

   for divisior in range(2,number):

      if (number % divisior == 0)  :

         print( number,'is not prime number')
         break
   
   else:
      print(f'{number} is prime number')



# Q10. Let’s create a Number Guessing Game.
# Given a secret number (decided by you),
# write a program that asks the user to guess it and prints:
# • If the guess is above the number → "Too high"
# • If the guess is below the number → "Too low"
# • If the guess matches → "Correct!"

n=int(input('enter user no'))
guess_number=10

if n>guess_number:
   print('too high')
elif n <guess_number:
   print('too low')
else:
   print('correct number')







