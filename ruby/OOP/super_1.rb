# super() in initialize
class Animal
  attr_accessor :name

  def initialize(name)
    @name = name
  end
end

class GoodDog < Animal
  attr_accessor :color
  
  def initialize(name, color)
    super(name)
    @color = color
  end
end

bruno = GoodDog.new "bruno", "brown"

puts bruno.name
puts bruno.color