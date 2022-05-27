require_relative "House"

class Home < House
  attr_reader :type

  def initialize(name, height, type)
    super name, height
    @type = type
  end
end


def get_user_input()
  print "Enter a name for your house: "
  name = gets.chomp.strip
  print "Enter a height for your house: "
  height = Integer(gets.chomp.strip)

  house = Home.new name, height, "Great!"
  puts house
  p "The height of house #{house.name} is #{house.height}. Type: #{house.type}"
end

2.times do
  get_user_input()
end

