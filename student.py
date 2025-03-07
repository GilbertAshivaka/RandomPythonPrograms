#Classmethods
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house


    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    @classmethod
    def get(cls,):
        name = input("Name  ")
        house = input("House  ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)



if __name__ =="__main__":
    main()






class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        

    def __str__(self):
        return f"{self.name} is from {self.house}"
    

    #Getter for name
    @property
    def name(self):
        return self._name
    
    #Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name.")
        self._name = name
        

    #Getter for house
    @property
    def house(self):
        return self._house
    
    #Setter for house
    @house.setter
    def house(self,house):
        if house not in ["Runda", "Kilimanjaro","Mara", "Kwetu"]:
            raise ValueError("Invalid House")
        self._house = house



def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Your name:  ")
    house = input("House:  ")
    return Student(name, house)

if __name__ == "__main__":
    main()





#Incoperating some error checking
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Runda", "Kilimanjaro","Mara", "Kwetu"]:
            raise ValueError("Invalid House")
        if patronus and patronus not in ["Stag", "Otter", "Jack Rusell Terrier"]:
            raise ValueError("Invalid Patronus")
        self.name = name
        self.house = house
        self.patronus = patronus
        ...
    def __str__(self):
        return f"{self.name} is from {self.house}"


    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Rusell Terrier": 
                return "🐶"
            case _:
                return "🤷‍♂️"


def main():
    student = get_student()
    print("Expecto Patronum!!")
    print(student.charm())    

def get_student():
    name = input("Your name:  ")
    house = input("House:  ")
    patronus = input("Patronus:  ") or None
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()






#Introducin classes to our code
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    ...


def main():
    student = get_student()
    print(f"{student.name} is from {student.house}" )

def get_student():
    name = input("Your name:  ")
    house = input("House:  ")
    return Student(name, house)

if __name__ == "__main__":
    main()







#Special case for Padma 
def main():
    student = get_student()
    if student ["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name'] } is from {student['house']}")
    


def get_student():
    name= input("Name:  ")
    house= input("House:  ")
    return {"name": name, "house": house } 

    


if __name__ == "__main__":
    main()




#Using lists & dictionary
def main():
    student = get_student()
    print(f"{student['name'] } is from {student['house']}")
    


def get_student():
    input("Name:  ")
    input("House:  ")
    return {"name": name, "house": house } 

    


if __name__ == "__main__":
    main()




#Usiing a turple to store the varuables and unpacking in the main function
def main():
    name, house = get_student()
    print(f"{name} is from {house}")


def get_student():
    name = input("Name:  ")
    house =input("House:  ")
    return name, house

if __name__ =="__main__": 
    main()





#Using a functional approach 
def main():
    name = get_name()
    house = get_house()
    print(f"{name} is from {house}")


def get_name():
    return input("Name:  ")

def get_house():
    return input("House")

if __name__ == "__main__":
    main()




#Using a procedural approach
name = input("Name:  ")
house = input("House:  ")
print(f"{name} is from {house } ")
