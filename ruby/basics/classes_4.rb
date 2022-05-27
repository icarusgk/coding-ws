# frozen_string_literal: true

require './classes_3'

class Ng < Classes3::Neighbor

end

nbb = Ng.new('sosa', 412)

puts nbb.name, nbb.people_count
