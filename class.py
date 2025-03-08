class_body = """
def __init__(self, name, age):
    self.name = name
    self.age = age

def greeting(self):
    return f'Hi, I am {self.name}. I am {self.age} year old.'
"""

class_dict = {}
exec(class_body, globals(), class_dict)

Person = type("Person", (object,), class_dict)

person = Person("Gilbert", 19)


print(f"{person.name} is {person.age} years old")













class Person:
    def __new__(cls, name):
        print(f"Creating a new {cls.__name__} object...")
        obj = object.__new__(cls)
        return obj
    
    def __init__(self, name):
        print("Initializing the Person object...")
        self.name = name

person = Person("John")
