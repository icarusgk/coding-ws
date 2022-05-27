# When you call super from within a method, it searches the method 
# lookup path for a method with the same name, then invokes it. Let's 
# see a quick example of how this works

class Animal
  def speak
    "Hello!"
  end
end

class GoodDog < Animal
  def speak
    #  we use super to invoke the speak method from the superclass, 
    # Animal, and then we extend the functionality by appending some 
    # text to the return value.
    super + " from GoodDog class"
  end
end

sparky = GoodDog.new
puts sparky.speak

