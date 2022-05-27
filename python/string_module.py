import string

# String constants
# ASCII American Standard Code for Information Interchange
# They are basically strings that contain a certain type of characters

print(string.ascii_letters)
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

print(string.digits)
# '0123456789'


# Check membership
user_input = input('Enter one digit: ')  # '5'

print(user_input in string.digits)  # True



# * The helper function
# ? syntax
# string.capwords(s, sep)
my_str = "the string i want to capitalize"
print(string.capwords(my_str))  # 'The String I Want To Capitalize'

my_other_str = "another,string,i,want,to,capitalize"

print(string.capwords(my_other_str, sep=","))  # 'Another,String,I,Want,To,Capitalize'
print(string.capwords(my_other_str))  # 'Another,string,i,want,to,capitalize'


# Formatting
# the Formatter class https://docs.python.org/3/library/string.html

# Template Strings
my_template = string.Template("Hello, $name!")
my_str = my_template.substitute(name="Jack")
print(my_str)  # 'Hello, Jack!'



name = input()
template = string.Template("Dear $username! It was really nice to meet you. "
                           "Hopefully, you have a nice day! See you soon, $username!"
    )
print(template.substitute(username=name))
