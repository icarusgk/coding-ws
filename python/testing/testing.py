# * assert

# 1
word = input("Enter a word: ")
# 'dog' != 'cat'
assert word != 'cat'
print("Your word is", word)


# 2
word = input("Enter a word: ")
message = "'cat' is the wrong word!"
assert word != "cat", message
print("Your word is", word)


# You can handle the AssertionError with a try and catch
try:
    word = input('Enter a word: ')
    message = "'cat' is a wrong word!"
    assert word != "cat", message
    print("Your word is", word)
except AssertionError as err:
    print(err)  # 'cat' is a wrong word!


# the "assert" keyword can be used with function
def test_mark(i):
    err_message = "This student got a bad mark!"
    assert i > 4, err_message
    return i


print(test_mark(5))  # 5
print(test_mark(2))  # Error


# * Assert vs Raise
# the keyword raise is used for raising an exception
# assert is used for raising an exception if the given condition is False

word = input('Enter a word: ')
if word != 'cat':
    print(word)
else:
    raise Exception('There is a wrong word!')

# As you can see, the raise keyword together with the if-else statement is very similar
# to the "assert" keyword, but their purposes are different. In the first case,
# raise is used mainly for data validation, while assert is used for debugging.





