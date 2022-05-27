# Yield
def double(n)
  yield(n)
end

double(8) do |n| n * 2 end

# Procs
multiples_of_3 = Proc.new do |n|
  n % 3 == 0
end

print (1..100).to_a.select(&multiples_of_3)


floats = [1.2, 3.45, 0.91, 7.727, 11.42, 482.911]
# Write your code below this line!
round_down = Proc.new do |f| f.floor() end


# Write your code above this line!
ints = floats.collect(&round_down)
print ints

# Here at the amusement park, you have to be four feet tall
# or taller to ride the roller coaster. Let's use .select on
# each group to get only the ones four feet tall or taller.

group_1 = [4.1, 5.5, 3.2, 3.3, 6.1, 3.9, 4.7]
group_2 = [7.0, 3.8, 6.2, 6.1, 4.4, 4.9, 3.0]
group_3 = [5.5, 5.1, 3.9, 4.3, 4.9, 3.2, 3.2]

# Complete this as a new Proc
over_4_feet = Proc.new do |height| height >= 4 end

# Change these three so that they use your new over_4_feet Proc
can_ride_1 = group_1.select(&over_4_feet)
can_ride_2 = group_2.select(&over_4_feet)
can_ride_3 = group_3.select(&over_4_feet)

puts can_ride_1
puts can_ride_2
puts can_ride_3

def greeter
  yield
end

phrase = Proc.new do puts 'Hello there!' end

greeter(&phrase)

hi = Proc.new do puts 'Hello!' end

hi.call

# Symbols to procs
strings = ['1', '2', '3']
nums = strings.map(&:to_i)

# Example 2
numbers_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

strings_array = numbers_array.collect(&:to_s)

puts strings_array



# Lambdas
def lambda_demo(a_lambda)
  puts "I'm the method!"
  a_lambda.call
end

lambda_demo(lambda do puts "I'm the lambda!" end)

strings = ['leonardo', 'donatello', 'raphael', 'michaelangelo']
# Write your code below this line!

symbolize = lambda do |string| string.to_sym end

# Write your code above this line!
symbols = strings.collect(&symbolize)
print symbols

# Difference between procs and lambda

def batman_ironman_proc
  victor = Proc.new { return 'Batman will win!' }
  victor.call
  'Iron Man will win!'
end

puts batman_ironman_proc

def batman_ironman_lambda
  victor = lambda { return 'Batman will win!' }
  victor.call
  'Iron Man will win!'
end

puts batman_ironman_lambda


# Passing a lambda to select
my_array = ['raindrops', :kettles, 'whiskers', :mittens, :packages]

# Add your code below!
symbol_filter = lambda do |element| element.is_a? Symbol end

symbols = my_array.select(&symbol_filter)

puts symbols


# Float filter
odds_n_ends = [:weezard, 42, 'Trady Blix', 3, true, 19, 12.345]

# Add your code below!
float_filter = Proc.new do |el| el.is_a? Integer end

ints = odds_n_ends.select(&float_filter)

puts ints



# Lambda Review
crew = {
  captain: 'Picard',
  first_officer: 'Riker',
  lt_cdr: 'Data',
  lt: 'Worf',
  ensign: 'Ro',
  counselor: 'Troi',
  chief_engineer: 'LaForge',
  doctor: 'Crusher'
}
# Add your code below!
first_half = lambda do |key, value| value < 'M' end
a_to_m = crew.select(&first_half)

puts a_to_m


