from typing import List, Tuple, Dict
from pydantic import BaseModel

def person(fname: str, lname_age: str | int):
    name_age = fname.title() + " " + str(lname_age)
    return name_age

def print_list(lst: Tuple[str, str, int]):
    for _ in lst:
        print(_)

def print_dict(dic: Dict[str, int]):
    for k, v in dic.items():
        print(k,v)

class Pet:
    sound = "(Not hooman)"
    
    def __init__(self, name: str):
        self.name = name
    
def pet_name(pet: Pet):
    return pet.name + " " + pet.sound

# ======================================================= #

class Person(BaseModel):
    id: int
    name: str
    age: int
    address: str | None = None

# ======================================================= #

if __name__ == '__main__':
    
    print(person("hello","world"))
    print(person("hello",25))

    print_list(("apple","banana",1))

    print_dict({'1':0,'2':1,'3':2})

    pet1 = Pet('Dog')
    pet1.sound = 'Woof'
    print(pet_name(pet1))

    pet2 = Pet('Cat')
    print(pet_name(pet2))

data1 = {'id':"123", 'name':"John", 'age':25, 'address':"London"}
data2 = {'id':456, 'name':"Joe", 'age':30}

# person1 = Person(**data1)
# person2 = Person(**data2)
# print(person1.id, person1.name)
# print(person2.id, person2.address)