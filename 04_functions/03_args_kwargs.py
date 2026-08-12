"""
*args and **kwargs — Python's version of JS rest/spread parameters
"""

# --- *args: variable number of POSITIONAL arguments ---
# JS: function sum(...nums) { return nums.reduce((a,b) => a+b, 0); }
def total(*args):
    print("args received as tuple:", args)   # args is a TUPLE inside the function
    return sum(args)

print(total(1, 2, 3, 4))

# --- **kwargs: variable number of KEYWORD (named) arguments ---
# JS: function createUser({ name, age, ...rest }) { ... }  (destructuring)
def create_profile(**kwargs):
    print("kwargs received as dict:", kwargs)   # kwargs is a DICT inside the function
    return kwargs

print(create_profile(name="Rahul", age=25, city="Delhi"))

# --- Combining normal args, *args, and **kwargs ---
def describe(name, *hobbies, **extra_info):
    print(f"Name: {name}")
    print(f"Hobbies: {hobbies}")
    print(f"Extra info: {extra_info}")

describe("Rahul", "coding", "gaming", age=25, city="Delhi")

# --- UNPACKING (the reverse direction — like JS spread ...) ---
# JS: const arr = [1, 2, 3]; myFunc(...arr);
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add3(*nums))          # unpack list into positional args, JS: myFunc(...nums)

info = {"a": 1, "b": 2, "c": 3}
print(add3(**info))         # unpack dict into keyword args, no direct JS equivalent

# --- Merging dicts (JS: { ...obj1, ...obj2 }) ---
defaults = {"theme": "dark", "lang": "en"}
overrides = {"lang": "hi"}
merged = {**defaults, **overrides}     # exactly like JS spread merge!
print(merged)   # {'theme': 'dark', 'lang': 'hi'}

# INTERVIEW: order of parameters MUST be:
# def f(positional, *args, keyword=default, **kwargs)

# TODO (practice): write a function `make_pizza(size, *toppings)` that
# prints "Making a {size} pizza with {toppings}"
