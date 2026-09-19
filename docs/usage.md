# Usage

The Automated Documentation Demo contains a simple Python calculator with four basic arithmetic operations.

## Importing the Calculator

The functions can be imported from the `calculator` module:

```python
from src.calculator import add, subtract, multiply, divide
```

## Addition

The `add()` function adds two numbers.

```python
result = add(10, 5)
print(result)
```

Output:

```text
15
```

### Syntax

```python
add(a, b)
```

* `a` — First number
* `b` — Second number
* Returns the sum of the two numbers

---

## Subtraction

The `subtract()` function subtracts the second number from the first.

```python
result = subtract(10, 5)
print(result)
```

Output:

```text
5
```

### Syntax

```python
subtract(a, b)
```

* `a` — First number
* `b` — Second number
* Returns the difference between the two numbers

---

## Multiplication

The `multiply()` function multiplies two numbers.

```python
result = multiply(10, 5)
print(result)
```

Output:

```text
50
```

### Syntax

```python
multiply(a, b)
```

* `a` — First number
* `b` — Second number
* Returns the product of the two numbers

---

## Division

The `divide()` function divides the first number by the second.

```python
result = divide(10, 5)
print(result)
```

Output:

```text
2.0
```

### Syntax

```python
divide(a, b)
```

* `a` — Numerator
* `b` — Denominator
* Returns the division result as a float

### Division by Zero

The function prevents division by zero.

```python
result = divide(10, 0)
```

This raises:

```text
ValueError: Cannot divide by zero.
```

---

## Example Program

The following example uses all four operations:

```python
from src.calculator import add, subtract, multiply, divide

a = 20
b = 5

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Multiplication:", multiply(a, b))
print("Division:", divide(a, b))
```

Output:

```text
Addition: 25
Subtraction: 15
Multiplication: 100
Division: 4.0
```

## Technical Documentation

Detailed documentation for the calculator's functions, parameters, return values, and exceptions is generated automatically using **Doxygen**.

[View Technical Documentation](doxygen/html/index.html)
