puts "Enter text: "
text = gets.chomp

# Array
words = text.split(" ")

# Default value
frequencies = Hash.new(0)

# So we can increment later here
words.each do |word|
  frequencies[word] += 1
end

frequencies = frequencies.sort_by do |color, count| count end
# Reverse the hash so the greatest turns out on top
frequencies.reverse!

frequencies.each do |word, count| puts "#{word} #{count}" end

