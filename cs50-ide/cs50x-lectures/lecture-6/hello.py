from cs50 import get_string, get_float, get_int

answer = get_string("What is your name?: ")
print("Hello, " + answer)

# With formatted string
print(f"Hello, {answer}")

# Without cs50 library
answerr = input("What is your name?: ")
print(f"Hello, {answer}")

