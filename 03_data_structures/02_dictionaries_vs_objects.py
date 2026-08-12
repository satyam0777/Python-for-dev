"""
DICTIONARIES — Python's version of JS Objects / Maps

JS:
    const user = { name: "Rahul", age: 25 };
    console.log(user.name);       // dot notation
    console.log(user["name"]);    // bracket notation

Python dicts use ONLY bracket-style access with quotes required around keys
(no dot notation for dicts — dot notation is reserved for object attributes,
see 05_oop).
"""

user = {
    "name": "Rahul",
    "age": 25,
    "is_developer": True
}

# --- Accessing values ---
print(user["name"])                 # KeyError if key doesn't exist (JS: undefined, no error)
print(user.get("email"))            # safer! returns None if missing. JS: user.email ?? undefined
print(user.get("email", "N/A"))     # with a default fallback value

# --- Adding / updating ---
user["email"] = "rahul@example.com"    # JS: user.email = "..."
user["age"] = 26
print(user)

# --- Removing ---
del user["is_developer"]              # JS: delete user.is_developer
print(user)

# --- Checking key existence ---
print("name" in user)                 # JS: "name" in user  OR  user.hasOwnProperty("name")

# --- Looping through a dict ---
# JS: Object.keys(user).forEach(key => console.log(key, user[key]))
for key in user:
    print(key, "->", user[key])

# JS: Object.entries(user).forEach(([key, value]) => ...)
for key, value in user.items():
    print(key, "=", value)

# JS: Object.keys(user)  /  Object.values(user)
print(list(user.keys()))
print(list(user.values()))

# --- Dict comprehension (like list comprehension but for dicts) ---
# JS has no direct equivalent; closest is Object.fromEntries(arr.map(...))
squares = {n: n * n for n in range(5)}
print(squares)   # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# --- Nested dicts (same idea as nested JS objects) ---
company = {
    "name": "TechCorp",
    "address": {
        "city": "Delhi",
        "pincode": "110001"
    }
}
print(company["address"]["city"])

# INTERVIEW: dict keys must be HASHABLE (immutable) — so you CAN use
# strings, numbers, tuples as keys, but NOT lists or other dicts as keys.
# (Same restriction JS Map has for object keys in some sense, but dict
# is closer to a plain JS object.)

# TODO (practice): build a dict comprehension mapping each fruit in
# ["apple","banana","mango"] to the length of its name.
