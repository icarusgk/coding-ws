# If we want our program to stop working when something goes wrong, we can use the raise keyword for the Exception class when a condition is met.

def example_exceptions_1(x, y):
    if y == 0:
        raise ZeroDivisionError("The denominator is 0! Try again, please!")
    elif y < 0:
        raise Exception("The denominator is negative!")
    else:
        print(x / y)


class NegativeResultError(Exception):
  print("Horray! My first exception is working!")

def example_exceptions_2(a, b):
    try:
        c = a / b
        if c < 0:
            raise NegativeResultError
        else:
            print(c)
    except NegativeResultError:
        print("There is a negative result!")


example_exceptions_2(2, 5)   # 0.4
example_exceptions_2(2, -5)  # There is a negative result!


class NotInBoundsError(Exception):
    def __str__(self):
        return "Wrong!"


def example_exceptions_4(num):
    try:
        if not 57 < num < 150:
            raise NotInBoundsError
        else:
            print(num)
    except NotInBoundsError as err:
        print(err)



example_exceptions_4(46)  # Wrong!
example_exceptions_4(58)  # 58



class LessThanFiveHundredError(Exception):
    def __init__(self, num):
        self.message = "The integer %s is below 500!" % str(num)
        super().__init__(self.message)


def example_exceptions_5(num):
    if num < 500:
        raise LessThanFiveHundredError(num)
    else:
        print(num)