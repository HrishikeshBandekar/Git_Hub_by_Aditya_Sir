class Person:
    
    def __init__(self,name :str ,age:int)-> None:
        self.name=name
        self.age=age

def get_person(one_person : Person)->tuple[str]:
    
    return one_person.name,one_person.age

p1=Person('rushi',28)

print(get_person(p1))