# Conditionals
if 1 < 2
  puts "2 is greater than 1"
elsif 3 > 2
  puts "3 is greater than 2"
else
  puts "1 is greater than 2"
  puts "hello!!"
end

# Unless
hungry = false

unless hungry
  puts "I'm writing Ruby programs!"
else
  puts "Time to eat!"
end

# User input
print "Enter a string:"
user_input = gets.chomp

user_input.downcase!

if user_input.include? "s"
  user_input.gsub!(/s/, "th")
  puts "#{user_input}"
else
  print "There are no s in your string"
end


# String interpolation
puts "#{}"

# While loops
i = 0
while i < 5
  puts i
  # Add your code here!
  i = i + 1  
end

# Until loop
counter = 1
until counter > 10
  puts counter
  # Add code to update 'counter' here!
  counter += 1
end

# For loop
# Exclude 10
for num in 1...10
  puts num
end

# Include 15
for num in 1..15
  puts num
end

# Loop
j = 20
loop do
  j -= 1
  print "#{i}\n"
  break if j <= 0
end

# Loop two
k = 0
loop do
  k += 1
  print "Ruby!"
  break if k == 30
end

# Arrays
my_array = [1, 2, 3, 4, 5]
my_array.each do |x|
  puts x
end

# Times loop
10.times do 
  print "hii!" 
end



# Ternary
puts true ? "icarusgk" : "pops"

# Collect
fibs = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# Add your code below!
doubled_fibs = fibs.collect do |num| num * 2 end
puts "Outputting: #{doubled_fibs}"