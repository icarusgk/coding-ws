# Conditional assignment
favorite_book = nil
puts favorite_book

favorite_book ||= "Cat's Cradle"
puts favorite_book

favorite_book ||= "Why's (Poignant) Guide to Ruby"
puts favorite_book

favorite_book = "Why's (Poignant) Guide to Ruby"
puts favorite_book

# Implicit return
# The last value of the function is returned
def multiple_of_three(n)
  n % 3 == 0 ? "True" : "False"
end

# Short-Circuit Evaluation
def a
  puts "A was evaluated!"
  return true
end

def b
  puts "B was also evaluated!"
  return true
end

puts a || b
puts "------"
puts a && b

# .downto .upto
"L".upto("P") do |letter| puts letter end

# Respond to
age.respond_to?(:next)

# Push shovel way
alphabet = ["a", "b", "c"]
alphabet << "d"

caption = "A giraffe surrounded by " << "weezards!"

# Refactor

def first_n_primes(n)
  return "n must be an integer." unless n.is_a? Integer
  return "n must be greater than 0." if n <= 0
  # Implicit return
  Prime.first n
end

first_n_primes(10)
