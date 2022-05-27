name = "Somebody else"

def print_full_name(first_name, last_name)
  name = first_name + last_name
  puts name
end

print_full_name "Se", "e"
puts name


# Blocks
total = 0
[1, 2, 3, 4].each do |n|
  total+=n
end
puts total


# Scope
# A new method is created
a = 5
3.times do |n|
  a = 3
end

puts a


# Not a method invocation
arr = [1, 2, 3]

for i in arr do
  a = 5
end

puts a


# The convention is to use curly braces for one liners
3.times { |n| a = 3 }

