# Closures in Python — Complete Notes

---

## 1. What Is a Closure?

A **closure** is a function object that **remembers values from its enclosing (non-local) scope**, even after the outer function has finished execution.

In simple terms:

> A closure allows a function to “carry state” without using global variables or classes.

---

## 2. Why Closures Exist

Closures solve problems where you need:

* State preservation
* Function customisation
* Encapsulation without classes
* Behaviour configured at runtime

They are a fundamental building block for decorators, callbacks, and functional patterns.

---

## 3. Basic Closure Example

```python
def outer():
    x = 10

    def inner():
        print(x)

    return inner
```

```python
f = outer()
f()
```

### What happens?

* `outer()` finishes execution
* `x` should normally disappear
* But `inner()` **retains access to `x`**

This retention of `x` is the closure.

---

## 4. How Closures Work Internally

A closure consists of:

1. A **nested function**
2. A **non-local variable**
3. A **reference** to that variable stored in the function object

You can inspect it:

```python
print(f.__closure__)
```

Each cell contains captured variables.

---

## 5. Enclosing vs Global Scope

Closures capture **enclosing scope**, not global scope.

```python
x = 100

def outer():
    x = 10
    def inner():
        print(x)
    return inner
```

Output is `10`, not `100`.

---

## 6. Modifying Enclosing Variables: `nonlocal`

By default, closure variables are **read-only**.

```python
def outer():
    x = 5
    def inner():
        x += 1   # Error
```

Fix using `nonlocal`:

```python
def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        return x
    return inner
```

---

## 7. Closure vs Global Variables

| Aspect        | Closure | Global     |
| ------------- | ------- | ---------- |
| Scope         | Limited | Everywhere |
| Safety        | High    | Low        |
| Encapsulation | Yes     | No         |
| Testability   | High    | Low        |

**Production rule:** Prefer closures over globals.

---

## 8. Closures with Parameters (Function Factories)

```python
def power(n):
    def inner(x):
        return x ** n
    return inner
```

```python
square = power(2)
cube = power(3)
```

### Real-world use

* Configurable logic
* Strategy patterns
* Reusable transformations

---

## 9. Closures in Loops (Common Pitfall)

```python
funcs = []

for i in range(3):
    def f():
        print(i)
    funcs.append(f)
```

All functions print `2`.

### Why?

Closures capture **variables, not values**.

### Fix: Bind value explicitly

```python
for i in range(3):
    def f(i=i):
        print(i)
```

---

## 10. Closures and Mutable Objects

```python
def collector():
    items = []
    def add(x):
        items.append(x)
        return items
    return add
```

No `nonlocal` required because list is mutated, not reassigned.

---

## 11. Closures vs Classes

| Feature    | Closure           | Class             |
| ---------- | ----------------- | ----------------- |
| State      | Captured variable | Instance variable |
| Complexity | Low               | Higher            |
| Mutability | Controlled        | Explicit          |
| Use case   | Simple state      | Complex behaviour |

**Rule:**
Use closures for **simple state**, classes for **complex state and behaviour**.

---

## 12. Closures and Decorators

Decorators are **closures wrapping functions**.

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print("Calling", func.__name__)
        return func(*args, **kwargs)
    return wrapper
```

Decorator uses closure to retain reference to `func`.

---

## 13. Closures in Production Systems

### Common Uses

* Logging
* Authentication checks
* Caching
* Rate limiting
* Retry logic
* Feature flags

---

### Example: Simple Cache

```python
def cache():
    store = {}
    def get(key):
        return store.get(key)
    def set(key, value):
        store[key] = value
    return get, set
```

Encapsulates state safely.

---

## 14. Performance Considerations

* Closure variable access is slightly slower than local access
* Faster and lighter than class instantiation
* Minimal memory overhead

Performance impact is negligible in most applications.

---

## 15. Garbage Collection and Closures

Captured variables are kept alive as long as the closure exists.

### Risk

Large objects captured unintentionally can cause memory retention.

**Best practice:** Capture only what is needed.

---

## 16. Debugging Closures

Inspect closure variables:

```python
func.__closure__
func.__code__.co_freevars
```

Useful when diagnosing unexpected behaviour.

---

## 17. Common Closure Mistakes

* Forgetting `nonlocal`
* Late binding in loops
* Overusing closures for complex logic
* Capturing large objects
* Confusing closure with global scope

---

## 18. When NOT to Use Closures

* Complex state machines
* Long-lived mutable state with many operations
* Public APIs requiring clarity
* Situations better modelled by classes

---

## 19. Mental Model

> A closure is a function + remembered environment.

If you can explain:

* Where the variable is defined
* Who owns it
* How long it lives

Then you understand closures.

---

## 20. Final Summary

* Closures allow functions to retain state.
* They rely on enclosing scope, not global scope.
* `nonlocal` enables modification of captured variables.
* Closures are foundational for decorators and functional patterns.
* Correct use leads to clean, safe, testable code.

---

