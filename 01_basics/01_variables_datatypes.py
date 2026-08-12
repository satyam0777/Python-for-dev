"""
VARIABLES & DATA TYPES — Python vs JavaScript

JS:
    let name = "Rahul";      // block-scoped
    const age = 25;          // constant
    var old = true;          // function-scoped (avoid)

Python has NO 'let/const/var'. You just assign. There's no keyword.
Python is dynamically typed too (like JS) but it is STRONGLY typed
(unlike JS, no silent "1" + 1 = "11" magic — Python will throw an error).
"""

# --- Basic assignment ---
name = "Rahul"          # str      -> like JS string
age = 25                 # int      -> JS has only "number", Python splits int/float
height = 5.9              # float    -> JS "number"
is_developer = True       # bool     -> JS boolean (note: capital True/False, not true/false!)
nothing = None            # None     -> JS null/undefined combined into one concept

print(name, age, height, is_developer, nothing)

# --- Checking type (like typeof in JS) ---
print(type(name))         # <class 'str'>   JS: typeof name -> "string"
print(type(age))          # <class 'int'>

# --- Multiple assignment (Python superpower, no JS equivalent this clean) ---
x, y, z = 1, 2, 3
print(x, y, z)

# JS equivalent would need destructuring:
# const [x, y, z] = [1, 2, 3];

# --- Constants ---
# Python has NO real constants. Convention: use ALL_CAPS name to signal
# "don't reassign this" — it's just a promise, not enforced by the language.
PI = 3.14159

# --- f-strings = JS template literals ---
# JS: `My name is ${name} and I am ${age}`
message = f"My name is {name} and I am {age}"
print(message)

# INTERVIEW: Python is "dynamically & strongly typed".
# Dynamic = you don't declare types upfront.
# Strong = no implicit type coercion like JS's "5" + 5 -> "55"
try:
    result = "5" + 5   # this will raise TypeError in Python (JS would give "55")
except TypeError as e:
    print("Error (as expected):", e)

# TODO (practice): create a variable `city` with your city, print its type.
