
# Python Dictionaries and Sets — Complete Notes

---

## PART 1: DICTIONARIES (`dict`)

---

## 1. What Is a Dictionary?

A **dictionary** is a built-in Python data structure that stores data as **key–value pairs**.

* Keys are **unique** and **immutable**
* Values can be of **any data type**
* Dictionaries are **mutable**
* Dictionaries are **unordered conceptually**, but **preserve insertion order** (Python 3.7+)

### Syntax

```python
my_dict = {
    "name": "Siddhant",
    "status": "Placed",
    "salary": 60000
}
```

---

## 2. Key Characteristics

| Property         | Dictionary        |
| ---------------- | ----------------- |
| Ordered          | Yes (Python 3.7+) |
| Mutable          | Yes               |
| Indexed by       | Keys              |
| Duplicate keys   | Not allowed       |
| Duplicate values | Allowed           |

---

## 3. Keys: Rules and Constraints

### Valid keys:

* `int`
* `float`
* `str`
* `tuple` (only if elements are immutable)

### Invalid keys:

* `list`
* `set`
* `dict`

Reason: **Keys must be hashable (immutable)**.

---

## 4. Accessing Values

### Using Key

```python
salary = my_dict["salary"]
```

Raises `KeyError` if key does not exist.

### Using `.get()` (Safer)

```python
salary = my_dict.get("salary")
salary = my_dict.get("bonus", 0)
```

**Production use:** Prevents crashes in APIs, config parsing, JSON handling.

---

## 5. Adding and Updating Elements

### Add / Update

```python
my_dict["location"] = "Remote"
my_dict["salary"] = 70000
```

Same syntax for both adding and updating.

**Real-world use:** Updating user profiles, modifying configuration settings.

---

## 6. Removing Elements

### `pop()`

```python
my_dict.pop("salary")
```

Removes key and returns value.

### `del`

```python
del my_dict["location"]
```

### `popitem()`

```python
my_dict.popitem()
```

Removes **last inserted key–value pair**.

**Production use:** LRU caches, stack-like behaviour.

---

## 7. Dictionary Methods (Important)

### Keys, Values, Items

```python
my_dict.keys()
my_dict.values()
my_dict.items()
```

Returns **view objects**, not lists.

**Use case:** Iteration, serialization, validation.

---

### Update

```python
my_dict.update({"bonus": 10000, "role": "Engineer"})
```

Merges dictionaries.

**Production use:** Updating configs, merging request payloads.

---

### Clear

```python
my_dict.clear()
```

Removes all elements.

---

## 8. Iterating Over Dictionaries

```python
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)
```

**Preferred:** `.items()` for clarity and performance.

---

## 9. Dictionary Comprehension

```python
squared = {x: x*x for x in range(5)}
```

**Production use:** Transforming datasets, mapping IDs to values.

---

## 10. Nested Dictionaries

```python
employee = {
    "name": "Siddhant",
    "job": {
        "role": "Engineer",
        "mode": "Remote"
    }
}
```

**Real-world use:** JSON responses, APIs, databases, configs.

---

## 11. Performance Characteristics

| Operation     | Time Complexity |
| ------------- | --------------- |
| Access        | O(1)            |
| Insert        | O(1)            |
| Delete        | O(1)            |
| Search by key | O(1)            |

Reason: Hash table implementation.

---

## 12. When to Use Dictionaries in Production

* API responses (JSON)
* Configuration management
* User profiles
* Caches
* Fast lookups by ID
* Mapping relationships (ID → object)

---

---

## PART 2: SETS (`set`)

---

## 13. What Is a Set?

A **set** is an unordered collection of **unique elements**.

* No duplicates
* Mutable
* Unordered
* Elements must be immutable

### Syntax

```python
my_set = {1, 2, 3}
empty_set = set()
```

⚠️ `{}` creates a dictionary, not a set.

---

## 14. Key Characteristics

| Property   | Set         |
| ---------- | ----------- |
| Ordered    | No          |
| Mutable    | Yes         |
| Duplicates | Not allowed |
| Indexed    | No          |

---

## 15. Why Sets Exist

Sets are optimised for:

* **Uniqueness**
* **Fast membership testing**
* **Mathematical operations**

---

## 16. Adding and Removing Elements

### Add

```python
my_set.add(4)
```

### Remove (Error if missing)

```python
my_set.remove(3)
```

### Discard (Safe)

```python
my_set.discard(10)
```

### Pop

```python
my_set.pop()
```

Removes arbitrary element.

---

## 17. Set Operations (Very Important)

### Union

```python
A | B
A.union(B)
```

### Intersection

```python
A & B
A.intersection(B)
```

### Difference

```python
A - B
A.difference(B)
```

### Symmetric Difference

```python
A ^ B
A.symmetric_difference(B)
```

**Production use:** Permissions, tags, recommendation systems, data comparison.

---

## 18. Membership Testing

```python
if 5 in my_set:
    print("Exists")
```

**Extremely fast — O(1)**

Used heavily in validation logic.

---

## 19. Set Comprehension

```python
unique_squares = {x*x for x in range(10)}
```

**Use case:** Deduplication and transformation in one step.

---

## 20. Frozen Sets

```python
fs = frozenset([1, 2, 3])
```

* Immutable
* Hashable
* Can be dictionary keys

**Production use:** Constant sets, security rules, configuration constraints.

---

## 21. Performance Characteristics

| Operation  | Time |
| ---------- | ---- |
| Add        | O(1) |
| Remove     | O(1) |
| Membership | O(1) |

---

## 22. When to Use Sets in Production

* Removing duplicates
* Fast membership checks
* Tag systems
* Permissions and roles
* Finding common or missing elements
* Data cleansing pipelines

---

## 23. Dictionary vs Set — Comparison

| Feature            | Dictionary       | Set         |
| ------------------ | ---------------- | ----------- |
| Stores             | Key–Value        | Values only |
| Lookup             | By key           | By value    |
| Duplicate elements | Keys not allowed | Not allowed |
| Use case           | Mapping          | Uniqueness  |

---

## 24. Common Production Mistakes

* Using lists instead of sets for membership checks
* Using mutable objects as dictionary keys
* Forgetting `.get()` and causing `KeyError`
* Assuming sets preserve order

---

## 25. Final Summary

* **Dictionaries** are for structured, fast key-based access.
* **Sets** are for uniqueness and mathematical logic.
* Both are hash-table based and extremely fast.
* Correct choice between list, set and dict directly impacts performance and clarity in production systems.

---

