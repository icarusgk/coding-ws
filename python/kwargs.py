# * **kwargs collects all possible extra values in a dictionary with keywords as keys.

def capital(**kwargs):
    for key, value in kwargs.items():
        print(value, "is the capital city of", key)


capital(Canada="Ottawa", Estonia="Tallinn", Venezuela="Caracas", Finland="Helsinki")

# Ottawa is the capital city of Canada
# Tallinn is the capital city of Estonia
# Caracas is the capital city of Venezuela
# Helsinki is the capital city of Finland


def func(positional_args, defaults, *args, **kwargs):
    pass

def say_bye(**names):
    for name in names:
        print("Au revoir,", name)
        print("See you on", names[name]["next appointment"])
        print()


humans = {"Laura": {"next appointment": "Tuesday"},
          "Robin": {"next appointment": "Friday"}}

say_bye(**humans)

# Au revoir, Laura
# See you on Tuesday
# 
# Au revoir, Robin
# See you on Friday