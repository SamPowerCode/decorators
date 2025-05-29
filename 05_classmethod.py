'''
The @classmethod decorator in Python is used to define a method that belongs to a 
class and operates on the class itself rather than on instances of the class. 
Class methods take the class (cls) as their first parameter, allowing them to 
access class variables and other class methods.
'''


class Animal:
    type = "Dog"

    @classmethod
    def get_type(cls):
        return cls.type




print(Animal.get_type())
