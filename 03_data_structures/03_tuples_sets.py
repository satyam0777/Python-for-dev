"""
TUPLES & SETS — two Python types with no exact 1:1 JS equivalent

TUPLE  = immutable, ordered list. JS has no native tuple (Object.freeze([...]) is closest)
SET    = unique unordered values, same concept as JS Set
"""

# --- TUPLES ---
point = (10, 20)
print(point[0], point[1])

# point[0] = 99   # TypeError! tuples are IMMUTABLE — this is THE key interview point

# Why use tuples over lists?
# 1. Signals "this data shouldn't change" (like coordinates, RGB values)
# 2. Can be used as DICT KEYS (lists cannot, because lists are mutable/unhashable)
locations = {
    (28.6, 77.2): "Delhi",
    (19.0, 72.8): "Mumbai"
}
print(locations[(28.6, 77.2)])

# --- Tuple unpacking (very Pythonic, used everywhere) ---
x, y = point                 # JS: const [x, y] = point;
print(x, y)

# Multiple return values from a function ALWAYS use tuples under the hood:
def get_min_max(nums):
    return min(nums), max(nums)   # this is secretly returning a tuple: (min, max)

low, high = get_min_max([4, 1, 9, 2])
print(low, high)

# --- SETS ---
# JS: const s = new Set([1, 2, 2, 3]);  console.log(s);  -> Set(3) {1, 2, 3}
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)              # {1, 2, 3} -- duplicates auto-removed

numbers.add(4)               # JS: s.add(4)
numbers.discard(1)           # JS: s.delete(1)   (discard won't error if missing; .remove() will)
print(numbers)

# --- Set math (this is where sets shine, no easy JS equivalent) ---
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b)   # intersection -> {3, 4}
print(a | b)   # union        -> {1,2,3,4,5,6}
print(a - b)   # difference   -> {1, 2}

# INTERVIEW: use a set to quickly deduplicate a list
raw = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(raw))
print(unique)   # order not guaranteed! use dict.fromkeys(raw) if you need to preserve order

# TODO (practice): given two lists of user IDs who liked post A and post B,
# find IDs who liked BOTH posts, using set intersection.
