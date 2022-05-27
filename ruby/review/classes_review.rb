class Dog
  attr_accessor :name
  LEGS = 4

  def initialize(name)
    @name = name
  end

  def to_s
    "My name is fido"
  end

  def self.what_am_i
    "I'm a Dog class"
  end

  def what_is_self
    self
  end

  def self.legs
    LEGS
  end

end

fido = Dog.new "fido"
puts fido.name

puts "#{fido.name} has #{Dog.legs}"

fido.name = "new fido"
puts fido.name



puts Dog.what_am_i

puts fido.what_is_self

