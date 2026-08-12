"""
FUNCTIONS — Python vs JavaScript
"""

# JS: function greet(name) { return `Hello, ${name}`; }
def greet(name):
    return f"Hello, {name}"

print(greet("Rahul"))

# --- Default parameters (same idea as JS) ---
# JS: function greet(name = "Guest") { ... }
def greet2(name="Guest"):
    return f"Hello, {name}"

print(greet2())

# --- Keyword arguments (Python-only convenience, no JS equivalent this direct) ---
def create_user(name, age, city="Delhi"):
    return {"name": name, "age": age, "city": city}

# You can pass args by NAME, in ANY order:
print(create_user(age=25, name="Rahul"))
print(create_user("Rahul", 25, city="Mumbai"))

# --- Multiple return values (via tuple, see 03_tuples_sets.py) ---
def divide(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder     # JS would need to return an array or object

q, r = divide(17, 5)
print(q, r)

# --- Functions are first-class citizens, same as JS ---
def apply_twice(func, value):
    return func(func(value))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))   # 20

# --- Type hints (optional but VERY common in real & interview code) ---
# JS/TS equivalent: TypeScript type annotations
def add(a: int, b: int) -> int:
    return a + b

print(add(3, 4))
# Type hints are NOT enforced at runtime by default — just documentation/tooling.

# --- Docstrings (like JSDoc comments in JS) ---
def multiply(a, b):
    """Multiply two numbers and return the result.

    Equivalent to JSDoc:
    /**
     * Multiply two numbers.
     * @param {number} a
     * @param {number} b
     * @returns {number}
     */
    """
    return a * b

print(multiply.__doc__)   # you can access the docstring at runtime!

# TODO (practice): write a function `is_palindrome(s)` that returns
# True/False whether a string reads the same forwards and backwards.
