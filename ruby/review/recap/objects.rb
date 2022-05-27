class Person
  @@organs = [:stomach, :head, :brain]
  def initialize(name)
    @name = name
  end

  def greet
    "Hello everyone! This is #{@name}"
  end

  def name
    @name
  end

  def self.organs
    @@organs
  end
end

yuji = Person.new "Yuji"
roger = Person.new "Roger"

puts yuji.name
puts roger.greet
puts Person.organs