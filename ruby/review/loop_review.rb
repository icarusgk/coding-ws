i = 0
loop do
  i = i + 1
  if i == 4
    next
  end
  puts i
  if i == 10
    break
  end
end


# do while

loop do
  puts "Again?"
  answer = gets.chomp

  if answer != 'y'
    break
  end
end

# for loops

# Recursion
def fibonacci(number)
  if number < 2
    number
  else
    fibonacci(number - 1) + fibonacci(number - 2)
  end
end

puts fibonacci 6

def count_to_zero(number)
  if number <= 0
    puts number
  else
    puts number
    count_to_zero(number - 1)
  end
end

count_to_zero(30)