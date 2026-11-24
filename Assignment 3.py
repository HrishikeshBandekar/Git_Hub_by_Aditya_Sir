# Q1. Ask the user for a string and check whether it is a palindrome or not.
# A palindrome string is the same when read forward and backward (e.g., "madam", "racecar").



#3

a=input('enter your string')

if a == a[::-1]:
    print('string is palidrome')

else:
    print('strinfg is nbot palidrome')




# Q2. Given a list of integers, compute the average of all numbers in the list.

list=[1,2,4,1.5,1.8,10]

avg=sum(list)/len(list)

print(avg)



# Q3. Input two lists of integers from the user. Merge them into one list and sort the result.
# Example:
# list1 = [1, 2, 7]
# list2 = [2, 4, 5]
# result = [1, 2, 2, 4, 5, 7]

# 1

list1=list(map(int,input('enter list1 numbers').split()))
list2=list(map(int,input('enter list1 numbers').split()))
list1+=list2
list1.sort()

print(list1)



    

# Q4. Given a tuple of integers, 
# create:
# • A tuple of all even numbers
# • A tuple of all odd numbers

integers=(1,2,3,4,5,6,7,8,9,10)

even=[]
odd=[]

for i in integers:

    if i % 2 ==0:
        even.append(i)
    else:
        odd.append(i)

even=tuple(even)
odd=tuple(odd)

print(f'tuple of even numbers {even} \n tuple of odd numbers {odd} ')

# Q5. Create a dictionary where:
# • Keys = student names
# • Values = marks (integer)
# Write a menu-based program where the user presses a key ('A', 'B', 'C', 'D') depending on the operation:
# A - Add a student
# B - Update marks
# C - Search for a student
# D - Display all students and marks


student_info={'sham':98,
              'ram':99,
              'aditya':85,
              'gauri':87}




menu=input( "adding new student data - press A\nUpdate existing marks - Press B\nSearch for a student - press C\nDisplay all student marks - press D")

if menu == 'A':
    name=input('enter student name')
    marks=input('enter student marks ')

    student_info.update({name:marks})
    

elif menu == 'B':
    name=input('enter student name whose marks going to update')
    marks=input('enter student new marks ')
    
    if student_info.get(name) !=None:
       student_info[name]=marks
       print(student_info[name])
    else:
        print('student name is invalid')

elif menu == 'C':
    name=input('enter student name')

    if name in student_info.keys():
        print(f'{name}:-{student_info[name]}')
elif menu == 'D':

    for name,marks in student_info.items():
        print(f'{name} : {marks}')
   







# Q6. Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example: {"apple": 5, "banana": 6, "kiwi": 4, "cherry": 6, "mango": 5}

words = ["apple", "banana", "kiwi", "cherry", "mango"]
dicti={}


# best approch
for i in words:
    dicti.update({i:len(i)})

print(dicti)



# Q7. Write a program that takes a string from the user and prints the number of spaces in the string.

string=input('enter your string')
print(string.count(' '))

# Q8. Write a program to check whether two lists share no common elements.
# Hint: Use sets.
# Example:
# list1 = [1, 2, 3, 4]
# list2 = [5, 6, 7, 8]   # no common elements
# list1 = [1, 2, 3]
# list2 = [3, 4]         # share common elements

list1=[1,2,3,4]
list2=[5,6,7,8]

list1=set(list1)
list2=set(list2)


if list1.isdisjoint(list2) :
    print('no common elements')
else:
    print('common elements')

#2

common=list1.intersection(list2)

if common:
    
    print('elements in common')
else:
    print('elements are not in common')
    



# Q9. Given a list, print all elements that appear more than once.
# Hint: Use sets.

list=[1,2,2,3]

seen=set()
duplicates=set()       

for item in list:
    if item  in seen:
        duplicates.add(item)
    else:
        seen.add(item)

print(duplicates)



# 2

list=[1,2,2,3]

seen=set()
duplicates=set()

for item in list:
    if item  not in  seen:
        seen.add(item)
        
    else:
        duplicates.add(item)
        

print(duplicates)



# Q10. Ask the user for a string and print:
# • All unique characters
# • The count of unique characters


string = "hello"
unique = set(string)
print(unique)


# below way to find non repeatating characters


string=input('enter your string')

unique_count=0
for i in string:
    if string.count(i) <=1:
        unique_count+=1
        
print(unique_count)
        














#




# give list of tuples with info(name,subject)
# list all unique courses
# list students enrolled in english
# create dictionary(student,set of cources)


info=[('alice','math'),
      ('shubham','english'),
      ('kiran','math'),
      ('alice','history'),
      ('shubham','physics')]


cources_set=set(map(lambda x : x[1] , info))   # all unique cources


l=[]
student_info={}

for name,cources in info:

    if cources == 'english':

         l.append(name)

    if student_info.get(name) == None:

         student_info.update({name :set()})
         student_info[name].add(cources)

    else:
        student_info[name].add(cources)


print(cources_set,l,student_info)

    














