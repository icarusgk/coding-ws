module Library
  FAV_BOOK = "Chainsaw Man"
  CHARACTERS = [:denji_surname, :makima_surname, :aki_surname, :power_surname]

  def Library.greet(name)
    "Hello there #{name}"
  end

  class Person
    attr_accessor :name, :age

    def initialize(name, age)
      @name = name
      @age = age
    end

    def to_s
      "Hello, my name is #{@name}"
    end

    def farewell
      "Bye there!"
    end
  end
end

puts "MODULESSSS!!"
def process_names(names)
  new_names = []
  names.each do |character|
    name, surname = character.to_s.split "_"
    # Could use yield !?
    new_names.push "#{name.capitalize} #{surname.capitalize}"
  end
  new_names
end

puts process_names Library::CHARACTERS