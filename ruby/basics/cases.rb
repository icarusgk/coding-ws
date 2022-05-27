movies = {
  joker: 9.7
}

puts "Enter a choice: "
choice = gets.chomp

case choice
  when "add"
    puts "Enter movie title: "
    title = gets.chomp

    puts "Enter movie's rating: "
    rating = gets.chomp

    if movies[title.to_sym] == nil
      movies[title.to_sym] = rating.to_i
      puts "Your movie has been added"
    else
      puts "This movie already exists"
    end
  when "update"
    puts "Enter the title of the movie you want to update"
    title = gets.chomp

    if movies[title.to_sym] == nil
      puts "This movie doesn't exists"
    else
      puts "Enter #{title}'s rating: "
      rating = gets.chomp
      movies[title.to_sym] = rating.to_i
      puts "The movie's rating has been updated"
    end
  when "display"
    movies.each do |movie, rating| puts "#{movie}: #{rating}\n" end
  when "delete"
    puts "Enter the movie's title you wish to delete: "
    title = gets.chomp

    if movies[title.to_sym] == nil
      puts "This movie doesn't exists"
    else
      movies.delete(title.to_sym)
      puts "#{title} has been deleted"
    end
  else
    puts "Error!"
end

# Shorthand

puts "Hello there!"
greeting = gets.chomp

# Add your case statement below!
case greeting
  when "English" then puts "Hello!"
  when "French" then puts "Bonjour!"
  when "German" then puts "Guten Tag!"
  when "Finnish" then puts "Haloo!"
  else puts "I don't know that language!"
end