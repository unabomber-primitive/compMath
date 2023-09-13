import math

def first_function(x: float):
    return 1 / x


def second_function(x: float):
    return math.sin(x)/x


def third_function(x: float):
    return x*x+2


def fourth_function(x: float):
    return 2*x+2


def five_function(x: float):
    return math.log(x)

def print_functions():
    print("""
          1. 1/x
          2. sin(x)/x
          3. x^2+2
          4. 2x+2
          5. log(x)
          """)

# How to use this function:
# func = Result.get_function(4)
# func(0.01)
def get_function(n: int):
    if n == 1:
        return first_function
    elif n == 2:
        return second_function
    elif n == 3:
        return third_function
    elif n == 4:
        return fourth_function
    elif n == 5:
        return five_function
    else:
        raise NotImplementedError(f"Function {n} not defined.")
