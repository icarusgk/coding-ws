# As you already know, decorators can help change the behavior of a function
# without modifying its code. In this topic, we will discuss three main
# built-in decorators that can help us to work with classes: staticmethod,
# classmethod, and property.

# * @staticmethod
# This decorator can be used to bind a function to a class as its method.
# In the following example, we have the CharType class and the method to
# get the type of character:

class CharType:
    @staticmethod
    def get_type(char):
        if char.isalpha():
            return 'letter'
        elif char.isdigit():
            return 'digit'
        else:
            return 'other'


print(CharType.get_type('a'))  # letter
print(CharType.get_type('1'))  # digit

# We can access the static method without creating an instance of the class.

# Even though a static method belongs to a class and all its instances,
# it does not get any access to instance internals.


# * @classmethod

# As you know, a "regular" method takes an instance of the class as its
# first argument, and then we use self to refer to it.
# Class methods, on the contrary, do not require particular class instances;
# they have access only to general class attributes and properties.
# Because of this, their first parameter should always be cls,
# which represents the class itself, and not the class instance,
# denoted by self.

# Example
class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        return f'{self.name} ({self.surname})'

    def __str__(self):
        return f'{self.name}!'


    @classmethod
    def from_string(cls, data):
        name, surname = data.split(' ')
        # passing the string values to the initialization call
        # the init method

        # We may carry out some kind of preprocessing before
        # actually creating a new object
        return cls(name, surname)


user = User.from_string('Roger Castro')
print(user.get_info())
print(user)

# * @classmethod vs @staticmethod
# static methods act as function outside the class and are ofthen used as
# utility methods

# class methods always take the class as the first argument
# They are frequently used as alternative constructors that create class
# objects for various use cases


# * @property
# This decorator is designed to access a method as if it was an attribute of
# a class.

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.full_name = f'{self.name} {self.surname}'


student = Student('Santa', 'Claus')
print(student.full_name)  # Santa Claus

# If we change the student's name the full_name will remain the same because
# it was set during initialization
student.name = 'Father'

print(student.name)  # Father
print(student.full_name)  # Santa Claus

# It is a perfect case to use the @property decorator!
# If we define full_name using the decorator, we will
# evaluate the method every time it is accessed as an attribute.


class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return f'{self.name} {self.surname}'


student = Student('Santa', 'Claus')
print(student.full_name)  # Santa Claus

student.name = 'Father'
print(student.name)  # Father
print(student.full_name)  # Father Claus



