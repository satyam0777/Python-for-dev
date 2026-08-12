"""
OPERATORS — Python vs JavaScript

Big differences to memorize for interviews:
    JS  &&  ||  !         ->  Python  and  or  not
    JS  ===  !==           ->  Python  ==  !=   (Python has no "loose equality" like JS ==, so no need for ===)
    JS  no built-in power  ->  Python  **  (exponent), JS uses Math.pow() or **
    JS  no floor divide    ->  Python  //  (integer/floor division)
"""

a, b = 10, 3

print(a + b, a - b, a * b)      # same as JS
print(a / b)                    # 3.333... -> ALWAYS float in Python (JS: also float, no int/float split)
print(a // b)                   # 3        -> floor division, NO JS equivalent operator (Math.floor(a/b) in JS)
print(a % b)                    # 1        -> modulo, same as JS
print(a ** b)                   # 1000     -> exponent, JS uses a ** b too (ES2016+) or Math.pow(a, b)

# --- Comparison ---
print(a > b, a < b, a == b, a != b)   # same symbols as JS

# --- Logical operators: WORDS not symbols ---
is_logged_in = True
is_admin = False
print(is_logged_in and not is_admin)   # JS: is_logged_in && !is_admin
print(is_logged_in or is_admin)        # JS: is_logged_in || is_admin

# --- Identity vs equality: `is` vs `==` ---
# INTERVIEW FAVORITE:
# `==` checks VALUE equality (like JS ==, but without type coercion)
# `is` checks IDENTITY (same object in memory) — similar to comparing references
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)   # True  -> same values
print(list1 is list2)   # False -> different objects in memory

list3 = list1
print(list1 is list3)   # True -> same object reference

# --- Chained comparisons (Python-only convenience, no JS equivalent) ---
age = 25
print(18 <= age <= 60)   # equivalent JS: age >= 18 && age <= 60

# --- Ternary operator ---
# JS: const status = age >= 18 ? "adult" : "minor";
status = "adult" if age >= 18 else "minor"   # order is different! value_if_true if condition else value_if_false
print(status)

# TODO (practice): write a ternary that checks if a number is even or odd.
