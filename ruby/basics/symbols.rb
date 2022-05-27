symbols = %i[hi hi hi hi hi hi hi]
numbers = [3, 4, 2, 3 ,4, 23, 4, 2]
print symbols.map(&:to_s)
print numbers.collect(&:to_s)