names = ['bob', 'joe', 'steve', nil, 'frank']

names.each do |name|
  begin
    puts "#{name}'s name has #{name.length} letters in it."
  rescue
    puts "Something went wrong!"
  end
end


# 'rescue' inline
zero = 0
puts "Before each call"
zero.each { |element| puts element } rescue puts "Can't do that!"
puts "After each call"


def divide(number, divisor)
  begin
    answer = number / divisor
  rescue ZeroDivisionError => e
    puts "There was an error! #{e.message}"
  end
end

puts divide 16, 4
puts divide 4, 0