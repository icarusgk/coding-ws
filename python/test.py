def f1(x):
    return pow(x, 2) + 1


def f2(x):
    return 1 / pow(x, 2)


def f3(x):
    return 2


def f(x):
    if x <= 0:
        return f1(x)
    elif 0 < x < 1:
        return f2(x)
    else:
        return f3(x)

print(f(1))


def calculate(amount, interest_rate, time):
    interest = (amount * interest_rate * time) / 100
    total_amount = amount + interest
    return interest, total_amount

def print_result(interest):
    print(f'The interest is: {interest}')
    print(f'The total amount is: {total_amount}')