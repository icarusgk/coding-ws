my_hash = {
  "name" => "Eric",
  "age" => 26,
  "hungry?" => true,
}

puts my_hash["name"]
puts my_hash["age"]
puts my_hash["hungry?"]

# Initializing an empty hash
pets = Hash.new
pets["tyke"] = "cat"

puts pets["tyke"]

s = [["ham", "swiss"], ["turkey", "cheddar"], ["roast beef", "gruyere"]]

s.each do |arr| arr.each do |l| puts l end end

secret_identities = {
  "The Batman" => "Bruce Wayne",
  "Superman" => "Clark Kent",
  "Wonder Woman" => "Diana Prince",
  "Freakazoid" => "Dexter Douglas",
}

secret_identities.each do |hero, name| puts "#{hero}: #{name}" end

puts "Text please: "
text = gets.chomp

words = text.split(" ")

frequencies = Hash.new(0)

words.each { |word| frequencies[word] += 1 }
frequencies = frequencies.sort_by { |a, b| b }
frequencies.reverse!
frequencies.each { |word, frequency| puts word + " " + frequency.to_s }

# New hash syntax
movie_ratings = {
  memento: 3,
  primer: 3.5,
  the_matrix: 5,
  truman_show: 4,
  red_dawn: 1.5,
  skyfall: 4,
  alex_cross: 2,
  uhf: 1,
  lion_king: 3.5,
}
# Select
good_movies = movie_ratings.select do |movie, score| score > 3 end

# Just keys and just values

my_hash = { one: 1, two: 2, three: 3 }

my_hash.each_key { |k| print k, " " }
# ==> one two three

my_hash.each_value { |v| print v, " " }
# ==> 1 2 3
