person = {
  name: "roger",
  hair: "black",
  weight: 55,
  height: "1.81 m"
}

# Iterating over an array
person.each do |k, v|
  puts "Roger's #{k} is #{v}"
end

puts person.fetch :name
print person.to_a