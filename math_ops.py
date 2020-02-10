import math
def is_prime(n : str):
    try:
        number = int(n)
    except ValueError:
        return "input is not an integer"
    # Corner cases
    if (number <= 1):
        return False
    if (number <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (number % 2 == 0 or number % 3 == 0):
        return False

    i = 5
    while (i * i <= number):
        if (number % i == 0 or number % (i + 2) == 0):
            return False
        i = i + 6

    return True

def factorial(n: str):
    try:
        number = int(n)
        factorial_res = math.factorial(number)
    except ValueError:
        return "input either not an integer or negative number"
    return factorial_res

def is_palindrome(n : str):
    try:
        number = int(n)
    except ValueError:
        return "input is not an integer"
    val = str(number)
    return val == val[::-1]

def is_sqrt(n: str):
    try:
        number = int(n)
        sqrt_res = math.sqrt(number)
    except ValueError:
        return "input either not an integer or negative number"
    return sqrt_res.is_integer()

