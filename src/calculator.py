"""
Calculator module.

Provides basic arithmetic operations.
"""


def add(a, b):
    """
    Add two numbers.

    Parameters:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: Sum of the two numbers.
    """
    return a + b


def subtract(a, b):
    """
    Subtract the second number from the first.

    Parameters:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: Difference between the two numbers.
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.

    Parameters:
        a (int | float): First number.
        b (int | float): Second number.

    Returns:
        int | float: Product of the two numbers.
    """
    return a * b


def divide(a, b):
    """
    Divide the first number by the second.

    Parameters:
        a (int | float): Numerator.
        b (int | float): Denominator.

    Returns:
        float: Result of the division.

    Raises:
        ValueError: If the denominator is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b
