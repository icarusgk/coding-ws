class Animal
  def speak
    "Hello!"
  end
end

# We use the "<" symbol to signify that the GoodDog class
# is inheriting from the Animal class.
class Cat < Animal
end

# Overriding a method
class GoodDog < Animal
  attr_accessor :name

  def initialize(name)
    self.name = name
  end

  # Ruby checks the object's class first for the method before 
  # it looks in the superclass. 
  def speak
    "#{self.name} says arf!"
  end
end


sparky = GoodDog.new "Sparky"
paws = Cat.new

puts sparky.speak
puts paws.speak