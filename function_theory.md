# Functions in Python — Complete Notes

---

## 1. What Is a Function?

A **function** is a reusable block of code that performs a specific task.

Functions:

* Improve code reuse
* Improve readability
* Reduce duplication
* Enable modular design
* Simplify testing and maintenance

---

## 2. Defining a Function

### Syntax

```python
def function_name(parameters):
    """Docstring"""
    statements
    return value
```

* `def` defines a function
* Function name should follow `snake_case`
* Docstring describes purpose
* `return` sends a value back to the caller

---

## 3. Basic Function Example

```python
def add(a, b):
    return a + b
```

### Real-world use

* Utility functions
* Business logic
* Data transformations

---

## 4. Calling a Function

```python
result = add(5, 3)
```

---

## 5. Return Statement

### With Return

```python
def square(x):
    return x * x
```

### Without Return

```python
def log_message(msg):
    print(msg)
```

Returns `None` implicitly.

---

## 6. Multiple Return Values

```python
def get_user():
    return "Siddhant", "Engineer", "Remote"
```

Actually returns a **tuple**.

### Production use

* Returning related data without creating objects

---

## 7. Function Parameters and Arguments

---

### 7.1 Positional Arguments

```python
def greet(name, role):
    print(name, role)
```

Order matters.

---

### 7.2 Keyword Arguments

```python
greet(role="Engineer", name="Siddhant")
```

Order does not matter.

---

### 7.3 Default Arguments

```python
def connect(timeout=5):
    pass
```

### Best practice

Never use mutable defaults (`list`, `dict`).

---

### 7.4 Variable-Length Arguments

#### `*args` (Tuple)

```python
def sum_all(*args):
    return sum(args)
```

Used when number of inputs is unknown.

---

#### `**kwargs` (Dictionary)

```python
def build_profile(**kwargs):
    return kwargs
```

Used for flexible configuration.

---

## 8. Parameter Order (Important)

Correct order:

```python
def func(positional, default=1, *args, **kwargs):
    pass
```

Incorrect order raises syntax error.

---

## 9. Scope and Lifetime

---

### Local Scope

Variables inside function.

```python
def f():
    x = 10
```

---

### Global Scope

```python
x = 5
```

---

### `global` Keyword

```python
def update():
    global x
    x = 10
```

Avoid in production unless absolutely necessary.

---

## 10. Nested Functions

```python
def outer():
    def inner():
        print("Inner")
    inner()
```

Used in decorators and closures.

---

## 11. Closures

```python
def multiplier(x):
    def inner(y):
        return x * y
    return inner
```

### Production use

* Caching
* Function factories
* Decorators

---

## 12. Lambda Functions

Anonymous, single-expression functions.

```python
add = lambda a, b: a + b
```

### Use cases

* Sorting
* Filtering
* Short transformations

Avoid complex logic.

---

## 13. Higher-Order Functions

Functions that accept or return functions.

```python
def apply(func, x):
    return func(x)
```

---

## 14. Common Built-in Higher-Order Functions

### `map()`

```python
map(func, iterable)
```

### `filter()`

```python
filter(func, iterable)
```

### `reduce()`

```python
from functools import reduce
```

Used sparingly in production.

---

## 15. Recursion

A function calling itself.

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

### Risks

* Stack overflow
* Slower than loops

Use when recursion fits naturally.

---

## 16. Function Annotations (Type Hints)

```python
def add(a: int, b: int) -> int:
    return a + b
```

### Production use

* Static analysis
* IDE support
* Documentation

---

## 17. Docstrings

```python
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b
```

Used by tools like Sphinx.

---

## 18. Pure vs Impure Functions

### Pure Function

* No side effects
* Same input → same output

```python
def square(x):
    return x * x
```

### Impure Function

* Modifies state or external data

---

## 19. Error Handling in Functions

```python
def safe_divide(a, b):
    if b == 0:
        return None
    return a / b
```

Or with exceptions:

```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None
```

---

## 20. Performance Considerations

* Functions have call overhead
* Small functions improve clarity
* Avoid deep recursion
* Avoid unnecessary global state

---

## 21. Best Practices

* One function = one responsibility
* Use descriptive names
* Keep functions small
* Avoid side effects
* Document behaviour clearly
* Use type hints

---

## 22. When to Use Functions in Production

* Business logic separation
* API handlers
* Data transformation pipelines
* Validation logic
* Reusable utilities
* Testing and mocking

---

## 23. Common Mistakes

* Mutable default arguments
* Overloaded functions with too many responsibilities
* Excessive parameters
* Hidden side effects
* Lack of documentation

---

## 24. Final Summary

* Functions are the backbone of Python programs.
* They enable modular, readable, testable code.
* Understanding parameters, scope, and return behaviour is critical.
* Clean function design directly impacts production code quality.

---