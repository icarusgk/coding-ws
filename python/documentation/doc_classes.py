class Cat():
    """ Creates a Cat object """

    def __init__(self, name, age):
        """
        Initializes the object.

        Parameters:
        name - a string with the cat's name,
        age - an int, the cat's age
        """
        self.name = name
        self.age = age

    def say_hi(self):
        """ Prints a greeting with the cat's name """
        print('Hi, I am', self.name)


if __name__ == '__main__':
  main()

# pydoc prioritizes docstrings over comments