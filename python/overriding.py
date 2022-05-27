class Parent:
    def do_something(self):
        print("Did something")


class Child(Parent):
    def do_something(self):
        print("Did something else")


parent = Parent()
child = Child()

parent.do_something()  # Did something
child.do_something()  # Did something else


# * super()
# Calls the method of the parent class inside the methods of the child class
class Parent:
    def __init__(self, name):
      self.name = name
      print("Called Parent __init__")


class Child(Parent):
    def __init__(self, name):
      super().__init__(name)
      print("Called Child __init__")

jack = Child("Jack")



class Animal:
  def __init__(self, species):
    self.species = species


class Cat(Animal):
  def __init__(self, name):
    # To mantain the species attr we use super()
    super().__init__("cat")
    self.name = name