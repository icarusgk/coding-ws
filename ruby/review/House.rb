class House
  attr_reader :height, :name

  def initialize(name, height)
    @name = name
    @height = height
  end

  def to_s
    "#{self.name} #{self.height}"
  end
end


# n = { name: { hi: { there: :name } } }
# h = name: :hi
# # p n[:name]
# p h

# def print_symbol(hash)
#   print "BEEPP BOPP - "
#   if hash[:name] == :roger
#     "Your name is rendered as Roger!"
#   elsif hash[:name] == :terminal
#     "Your name is being displayed in the terminal"
#   end
# end

# p print_symbol name: :roger
# p print_symbol name: :terminal
