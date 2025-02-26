"""Module providing simple math and greeting functions."""

def add(a, b):
    """
    Add two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    return a + b

def multiply(x, y):
    """
    Multiply two numbers.

    Args:
        x (int or float): The first number.
        y (int or float): The second number.

    Returns:
        int or float: The product of x and y.
    """
    return x * y

def divide(x, y):
    """
    Divide x by y.

    Args:
        x (int or float): The numerator.
        y (int or float): The denominator.

    Returns:
        float: The result of x / y if y != 0.
        None: If y == 0 (division by zero case).
    """
    if y != 0:
        return x / y
    return None

def greet(name):
    """
    Return a greeting message.

    Args:
        name (str): The name to greet.

    Returns:
        str: A greeting string. If name is empty, returns "Hello, World!".
    """
    if name == "":
        return "Hello, World!"
    return "Hello, " + name
