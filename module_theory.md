# Modules in Python

---

## 1. What Is a Module?

A **module** is a file containing Python code that can be **imported and reused** in other programs.

Technically:

* Any `.py` file is a module
* Its filename becomes the module name

Example:

```text
math_utils.py
```

This file itself is a module named `math_utils`.

---

## 2. Why Modules Exist

Before modules, code often looks like this:

```python
# everything in one file
def add(a, b): ...
def subtract(a, b): ...
def multiply(a, b): ...
```

### Problems

* Files become large and unmanageable
* Code cannot be reused easily
* No logical separation
* Difficult to test and maintain

Modules solve this by enforcing:

* Separation of concerns
* Reusability
* Maintainability
* Scalability

---

## 3. Creating a Module

### File: `math_utils.py`

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### Using the Module

```python
import math_utils

print(math_utils.add(2, 3))
```

---

## 4. Importing Modules — All Ways

---

### 4.1 `import module`

```python
import math_utils

math_utils.add(2, 3)
```

Best when:

* Avoiding name conflicts
* Clarity is important

---

### 4.2 `from module import name`

```python
from math_utils import add

add(2, 3)
```

Best when:

* Only a few functions are needed

Risk:

* Namespace pollution

---

### 4.3 `from module import *` (Not Recommended)

```python
from math_utils import *
```

Problems:

* Unclear where names come from
* Can overwrite existing names
* Hard to debug

Avoid in production.

---

### 4.4 Import with Alias

```python
import numpy as np
```

Used when:

* Module names are long
* Industry conventions exist

---

## 5. Built-in Modules

Python ships with many **standard library modules**.

Examples:

```python
import math
import os
import sys
import datetime
import argparse
import pathlib
```

### Why Standard Library Matters

* No external dependencies
* Well-tested
* Cross-platform
* Production-ready

---

## 6. Example: Using a Built-in Module

```python
import math

math.sqrt(16)
math.pi
```

---

## 7. Module Search Path (`sys.path`)

When you import a module, Python searches in:

1. Current directory
2. Standard library directories
3. Site-packages (installed libraries)

```python
import sys
print(sys.path)
```

### Production Insight

* Incorrect paths cause `ModuleNotFoundError`
* Virtual environments isolate dependencies

---

## 8. `__name__` and Module Execution

Every module has a `__name__` attribute.

```python
print(__name__)
```

* When run directly → `"__main__"`
* When imported → module name

---

### 8.1 `if __name__ == "__main__"`

```python
def main():
    print("Running main logic")

if __name__ == "__main__":
    main()
```

### Why This Exists

* Allows reuse without auto-execution
* Essential for libraries
* Standard production pattern

---

## 9. Modules vs Scripts

| Script            | Module           |
| ----------------- | ---------------- |
| Executed directly | Imported         |
| Entry-point logic | Reusable logic   |
| CLI oriented      | Library oriented |

A good Python file can be **both**.

---

## 10. Variables in Modules

```python
# config.py
DEBUG = True
TIMEOUT = 30
```

Usage:

```python
import config

if config.DEBUG:
    ...
```

### Production Use

* Centralised configuration
* Shared constants
* Feature flags

---

## 11. Module Caching

Imported modules are loaded **once per process**.

```python
import math
import math  # not reloaded
```

Stored in:

```python
sys.modules
```

### Implication

* Global state persists
* Side effects run only once

---

## 12. Reloading a Module (Rare)

```python
import importlib
importlib.reload(module)
```

Used mainly in:

* Development
* REPL environments

Avoid in production.

---

## 13. Writing Clean Modules

### Best Practices

* One responsibility per module
* Clear naming
* No heavy logic at import time
* Avoid side effects
* Explicit imports

---

## 14. Private Members in Modules

Python uses convention:

```python
_internal_value = 10
```

Meaning:

* Internal use only
* Not part of public API

Enforced by discipline, not the language.

---

## 15. `__all__` — Controlling Exports

```python
__all__ = ["add", "subtract"]
```

Used with:

```python
from module import *
```

Rare in production, but useful in libraries.

---

## 16. Package vs Module (Preview)

* **Module** → single `.py` file
* **Package** → directory of modules

Example:

```text
utils/
  ├── __init__.py
  ├── math_utils.py
  └── string_utils.py
```

---

## 17. Real-World Production Use Cases

### Backend Systems

* Auth module
* Database module
* Logging module

### ML / Data Science

* Data loaders
* Feature engineering
* Evaluation metrics

### DevOps

* Deployment helpers
* Monitoring utilities

---

## 18. Common Mistakes

* Circular imports
* Heavy code at import time
* Using `import *`
* Mixing CLI logic with library logic
* Poor naming

---

## 19. Mental Model

> A module is a **unit of reuse and responsibility**.

If a file has:

* A clear purpose
* No accidental execution
* Clean imports

It is production-ready.

---

## 20. Final Summary

* Every `.py` file is a module
* Modules enable reuse, structure, and clarity
* Proper imports are essential for scalability
* `__name__ == "__main__"` is critical
* Clean modules are the foundation of professional Python

---

