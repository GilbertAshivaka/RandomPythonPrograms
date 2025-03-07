import random

class Hat:
    houses = ["Runda", "Kilimanjaro","Mara", "Kwetu"]
    
    
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))



Hat.sort("Gilbert")






import random

class Hat:
    def __init__(self,): 
        self.houses = ["Runda", "Kilimanjaro","Mara", "Kwetu"]
    
    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Gilbert")

