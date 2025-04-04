from abc import ABC, abstractmethod
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person(name = {self.name})"


class PersonStorage(ABC):
    @abstractmethod
    def save(self, person):
        pass

class PersonDB(PersonStorage):
    def save(self, person):
        return f"Save {person} to database"
    

class PersonJSON(PersonStorage):
    def save(self, person):
        return f"Save {person} to a JSON file."
    
class PersonXML(PersonStorage):
    def save(self, person):
        return f"Save {person} to an XML file."
    

if __name__ == "__main__":
    person = Person("Gilbert Ashivaka")
    storage = PersonXML()
    storage.save(person)

print("Operation completed succesfully.")