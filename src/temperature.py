

def kelvin_to_celsius(kelvin):
  """
  Convert Kelvin to Celsius.
  
  Parameters:
  kelvin: Temperature in Kelvin.
  
  Returns:
  Temperature in Celsius.
  """
  return kelvin - 273.15

def celsius_to_fahrenheit(celsius: float) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius: Temperature in degrees Celsius.

    Returns:
        The equivalent temperature in degrees Fahrenheit.

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
    """
    return (celsius * 9 / 5) + 32