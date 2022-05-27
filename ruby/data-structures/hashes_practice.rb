# frozen_string_literal: true

name = 'Roger'

my_hash = {
  name: name,
  handle: '@icarus.gk',
  age: 21,
  languages: %w[python ruby]
}

my_hash['pet'.to_sym] = 'tyke'

my_hash.each do |k, v| puts "#{k}: #{v}" end

%w[hi hi hi hi tel asdjkf asdf asdf asdf]



