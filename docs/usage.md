# Usage

This page describes the available functions and classes in **Auto Documentation Demo**.

## `src/calculator.py`

Calculator module. Provides basic arithmetic operations.

### `add()`

Add two numbers. Parameters: a (int | float): First number. b (int | float): Second number. Returns: int | float: Sum of the two numbers.

**Parameters:**

- `a`
- `b`

**Example:**

```python
add(value, value)
```

### `subtract()`

Subtract the second number from the first. Parameters: a (int | float): First number. b (int | float): Second number. Returns: int | float: Difference between the two numbers.

**Parameters:**

- `a`
- `b`

**Example:**

```python
subtract(value, value)
```

### `multiply()`

Multiply two numbers. Parameters: a (int | float): First number. b (int | float): Second number. Returns: int | float: Product of the two numbers.

**Parameters:**

- `a`
- `b`

**Example:**

```python
multiply(value, value)
```

### `divide()`

Divide the first number by the second. Parameters: a (int | float): Numerator. b (int | float): Denominator. Returns: float: Result of the division. Raises: ValueError: If the denominator is zero.

**Parameters:**

- `a`
- `b`

**Example:**

```python
divide(value, value)
```

## `src/temperature.py`

### `kelvin_to_celsius()`

Convert Kelvin to Celsius. Parameters: kelvin: Temperature in Kelvin. Returns: Temperature in Celsius.

**Parameters:**

- `kelvin`

**Example:**

```python
kelvin_to_celsius(value)
```

### `celsius_to_fahrenheit()`

Convert a temperature from Celsius to Fahrenheit. Args: celsius: Temperature in degrees Celsius. Returns: The equivalent temperature in degrees Fahrenheit. Examples: >>> celsius_to_fahrenheit(0) 32.0 >>> celsius_to_fahrenheit(100) 212.0

**Parameters:**

- `celsius`

**Example:**

```python
celsius_to_fahrenheit(value)
```

---

For detailed API information, see the automatically generated Doxygen documentation.
