#!/usr/bin/ruby
person = "icarus.gk".to_sym
place = :cinepolis

def farewell(person)
  "Until next time! See ya #{person}"
end

puts "Last night I went to the movies with #{person}"
puts "We had a great time"
puts "We went to #{place}"

puts farewell person

