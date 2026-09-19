"""
Unit conversion utilities.

Provides functions for converting common measurements.
"""


def kilometers_to_miles(kilometers):
    """
    Convert kilometers to miles.

    Parameters:
        kilometers: Distance in kilometers.

    Returns:
        Distance in miles.
    """
    return kilometers * 0.621371


def miles_to_kilometers(miles):
    """
    Convert miles to kilometers.

    Parameters:
        miles: Distance in miles.

    Returns:
        Distance in kilometers.
    """
    return miles / 0.621371


def kilograms_to_pounds(kilograms):
    """
    Convert kilograms to pounds.

    Parameters:
        kilograms: Weight in kilograms.

    Returns:
        Weight in pounds.
    """
    return kilograms * 2.20462