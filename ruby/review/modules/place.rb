require_relative 'modules'

p Library::FAV_BOOK
p Library::CHARACTERS
person = Library::Person.new("Roger", 21)
puts person
puts person.farewell
puts Library::greet("Roger")