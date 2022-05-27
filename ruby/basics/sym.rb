number_icarus = 442

my_js = {
  first: number_icarus,
  balance: 49
}


# def say_name(name)
#   puts name
# end

def say_hash(hash)
  hash.each do |k, v| puts "#{k}: #{v}" end
end

# say_name "Roger"
# say_hash my_js

# puts my_js

name = :"icarus.gk"
my_other_name = :"icarus.gk"
my_secret_name = :"icarus.gk"

puts name.object_id
puts my_secret_name.object_id
puts my_other_name.object_id

puts Symbol.all_symbols.find_index(:say_hash) # 3202
puts Symbol.all_symbols.at 3202 # say_hash


my_requests = [:get, :post, :put, :delete]

request = :get

puts request if my_requests.include? request
