# Single inheritance
class Animal:
  def __init__(self, name):
    self.name = name
  

class Dog(Animal):
  pass

cow = Animal("Bessie")
corgi = Dog("Baxter")

print(type(cow) == Animal)
print(type(cow) == object)
print(isinstance(cow, object))
print(isinstance(cow, Animal))
print(isinstance(corgi, Dog))
print(issubclass(Dog, Animal))
print(issubclass(Dog, (Animal, object)))

class Robot:
  pass

# The case with several classes might be somewhat misleading, though. The thing is that the function checks whether any element of the tuple is a parent. Say, we have defined a new class Robot:

# Even though Dog has nothing to do with Robot, in the last case, we got True. So keep this detail in mind when calling this function!
print(issubclass(Dog, (Robot, Animal))) # True
