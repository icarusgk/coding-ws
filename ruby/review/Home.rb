class Home
  @@houses = 0
  attr_reader :name, :persons
  
  def initialize(name, persons)
    @name = name
    @persons = persons
    @@houses += 1
  end

  def self.houses_added
    @@houses
  end
end