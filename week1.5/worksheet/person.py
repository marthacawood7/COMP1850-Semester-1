# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    
    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    
    def __init__(self, name, birth):
        """Initialise the person object"""
        
        if not isinstance(name, str):
            raise TypeError("Name must be a string")

        if name == "":
            raise ValueError("Name cannot be empty")
        
        self.name = name

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date")

        self.birth = birth
        
    def initials(self):
        """Returns the initials of the person"""
        initials = ""
        for word in self.name.split():
            initials = initials + word[0].upper()
        return initials

    def is_birthday(self):
        """Returns true if it is the persons birthday today, false otherwise"""
        if self.birth.month == date.today().month and self.birth.day == date.today().day:
            return True

        else:
            return False
        


    def __str__(self):
        return f"{self.name} has birthday on the {self.birth}. Is it their birthday today? {self.is_birthday()}. Their initials are: {self.initials()}"
    

    

person1 = Person("Martha Cawood", date(2007, 9, 12))




print(person1)


    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
