# frozen_string_literal: true

module Classes3
  class Neighbor
    attr_accessor :name, :people_count

    def initialize(name, people_count)
      @name = name
      @people_count = people_count
    end
  end
end

