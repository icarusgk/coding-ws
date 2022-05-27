import argparse

parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")


parser.add_argument('-i1', '--ingredient_1')

# For action = "store_false": the default value is True.
# For action = "store_true": the default value is False.
parser.add_argument("--salt", action="store_true")

# The same can be achieved by specifying the default parameter:
parser.add_argument("--pepper", default=False)

# the choices parameter that will show the acceptable values for 
# a particular argument
parser.add_argument("-i2", "--ingredient_2",
                    choices=["pasta", "rice", "potato", "onion",
                             "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

# The parse_args() method is used for reading argument strings 
# from the command line:
args = parser.parse_args()


# Now we can access the values specified by a user as attributes of the args. 
# The long versions are used as attribute names:

print(args.ingredient_2)  # onion 

# In case a user didn't specify an optional argument in the command line, 
# the value is set toNone by default:
print(args.ingredient_3)  # None

print(args)