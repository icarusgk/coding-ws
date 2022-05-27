def greeting
  puts "Hello there!"
end

def array_of_10
  puts (1..10).to_a
end

# Call the method
array_of_10

# Splat arguments
# Splat arguments are arguments preceded by a *, which tells 
# the program that the method can receive one or more arguments.

def what_up(greeting, *friends)
  friends.each { |friend| puts "#{greeting}, #{friend}!" }
end

what_up("What up", "Ian", "Zoe", "Zenas", "Eleanor")

# RESULT
# What up, Ian!
# What up, Zoe!
# What up, Zenas!
# What up, Eleanor!


def greeter(name)
  return "Hello #{name}"
end

def by_three?(number)
  return number % 3 == 0
end

def alphabetize(arr, rev=false)
  arr.sort!
  if rev
    arr.reverse!
  else
    return arr
  end
end

numbers = [1, 4, 5, 2]

puts alphabetize(numbers)