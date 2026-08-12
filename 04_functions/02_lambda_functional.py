"""
LAMBDA & FUNCTIONAL PROGRAMMING — Python vs JS Arrow Functions
"""

# JS: const add = (a, b) => a + b;
add = lambda a, b: a + b
print(add(2, 3))

# Lambdas are limited to a SINGLE expression (no multi-line logic, no statements).
# Used mostly as throwaway functions passed into map/filter/sort.

# --- sort with a custom key (super common interview + real-world pattern) ---
users = [
    {"name": "Rahul", "age": 25},
    {"name": "Aisha", "age": 22},
    {"name": "Vikram", "age": 30},
]

# JS: users.sort((a, b) => a.age - b.age)
users_sorted = sorted(users, key=lambda u: u["age"])
print(users_sorted)

# JS: users.sort((a, b) => b.age - a.age)  // descending
users_desc = sorted(users, key=lambda u: u["age"], reverse=True)
print(users_desc)

# --- map / filter with lambda (list comprehensions are usually preferred in Python) ---
nums = [1, 2, 3, 4, 5]

doubled = list(map(lambda n: n * 2, nums))       # prefer: [n*2 for n in nums]
evens = list(filter(lambda n: n % 2 == 0, nums))  # prefer: [n for n in nums if n % 2 == 0]
print(doubled, evens)

# --- Higher order functions: functions that return functions ---
# JS: const makeMultiplier = (factor) => (x) => x * factor;
def make_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)
print(double(10), triple(10))   # 20 30

# This "function returning a function" pattern is the FOUNDATION of decorators
# — see 09_advanced/01_decorators.py

# TODO (practice): use sorted() with a lambda to sort a list of strings
# by their length: ["banana", "kiwi", "apple"] -> shortest to longest
