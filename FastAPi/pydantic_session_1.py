

# Pydantic is a Python library used for data validation nad  enforcing data types.
# Pydantic ensures that the data your application receives follows the structure and rules you have defined.
# strict mode :- like fail fast mode, dont convert
# flex Mode:- convert the data
# 2. Converts compatible input values into the expected datatype.
# 3. Example: "25" (str) -> 25 (int).
# 4. It is the default mode 



# install pydantic
# in terminal --> uv pip install pydantic






# before pydantic

class Student:
    
    def __init__(self,name: str , age:int ,gpa :float):
        self.name=name
        self.age=age
        self.gpa=gpa
        
s1=Student(name='hrishi',age='twenty',gpa=True)
print(s1.name,s1.age,s1.gpa, sep='\n')


# after pydantic
# BaseModel Class Provides this methods(student just inherting)
#    __init__()  -> Initializes the model and validates input data.
#    __str__()   -> Provides a readable string representation.
#    __repr__()  -> Provides a developer-friendly representation.


from pydantic import BaseModel

class Student(BaseModel):
    
    name:str
    age:int
    gpa:float
    status:bool
    
s1=Student(name='rushi',age=28,gpa=2.5,status=)  # positive scenario
print(s1)

s1=Student(name='rushi',age='28',gpa=True)  # by default lax mode
print(s1)

s2=Student(name='ram',age='twenty',gpa=True)  # it will not work
print(s2)

