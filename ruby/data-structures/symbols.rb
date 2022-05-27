strings = ["HTML", "CSS", "JavaScript", "Python", "Ruby"]
symbols = []

# Add your code below!
strings.each do |s| symbols.push(s.to_sym) end
# strings.each do |s| symbols.push(s.intern) end

puts symbols

movies = {
  end_game: "marvel",
  joker: "DC"
}

puts movies[:end_game]
