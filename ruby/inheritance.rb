module Swimmable
  def swim
    "I'm swimming"
  end
end

class Animal
  def initialize(name)
    @name = name
  end
end

class Dog < Animal
  DOG_YEARS = 7

  attr_reader :age, :name

  def initialize(age, name)
    super(name)
    @age = age
  end


  def public_disclosure
    "#{self.name} in human years is #{human_years}"
  end

  private
  
  def human_years
    age * DOG_YEARS
  end

end

class Cat < Animal
  include Swimmable
end



fido = Dog.new 20, "Fido"

puts fido.age
puts fido.name

puts fido.public_disclosure

kitty = Cat.new "kitty"
puts kitty.swim

