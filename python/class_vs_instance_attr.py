class Pet:
    kind = "mammal"
    n_pets = 0
    pet_names = []

    # Instance attributes
    def __init__(self, spec, name):
        self.spec = spec
        self.name = name
        self.legs = 4
        Pet.n_pets += 1
        Pet.pet_names.append(self.name)


tom = Pet("cat", "Tom")
print(Pet.n_pets, Pet.pet_names)
avocado = Pet("dog", "Avocado")
print(Pet.n_pets, Pet.pet_names)
ben = Pet("goldfish", "Benjamin")

print(tom.kind)
print(avocado.kind)
print(ben.kind)

# When we try to modify the class attribute from the instance
# using these operators, we essentially create a new instance
# attribute for that particular object.
ben.kind = 'fish'
ben.legs = 0
print(ben.kind)
print(ben.legs)

# Adding attributes
# To classes
Pet.all_pets = [tom.spec, avocado.spec, ben.spec]
print(Pet.all_pets)

# To instances
avocado.breed = 'corgi'

# The class itself wouldn't have this attribute, so the following lines of code would
# cause an error
# ben.breed  # AttributeError
# Pet.breed  # AttributeError
# tom.breed  # AttributeError



