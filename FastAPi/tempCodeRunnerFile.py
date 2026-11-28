from pydantic import BaseModel

class Student(BaseModel):
    
    name:str
    age:int
    gpa:float
    
s1=Student(name='rushi',age=28,gpa=2.5)  # positive scenario
print(s1)

s1=Student(name='rushi',age='28',gpa=True)  # by default lax mode
print(s1)