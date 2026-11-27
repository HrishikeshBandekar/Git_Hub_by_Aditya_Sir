
age1 : int =10
print(type(age1))
print(age1)


# type hint do not enforce types at runtime, 
# type hint code get ignored at runtime by python

age2 : int ='ram'
print(type(age2))
print(age2)





# function without type hint 

def func1(param):
    param.reverse()
    return param

print(func1([1,2]))



def full_name1(first_name,last_name):
    return f'{first_name.title()} {last_name.title()}'

print(full_name1('rushi','bandekar'))



# function with type hint 

def func2(param:list[str ])->list[str]:
    param.reverse()
    return param

print(func2(['1','2']))






def full_name2(first_name: str ,last_name :str)-> str:
    return f'{first_name.title()} {last_name.title()}'

print(full_name2('rushi','bandekar'))




#################################


age1
age2
func1
func2
full_name1
full_name2



#################################

"""
Common type hint

int
float
str
bool
bytes

****generic type hint*****

list[int]
tuple[int, str]
dict[str, int]
set[int]

"""

def common_items(item1:int,item2:float,item3:str,item4:bool,item5:bytes):
    return item1,item2,item3,item4,item5

print(common_items(1,
                1.2,
                'rushi',
                True,
                b'1'))





def process_list(items:list[str])->None:
    
    for value in items:
        print(items)
        
print(process_list(['1','2','3']))






def process_tuple_set(item_t:tuple[int,str,bool],items_S:set[int]):
    return item_t,items_S

print(process_tuple_set((1,2,7,8),{1,'ram','sham'}))





def process_dict(product:dict[str:int]):
    
    for key,value in product.items():
        print(key,"->",value)
        
print(process_dict({'pen':10,
                    'book':5,
                    'pencil':89}))




# Any

from typing import Any

def random(data):
    return data
print(random(1))

def random(data:Any)->Any:
    return data
print(random(1))


#typehint with union
# Union (|)
# Allows more than one type in a type hint.
# Introduced with the '|' syntax in Python 3.10.

def process_id(id : int | str ):
    print(id)
    
process_id(1)


# typehint with by default argument with None

def process_id(id : int | None = None):
    if id:
        print(id)
    else:
        print('no_id')
    
process_id(1)
process_id()




# type hint for iterable

from collections.abc import Iterable

def array(item : Iterable[str]):
    
    item.reverse()
    
    return item
        
print(array(['ram',1,2,'ink']))





## type hint with class

class Person:
    
    def __init__(self,name :str ,age:int)-> None:
        self.name=name
        self.age=age

def get_person(one_person : Person)->tuple[str]:
    
    return one_person.name,one_person.age

p1=Person('rushi',28)

print(get_person(p1))



# literal in type hint
#Literal is used when you want to allow  specific exact values for literal, not just a dataytpe
# does not enforce type

from typing import Literal

def set_access(name : str, Role : Literal['Admin','Editor','Viwer']) -> str:
    return f'{name} as a {Role} permission'

print(set_access('rushikesh','Admin'))
print(set_access('sham','Viwer'))
print(set_access('ram','xyz'))   # does not enforce type



# Enum in TypeHint
# we can re-use role class multiple places

from enum import Enum

class Role(Enum):
    Admin='admin'
    Editor='editor'
    Viwer='viwer'
    
def get_access(user : str, role :Role)-> str:
    return f'{user} has role name :-{role.name}, for value:-{role.value}'
    

print( get_access('rushi',Role.Admin))
    