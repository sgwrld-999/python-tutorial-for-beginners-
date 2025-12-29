# Scope in Python — Complete Notes

---

## 1. What Is Scope?

**Scope** defines the region of a program where a variable is **accessible**.

In Python, scope determines:

* Where a variable can be read
* Where it can be modified
* How name resolution works

Incorrect understanding of scope is a major source of bugs in real-world systems.

---

## 2. Python’s LEGB Rule (Very Important)

Python resolves variable names using the **LEGB order**:

1. **L – Local**
2. **E – Enclosing**
3. **G – Global**
4. **B – Built-in**

Python searches in this order and stops at the first match.

---

## 3. Local Scope

### Definition

Variables defined **inside a function** belong to the local scope of that function.

### Example

```python
def func():
    x = 10
    print(x)
```

* `x` exists only inside `func`
* Accessing `x` outside raises `NameError`

### Real-world use

Temporary variables, intermediate calculations, function internals.

---

## 4. Enclosing Scope (Nonlocal Scope)

### Definition

Variables defined in an **outer function**, accessed by an **inner function**.

### Example

```python
def outer():
    x = 5

    def inner():
        print(x)

    inner()
```

Here, `x` is in the **enclosing scope** of `inner`.

---

### Modifying Enclosing Variables: `nonlocal`

```python
def outer():
    x = 5

    def inner():
        nonlocal x
        x += 1

    inner()
    print(x)
```

Without `nonlocal`, Python treats `x` as local to `inner`.

### Production use

Closures, decorators, function factories.

---

## 5. Global Scope

### Definition

Variables defined **outside all functions** belong to the global scope.

### Example

```python
x = 10

def func():
    print(x)
```

---

### Modifying Global Variables: `global`

```python
x = 10

def update():
    global x
    x += 1
```

### Caution

Using `global` tightly couples functions to external state.

### Production guidance

Avoid modifying global state unless unavoidable (configuration, constants excluded).

---

## 6. Built-in Scope

### Definition

Contains Python’s built-in names such as:

* `len`
* `print`
* `range`
* `sum`

```python
print(len([1, 2, 3]))
```

### Danger: Shadowing Built-ins

```python
len = 10
```

This overrides the built-in `len`.

### Production impact

Shadowing built-ins causes subtle and hard-to-debug issues.

---

## 7. Scope Resolution Example (LEGB in Action)

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)

    inner()

outer()
```

Output:

```
local
```

Python finds `x` in **local scope first**.

---

## 8. Name Binding Rules (Critical Concept)

* Assignment creates a **local variable by default**
* Reading does **not**
* Python decides scope at compile time

### Common Bug

```python
x = 10

def func():
    print(x)
    x = 5
```

Raises `UnboundLocalError` because `x` is treated as local due to assignment.

---

## 9. Scope vs Lifetime

| Concept  | Meaning                            |
| -------- | ---------------------------------- |
| Scope    | Where variable is accessible       |
| Lifetime | How long variable exists in memory |

A variable may exist in memory but not be accessible.

---

## 10. Loop Scope in Python

Python **does not create block scope** for loops.

```python
for i in range(3):
    pass

print(i)
```

`i` is accessible after the loop.

### Production implication

Avoid relying on loop variables outside loops.

---

## 11. `if` Statements and Scope

```python
if True:
    x = 10

print(x)
```

Python does not create a new scope for `if`.

---

## 12. Comprehension Scope

List, set, and dict comprehensions **have their own scope** (Python 3+).

```python
x = 10
lst = [x for x in range(5)]
print(x)
```

Output:

```
10
```

---

## 13. Functions Create Scope, Classes Do Too (But Differently)

### Function Scope

```python
def f():
    x = 5
```

### Class Scope

```python
class A:
    x = 10
```

Class scope is **not part of LEGB lookup for methods**.

---

## 14. Closures and Scope

A **closure** is a function that remembers variables from its enclosing scope.

```python
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```

### Production use

* Caching
* Rate limiting
* Decorators

---

## 15. Scope and Mutable Objects

```python
lst = []

def add_item():
    lst.append(1)
```

No `global` needed because object is mutated, not reassigned.

### Reassignment requires `global`

```python
def reset():
    global lst
    lst = []
```

---

## 16. Scope in Exception Blocks

```python
try:
    x = 10
except:
    pass

print(x)
```

`x` exists after `try`.

---

## 17. Best Practices for Scope

* Prefer local variables
* Avoid global state
* Use function parameters instead of globals
* Never shadow built-ins
* Use `nonlocal` sparingly
* Keep scopes shallow

---

## 18. Common Scope Mistakes

* Assuming loops create scope
* Forgetting `nonlocal`
* Modifying globals unintentionally
* Shadowing names
* Overusing `global`

---

## 19. Real-World Production Examples

### Example: Configuration Access

```python
CONFIG = {"timeout": 5}

def connect():
    return CONFIG["timeout"]
```

Safe because CONFIG is not reassigned.

---

### Example: Buggy Global Modification

```python
count = 0

def inc():
    count += 1
```

Fails without `global`.

---

## 20. Final Summary

* Python uses **LEGB** to resolve names.
* Functions define scope; loops do not.
* Assignment determines scope at compile time.
* `global` and `nonlocal` modify binding rules.
* Correct scope usage is critical for clean, safe, production code.

---

