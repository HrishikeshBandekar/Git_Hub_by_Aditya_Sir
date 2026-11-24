# ============================================================
# Q1. BankAccount
# Concept: Classes & Objects
# Create a class with attributes:
#   - account_number
#   - owner_name
#   - balance
# Add methods:
#   - deposit(amount)
#   - withdraw(amount)
#   - check_balance()
# ============================================================

class BankAccount:

    Bank_Name='Bank of Maharashtra'

    def __init__(self,account_number,owner_name,balance):

        self.__account_number=account_number
        self._owner_name=owner_name
        self.__balance=balance

    def setter_deposit(self,deposit):


        if deposit < 0:

            return f'enter correct amount'
        else:
            self.__balance +=deposit

            return f'you deposited amount:-{deposit}'

    def setter_withdrawal(self,withdrawal):

        if withdrawal > self.__balance:

            return f'dont have sufficent balance for withdrawal'
        
        if withdrawal < 0:

            return f'enter correct amount'
        else:
            self.__balance -=withdrawal

            return f'successfully withdrawed amount {withdrawal}'

    def getter_check_balance(self):

        return(f'       welcome to {self.Bank_Name}\n'
              f'Account holder  :-{self._owner_name}\n'
              f'Account  NO     :-{self.__account_number}\n'
              f'your balance is :-{self.__balance}')

A1=BankAccount(account_number=123,owner_name='rushikesh',balance=60_00_000)

account_details=A1.getter_check_balance()
print(account_details)


print(A1.setter_deposit(3_50_000))

print(A1.setter_withdrawal(1_00_000))

print(A1.getter_check_balance())


# ============================================================
# Q2. Book
# Concept: Classes & Objects
# Create a class with attributes:
#   - title
#   - author
#   - list_of_reviews
# Add methods:
#   - add_review(review)
#   - count_reviews()
#   - display_reviews()
# ============================================================

class book:

    def __init__(self,title,author,list_of_reviwers):

        self.title=title
        self.author=author
        self.list_of_reviwers=list_of_reviwers

    def add_review(self,review):

        self.list_of_reviwers.append(review)

    def count_reviews(self):

        print(len(self.list_of_reviwers))

    def display_reviwes(self):

        print(*self.list_of_reviwers)

b1=book('mahabharat','vyash',['r1','r2','r3'])


b1.add_review('r3')
b1.count_reviews()
b1.display_reviwes()

        




# ============================================================
# Q3. Student
# Concept: Encapsulation
# Create a class with private attributes:
#   - __name
#   - __roll_no
#   - __marks
# Provide getter and setter methods with validation:
#   - name cannot be empty
#   - roll_no must be between 1 and 100
#   - marks cannot be negative
# ============================================================

   

class student:

    def __init__(self,name,roll_no,marks):



        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks

    def setter(self,name,roll_no,marks):
        corrections=[]


        if name is None:

            corrections.append('please provide valid name')
           
        if roll_no < 1  or roll_no > 100:

            corrections.append('please provide roll no between 1 - 100')
            
        if marks < 0:

            corrections.append('please provide valid marks')
        
        if corrections:

            return corrections


        self.__name=name
        self.__roll_no=roll_no
        self.__marks=marks

    def getter(self):

        return (f'name of student    :-{self.__name}\n'
                f'roll no of student :-{self.__roll_no}\n'
                f'marks of student   :-{self.__marks}')

s1=student(name='rushi',roll_no=1,marks=30)

print(s1.setter(name=None,roll_no=101,marks=-1000))

print(s1.getter())




# ============================================================
# Q4. Shape
# Concept: Function Overriding
# Create a base class Shape with method area().
# Create subclasses Circle, Rectangle, Triangle
# Each subclass should override area() with its own formula.
# ============================================================


from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Circle(Shape):

    def area(self):
        r = 2
        print(3.14 * r ** 2)


class Rectangle(Shape):

    def area(self):
        w = 5
        l = 8
        print(w * l)


class Triangle(Shape):

    def area(self):
        base = 10
        height = 5
        area = 0.5 * base * height
        print("Area of triangle =", area)


c = Circle()
c.area()

r = Rectangle()
r.area()

t = Triangle()
t.area()



# ============================================================
# Q5. Vehicle
# Concept: Inheritance
# Create a base class Vehicle with attributes:
#   - brand
#   - model
# Create subclasses:
#   - Car (extra attribute: seats)
#   - Bike (extra attribute: engine_cc)
# ============================================================

class vehicle:

    brand='honda'
    model=2005

class car(vehicle):

    seats=7

class bike(vehicle):

    engine_cc=350


print(bike.model,bike.brand,bike.engine_cc)

# ============================================================
# Q6. Employee
# Concept: Abstraction
# Create an abstract class Employee with abstract method calculate_salary().
# Create subclasses:
#   - Intern
#   - FullTimeEmployee
#   - ContractEmployee
# Each should implement calculate_salary() differently.
# ============================================================

from abc import ABC,abstractmethod

class employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass
class intern(employee):

    def calculate_salary(self):

        print('salary of intern is 25_000')
class fulltime_employee(employee):

    def calculate_salary(self):
        print('salary of full time employee is 40_000')

class contract_employee(employee):

    def calculate_salary(self):
        print('salary of contract_employee is 40_000')

i=intern()
f=fulltime_employee()
c=contract_employee()

i.calculate_salary()


# ============================================================
# Q7. Person
# Concept: Constructor Overloading (simulate with default parameters)
# Create a class Person that allows constructor calls with:
#   - name only
#   - name + age
#   - name + age + address
# ============================================================

#1

class person:

    def __init__(self,name=None,age=0,address=None):

        self.name=name
        self.age=age
        self.address=address



p1=person()
p2=person('ram')
p3=person('sham',27)
p4=person('vivek',26,'bandekarwadi')



#2

class person:

    def __init__(self,*args):

        if len(args) == 1:

            self.name=args[0]

        elif len(args) ==2:

            self.name=args[0]
            self.age=args[1]

        elif len(args) ==3:

            self.name=args[0]
            self.age=args[1]
            self.address=args[2]



p1=person()
p2=person('ram')
p3=person('sham',27)
p4=person('vivek',26,'bandekarwadi')




#3

class person:

    def __init__(self,**kwargs):


        if 'name' in kwargs.keys():

            self.name=kwargs['name']

        if 'age' in kwargs.keys():

            self.age=kwargs['age']

        if 'address' in kwargs.keys():

            self.address=kwargs['address']

p1=person()
p2=person(name='ram')
p3=person(name='sham',age=27)
p4=person(name='vivek',age=26,address='bandekarwadi')




# ============================================================
# Q8. Player
# Concept: Instance & Class Attributes
# Create a class Player with:
#   - class variable player_count
#   - instance variables name and level
# Track how many players were created.
# ============================================================

class player:

    player_count=0


    def __init__(self,name=None,level=0):
     
        self.name=name
        self.level=level
        player.player_count+=1



p1=player('ram',1)
p2=player('sham',2)
p3=player('vivek',3)

print(p3.player_count)




# ============================================================
# Q9. Bear
# Concept: Multiple Inheritance
# Create classes Herbivore, Carnivore, Omnivore with some attributes & methods.
# Create a class Bear that inherits from all three to demonstrate multiple inheritance.
# ============================================================


class herbivore:


     name=f'herbivore'

     def class_name(self):

         print(f'you are inside {herbivore.name}')

class Carnivore:


     name='Carnivore'

     def class_name(self):

         print(f'you are inside {Carnivore.name}')

class Omnivore:


     name='Omnivore'

     def class_name(self):

         print(f'you are inside {Omnivore.name}')

class bear(Omnivore,Carnivore,herbivore):

    name='bear'

    def class_name(self):

        print(f'you are inside {bear.name}')


b1=bear()

b1.class_name()




# ============================================================
# Q10. Chat System (Mini Project)
# Concept: OOP Integration
# Create classes:
#   - User
#   - Message
#   - ChatRoom
# Implement functions:
#   - sending messages
#   - viewing chat history
#   - user joining and leaving the chatroom
# ============================================================


# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1   # simple counter

    def __init__(self, sender, content):
        self.sender = sender            # username=Alice chatroom=<room_object>  self is message object refernce sender is user object reference
        self.content = content          # 'hello everyone !!
        self.id = Message.message_counter
        Message.message_counter += 1  

    def __str__(self):                                                 # string representation method
        return f"({self.id}) {self.sender.username}: {self.content} just demo {self.sender.chatroom.name}"  


# -------------------------------
# User Class
# -------------------------------
class User:

    def __init__(self,username):
        self.username=username
        self.chatroom=None

    
    def join_chatroom(self, chatroom):

      
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)    
            self.chatroom = chatroom   #self.chatroom=<room_object>
            print(f"{self.username} joined {chatroom.name}")   


    def leave_chatroom(self):   

        if self.chatroom:

            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None
            
        else:
            print(f"{self.username} is not in any chatroom.")


    def send_message(self, content):

        if  self.chatroom:
             self.chatroom.broadcast(self, content)
        else:
            print(f"{self.username} cannot send a message (not in a chatroom).")


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:

    def __init__(self, name):
        self.name = name
        self.users = [] #u1,u2
        self.messages = [] ## message_object
    
    def __str__(self):

        return f'name:-{self.name}\nuser:-{self.users}\nmessages:-{self.messages} ' 

    def add_user(self, user): 
        
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content) # message_object
        self.messages.append(message)
        print('br',message)   # Show message to all users with help of __str__ of Message class

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()




# ---------------------------------------
# Example Usage
# ---------------------------------------
if __name__ == "__main__": # Run this code,only when the Python file is executed directly, not when the file is imported as a module.

    room = ChatRoom("Python Lounge")  # room --> name=python lounge users=empty messages=empty

    u1 = User("Alice")   #u1-->username=Alice chatroom=none
    u2 = User("Bob")     # u2 --> username=bob chatroom=none
    u3 = User("Charlie")

    u1.join_chatroom(room)  # #u1-->username=Alice chatroom=<room_object>
    u2.join_chatroom(room)  # u2-->username=bob chatroom=<room_object>

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()

# Alice joined Python Lounge
# Bob joined Python Lounge
# (1) Alice: Hello everyone!
# (2) Bob: Hi Alice!
# Charlie joined Python Lounge
# (3) Charlie: Hey guys, what's up?

# Chat History of Python Lounge:
# (1) Alice: Hello everyone!
# (2) Bob: Hi Alice!
# (3) Charlie: Hey guys, what's up?

# Alice left Python Lounge
# Bob left Python Lounge
# Charlie left Python Lounge


#--------------------------------------------------------
#        string representation method
#--------------------------------------------------------

# this method used to show object into human redable string format


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

p = Person("Alice", 25)
print(p)





class Message:

    message_count=1

    def __init__(self,sender,content):

        self.sender=sender
        self.content=content
        self.id=self.message_count
        Message.message_count+=1

    def __str__(self):

        return f'({self.id}){self.sender.username} :-{self.content}'

class User:


    def __init__(self,username):
        self.username=username
        self.chatroom=None


    def join_chatroom(self,chatroom):

        if self.chatroom:

            print(f'you are already part of {self.chatroom.name}')
        else:

            chatroom.add_user(self)
            self.chatroom=chatroom
            print(f'hello {self.username} you are part of {chatroom.name}')

    def leave_chatroom(self):

        if self.chatroom:

            self.chatroom.remove_user(self)
            print(f'{self.username} left the {self.chatroom.name}')
            self.chatroom=None
        else:
            print(f'{self.name} you are not part of any chatgroup')

    def send_message(self,content):

        if self.chatroom:

            self.chatroom.broadcast(self,content)
        else:
            print(f'{self.name} you are not part of any chatgroup')



class ChatRoom:


     def __init__(self,name):

         self.name=name
         self.users=[]
         self.messages=[]

     def add_user(self,user):

         self.users.append(user)

     def remove_user(self,user):

         self.users.remove(user)

     def broadcast(self,sender,content):

         message=Message(sender,content)
         self.messages.append(message)
         print(message)

     def message_history(self):

         print(f'showing message history of chatroom{self.name}')

         for msg in self.messages:

             print(msg)


room=ChatRoom('Boys')

u1=User('rushikesh')
u2=User('shubham')
u3=User('rushikesh')

u1.join_chatroom(room)

u2.join_chatroom(room)

u3.join_chatroom(room)

u1.send_message('hello guys')
u2.send_message('hello rushi')

u1.leave_chatroom()

room.message_history()



