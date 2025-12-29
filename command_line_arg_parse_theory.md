# Command Line Arguments in Python (`argparse`)

---

## 1. What Are Command Line Arguments?

Command line arguments are **values passed to a program at runtime**, directly from the terminal.

Example:

```bash
python app.py --input data.csv --epochs 50
```

Here:

* `--input` and `--epochs` are arguments
* `data.csv` and `50` are their values

---

## 2. Why Command Line Arguments Exist

Before arguments, scripts were often written like this:

```python
input_file = "data.csv"
epochs = 50
```

### Problems with Hardcoded Values

* Script must be edited every time
* Not reusable
* Not automatable
* Impossible to integrate into pipelines, CI/CD, or cron jobs

Command line arguments solve this by **separating configuration from code**.

---

## 3. Early / Incorrect Way: `sys.argv`

### Example

```python
import sys

print(sys.argv)
```

Command:

```bash
python app.py hello 10
```

Output:

```python
['app.py', 'hello', '10']
```

### Problems with `sys.argv`

* No type checking
* No validation
* No help messages
* Manual parsing
* Easy to break

This is why `argparse` exists.

---

## 4. What Is `argparse`?

`argparse` is Python’s **standard library** for building **professional command-line interfaces (CLI)**.

It provides:

* Automatic help messages
* Type conversion
* Validation
* Default values
* Optional and positional arguments
* Subcommands (like `git commit`, `git push`)

---

## 5. Basic Structure of `argparse`

Every argparse program follows this structure:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(...)
args = parser.parse_args()
```

---

## 6. Minimal Working Example

```python
import argparse

parser = argparse.ArgumentParser(description="Simple CLI example")
parser.add_argument("name")
args = parser.parse_args()

print(f"Hello {args.name}")
```

Command:

```bash
python app.py Siddhant
```

Output:

```
Hello Siddhant
```

---

## 7. Positional Arguments

Positional arguments are **mandatory** and determined by position.

```python
parser.add_argument("filename")
```

Usage:

```bash
python app.py data.csv
```

Access:

```python
args.filename
```

### Production Use

* Input files
* Mandatory identifiers
* Required paths

---

## 8. Optional Arguments (Flags)

Optional arguments start with `-` or `--`.

```python
parser.add_argument("--epochs")
```

Usage:

```bash
python train.py --epochs 50
```

Access:

```python
args.epochs
```

---

## 9. Short and Long Flags

```python
parser.add_argument("-e", "--epochs")
```

Both work:

```bash
python train.py -e 50
python train.py --epochs 50
```

### Production Convention

* Short flags for frequent use
* Long flags for clarity

---

## 10. Type Conversion

By default, arguments are strings.

```python
parser.add_argument("--epochs", type=int)
```

Now:

```bash
python train.py --epochs 10
```

`args.epochs` is an integer.

### Supported Types

* `int`
* `float`
* `str`
* `pathlib.Path`
* Custom functions

---

## 11. Default Values

```python
parser.add_argument("--lr", type=float, default=0.001)
```

If not passed:

```python
args.lr == 0.001
```

### Production Use

* Sensible defaults
* Optional configuration

---

## 12. Required Optional Arguments

Optional syntax but mandatory presence:

```python
parser.add_argument("--config", required=True)
```

Usage:

```bash
python app.py --config config.yaml
```

---

## 13. Boolean Flags

### Incorrect Way

```python
--debug True
```

### Correct Way

```python
parser.add_argument("--debug", action="store_true")
```

Usage:

```bash
python app.py --debug
```

Result:

```python
args.debug == True
```

---

## 14. Choices (Validation)

```python
parser.add_argument(
    "--mode",
    choices=["train", "test", "eval"]
)
```

Invalid input automatically errors.

### Production Use

* Environment selection
* Mode control
* Prevent invalid states

---

## 15. Help Messages (Auto-Generated)

Running:

```bash
python app.py --help
```

Produces a full help page automatically.

You can customise:

```python
parser.add_argument(
    "--epochs",
    help="Number of training epochs"
)
```

---

## 16. Customising the Program Description

```python
parser = argparse.ArgumentParser(
    description="Training pipeline for ML model"
)
```

Appears at the top of `--help`.

---

## 17. Argument Groups (Clean Help Output)

```python
group = parser.add_argument_group("Training Parameters")
group.add_argument("--epochs", type=int)
group.add_argument("--lr", type=float)
```

### Production Use

* Large tools
* Clear separation of concerns

---

## 18. Parsing Lists

```python
parser.add_argument("--layers", nargs="+", type=int)
```

Usage:

```bash
python app.py --layers 64 128 256
```

Result:

```python
args.layers == [64, 128, 256]
```

---

## 19. File and Path Handling

```python
from pathlib import Path

parser.add_argument("--input", type=Path)
```

### Why This Is Better

* Cross-platform
* Cleaner file operations
* Safer path handling

---

## 20. Subcommands (Advanced, Production-Level)

Used in tools like `git`, `docker`, `kubectl`.

```python
subparsers = parser.add_subparsers(dest="command")

train = subparsers.add_parser("train")
train.add_argument("--epochs", type=int)

test = subparsers.add_parser("test")
test.add_argument("--checkpoint")
```

Usage:

```bash
python app.py train --epochs 10
python app.py test --checkpoint model.pt
```

---

## 21. Real-World Production Use Cases

### Machine Learning

* Training configs
* Hyperparameters
* Dataset paths

### DevOps

* Deployment scripts
* Environment selection
* Secrets injection (paths only)

### Data Engineering

* ETL pipelines
* Batch jobs
* Cron-based automation

### Backend Tooling

* Database migrations
* Admin scripts
* Maintenance jobs

---

## 22. Common Mistakes

* Forgetting `type=`
* Overusing positional arguments
* No help descriptions
* Hardcoding values instead of arguments
* Using argparse for user input inside programs (wrong use case)

---

## 23. When NOT to Use `argparse`

* Interactive applications
* GUIs
* Web servers
* Real-time user prompts

`argparse` is strictly for **program startup configuration**.

---

## 24. Mental Model

> `argparse` is how professionals turn scripts into tools.

It converts:

* Scripts → CLI programs
* Manual runs → automation
* Ad-hoc code → production utilities

---

## 25. Final Summary

* `argparse` is the standard for CLI tools in Python
* It is safer, cleaner, and more maintainable than `sys.argv`
* It enforces correctness at program entry
* Essential for real-world, production-ready Python

---

