# Loops in Python — Complete Notes

---

## 1. What Is a Loop?

A **loop** is a control structure that allows a block of code to be executed **repeatedly** until a condition is met or a sequence is exhausted.

Loops are fundamental for:

* Iteration over data
* Automation
* Repetition of tasks
* Traversing collections
* Implementing algorithms

Python primarily provides:

* `for` loop
* `while` loop

---

## 2. `for` Loop

### Definition

A `for` loop iterates over **any iterable object**.

Iterables include:

* list
* tuple
* string
* set
* dictionary
* range
* generators

### Syntax

```python
for variable in iterable:
    statement
```

---

## 3. Basic `for` Loop Example

```python
names = ["A", "B", "C"]

for name in names:
    print(name)
```

### Real-world use

* Processing user records
* Iterating database query results
* Handling API response lists

---

## 4. Looping with `range()`

### `range()` Basics

```python
range(start, stop, step)
```

* `start` → inclusive
* `stop` → exclusive
* `step` → increment (default = 1)

### Examples

```python
for i in range(5):
    print(i)
```

```python
for i in range(1, 10, 2):
    print(i)
```

### Real-world use

* Looping fixed number of times
* Index-based iteration
* Pagination logic

---

## 5. Looping with Index: `enumerate()`

```python
names = ["A", "B", "C"]

for index, value in enumerate(names):
    print(index, value)
```

### Why use `enumerate()`?

* Avoids manual counter
* Cleaner and safer

### Production use

* Logging
* Displaying indexed items
* Debugging pipelines

---

## 6. Looping Over Dictionaries

```python
data = {"name": "Siddhant", "role": "Engineer"}

for key in data:
    print(key)

for value in data.values():
    print(value)

for key, value in data.items():
    print(key, value)
```

### Best practice

Use `.items()` when both key and value are needed.

---

## 7. Looping Over Strings

```python
word = "Python"

for char in word:
    print(char)
```

### Use case

* Parsing
* Validation
* Tokenisation

---

## 8. `while` Loop

### Definition

A `while` loop continues executing **as long as the condition is `True`**.

### Syntax

```python
while condition:
    statement
```

---

## 9. Basic `while` Loop Example

```python
count = 0

while count < 5:
    print(count)
    count += 1
```

### Real-world use

* Reading streams
* Polling APIs
* Retry mechanisms
* Event loops

---

## 10. Infinite Loops

```python
while True:
    pass
```

Used intentionally with `break`.

### Production use

* Server listeners
* Daemons
* Event-driven systems

⚠️ Must always have an exit strategy.

---

## 11. Loop Control Statements

---

### `break`

Terminates the loop immediately.

```python
for i in range(10):
    if i == 5:
        break
```

**Use case:** Stop when condition is met (search, validation).

---

### `continue`

Skips current iteration.

```python
for i in range(5):
    if i == 2:
        continue
    print(i)
```

**Use case:** Ignore invalid or unwanted data.

---

### `pass`

Does nothing.

```python
for i in range(5):
    pass
```

**Use case:** Placeholder for future logic.

---

## 12. `else` with Loops (Important but Overlooked)

### `for-else`

```python
for i in range(5):
    if i == 10:
        break
else:
    print("Loop completed normally")
```

`else` executes **only if loop was not terminated by `break`**.

### Real-world use

* Search operations
* Validation checks

---

## 13. Nested Loops

```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

### Real-world use

* Matrix operations
* Grid traversal
* Combinatorial problems

⚠️ Performance can degrade quickly.

---

## 14. Looping with Multiple Iterables: `zip()`

```python
names = ["A", "B"]
scores = [90, 85]

for name, score in zip(names, scores):
    print(name, score)
```

### Production use

* Merging parallel datasets
* Data alignment

---

## 15. List Comprehension (Loop Shortcut)

```python
squares = [x*x for x in range(5)]
```

Equivalent to:

```python
squares = []
for x in range(5):
    squares.append(x*x)
```

### When to use

* Simple transformations
* Filtering

⚠️ Avoid for complex logic.

---

## 16. Set and Dictionary Comprehensions

```python
unique = {x for x in range(10)}
mapping = {x: x*x for x in range(5)}
```

Used in data pipelines and transformations.

---

## 17. Loop Performance Considerations

| Scenario          | Recommendation                 |
| ----------------- | ------------------------------ |
| Membership check  | Use `set`, not loop            |
| Large datasets    | Avoid nested loops             |
| Simple transform  | Use comprehension              |
| Heavy computation | Consider vectorisation (NumPy) |

---

## 18. Common Loop Mistakes

* Forgetting to update loop variable (`while`)
* Modifying list while iterating
* Using `range(len(list))` instead of direct iteration
* Infinite loops
* Deeply nested loops without optimisation

---

## 19. When to Use Which Loop

| Use Case                   | Loop Type       |
| -------------------------- | --------------- |
| Known number of iterations | `for`           |
| Condition-based repetition | `while`         |
| Searching                  | `for` + `break` |
| Streaming data             | `while`         |
| Data transformation        | Comprehension   |

---

## 20. Production Examples

### Example 1: Validate Records

```python
for user in users:
    if not user["email"]:
        continue
    process(user)
```

---

### Example 2: Retry Logic

```python
retries = 3

while retries > 0:
    if connect():
        break
    retries -= 1
```

---

## 21. Final Summary

* Loops automate repetition.
* `for` loops iterate over iterables.
* `while` loops depend on conditions.
* Control statements (`break`, `continue`, `else`) refine flow.
* Comprehensions provide concise loop-based transformations.
* Efficient loop usage is critical for performance in production systems.

---
