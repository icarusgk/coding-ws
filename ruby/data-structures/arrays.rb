multi_d_array = [
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0],
  [0,0,0,0]
]

multi_d_array.each { |x| puts "#{x}" }

my_2d_array = [
  [false, true, false],
  ["icarus", "pops", "tyke"],
  [20, 19, 3]
]

my_arr = [1, 2, 3, 4]
my_arr.delete 3

print my_arr

repeated_arr = [1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3]
print repeated_arr.uniq

# Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print numbers.select { |n| n > 4 } # [5, 6, 7, 8, 9, 10]

# The block, {|i| puts i}, is passed the current
# array item each time it is evaluated. This block
# prints the item. 
# [1, 2, 3, 4, 5].each { |i| puts i }

# This block prints the number 5 for each item.
# (It chooses to ignore the passed item, which is allowed.)
# [1, 2, 3, 4, 5].each { |i| puts i*5 }

# Sorting
my_array = [3, 4, 8, 7, 1, 6, 5, 9, 2]

# Call the sort! method on my_array below.
# my_array should then equal [1, 2, 3, 4, 5, 6, 7, 8, 9].
my_array.sort!
puts my_array