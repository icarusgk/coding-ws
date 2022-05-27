# Blocks can be passed as arguments
# The ampersand (&) in the method definition tells us that the argument is a block. 
def take_block(&block)
  block.call
end

take_block do
  puts "block being called in the method!"
end

# with a extra parameter
def take_block_n(number, &block)
  block.call(number)
end

take_block_n 42 do |n|
  puts "Block being called in the method! #{n}"
end

# Procs are blocks that are wrapped in a proc object
talk = Proc.new do
  puts "I am talking"
end

talk.call

# Procs can take arguments
talk_n = Proc.new do |name|
  puts "I am talking to #{name}"
end

talk_n.call "Bob"

# Procs can be passed into methods
def take_proc(proc)
  [1, 2, 3, 4, 5].each do |number|
    proc.call number
  end
end

my_proc = Proc.new do |number|
  puts "#{number}. Proc being called in the method!"
end

take_proc my_proc