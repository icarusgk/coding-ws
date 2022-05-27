# Basics of a class
class Person
  def initialize(name)
    @name = name
  end
end

matz = Person.new("Yukihiro")



class Computer
  # Global variable
  $manufacturer = "Mango Computer, Inc."

  # Class variable
  @@files = {hello: "Hello, world!"}
  
  def initialize(username, password)
    @username = username
    @password = password
  end
  
  def current_user
    @username
  end
  
  def self.display_files
    @@files
  end
end

# Make a new Computer instance:
hal = Computer.new("Dave", 12345)

puts "Current user: #{hal.current_user}"
# @username belongs to the hal instance.

puts "Manufacturer: #{$manufacturer}"
# $manufacturer is global! We can get it directly.

puts "Files: #{Computer.display_files}"
# @@files belongs to the Computer class.




# Inheritance
class ApplicationError
  def display_error
    puts "Error! Error!"
  end
end

class SuperBadError < ApplicationError
end

err = SuperBadError.new
err.display_error


# Overriding
class Creature
  def initialize(name)
    @name = name
  end
  
  def fight
    return "Punch to the chops!"
  end
end

# Add your code below!
class Dragon < Creature
  def fight
    puts "Instead of breathing fire..."
    super()
  end
end


# Inheritance and overriding review
class Message
  @@messages_sent = 0
  def initialize(from, to)
    @from = from
    @to = to
    @@messages_sent += 1
  end
end

class Email < Message
  def initialize(from, to)
    super(from, to)
  end
end

my_message = Message.new("icarus", "pops")



class Computer
  @@users = Hash.new

  def initialize(username, password)
    @username = usernjame
    @password = password
    @@users[username] = password
    @files = Hash.new
  end
  

  def create(filename)
    time = Time.now
    @files[filename] = time
    puts "#{filename} has been created at #{time}"
  end

  def Computer.get_users
    @@users
  end
end

my_computer = Computer.new("Roger", "1234")

