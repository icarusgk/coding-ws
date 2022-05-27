# Combined Comparison Operator
# The combined comparison operator looks like this: <=>. 
# It returns 0 if the first operand (item to be compared) equals the second, 
# 1 if the first operand is greater than the second, 
# and -1 if the first operand is less than the second.

books = ["Charlie and the Chocolate Factory", "War and Peace", "Utopia", "A Brief History of Time", "A Wrinkle in Time"]

# To sort our books in ascending order, in-place
books.sort! { |firstBook, secondBook| firstBook <=> secondBook }

# Sort your books in descending order, in-place below
books.sort! { |firstBook, secondBook| secondBook <=>  firstBook }

fruits = ["orange", "apple", "banana", "pear", "grapes"]

fruits.sort! do |firstFruit, secondFruit| secondFruit <=> firstFruit end