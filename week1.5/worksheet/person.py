# Worksheet 1.5: Person class

from datetime import datetime

class Person:
    """
    A Person, with a name and a date of birth.
    """
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    
    def __init__(self, name, birth):
        
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if name == "":
            raise ValueError("Name cannot be empty")
        
        self.name = name

        if not isinstance(birth, str):
            raise TypeError("Birth must be a string")

        try:
            self.birth = datetime.strptime(birth, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Birth must be a valid date in the correct format")
        


    def __str__(self):
        return f"{self.name} has birthday on the {self.birth}"

    

    

person1 = Person("Martha", "12/09/2007")
person2 = Person("Henry", 234)
person3 = Person(234, "09/06/2008")



print(person1)
print(person2)
print(person3)

    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
