module MyLibrary
  FAVE_MANGA = "Chainsaw Man!"
end

module Hospital
  BEST_DOCTOR = "Dr. Castro"
  
  def attend
    @patients = 3
    "There are #{@patients} patients"
  end
end

class Library
  include MyLibrary
  include Hospital

  @@instances = 0

  attr_reader :name, :fav_book
  attr_writer :fav_book

  def initialize(name)
    @@instances += 1
    @name = name
    @fav_book = MyLibrary::FAVE_MANGA
  end

  def say_doctor
    BEST_DOCTOR
  end

  def self.total
    @@instances
  end
end

fernando = Library.new "Fernando"
modelo = Library.new "Modelo"
puts fernando.name
puts fernando.fav_book
fernando.fav_book = "Jujutsu Kaisen"
puts fernando.fav_book
puts fernando.attend

puts Library.total