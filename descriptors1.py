class RequieredString:
    def __set_name__(self, owner, name):
        self.property_name = name

    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        
        return instance.__dict__[self.property_name] or None
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"The {self.property_name} must be a string")
        
        if len(value) == 0:
            raise ValueError(f"The {self.property_name} field cannot be left empty")
        

        instance.__dict__[self.property_name] = value



class Person:
    first_name = RequieredString()
    last_name = RequieredString()


try:
    person = Person()
    person.first_name = 'Gilbert'
except ValueError as e:
    print(e)

print("Operation Succesfull!")