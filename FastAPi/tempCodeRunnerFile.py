from enum import Enum

class Role(Enum):
    Admin='admin'
    Editor='editor'
    Viwer='viwer'
    
def get_access(user : str, role :Role)-> str:
    return f'{user} has role name :-{role.name}, for value:-{role.value}'
    

print( get_access('rushi',Role.Admin))