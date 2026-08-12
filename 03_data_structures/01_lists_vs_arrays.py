"""
LISTS — Python's version of JS Arrays

Lists are mutable, ordered, allow duplicates and mixed types — exactly
like JS arrays. Method names differ though.
"""

fruits = ["apple", "banana", "mango"]

# --- Adding items ---
fruits.append("orange")          # JS: fruits.push("orange")
print(fruits)

fruits.insert(1, "grape")        # JS: fruits.splice(1, 0, "grape")
print(fruits)

# --- Removing items ---
fruits.remove("banana")          # removes by VALUE. JS: fruits.splice(fruits.indexOf("banana"), 1)
print(fruits)

last = fruits.pop()              # removes & returns LAST item. Same as JS fruits.pop()
print("popped:", last, fruits)

first = fruits.pop(0)            # pop by index. JS: fruits.shift() for index 0
print("popped first:", first, fruits)

# --- Slicing (more powerful than JS .slice()) ---
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])     # [1, 2, 3]   JS: nums.slice(1, 4)
print(nums[:3])      # [0, 1, 2]   JS: nums.slice(0, 3)
print(nums[::2])     # [0, 2, 4]   every 2nd element -- no direct JS equivalent

# --- Combining / spreading lists ---
a = [1, 2]
b = [3, 4]
combined = a + b            # JS: [...a, ...b]
print(combined)

# --- Common functional methods (map/filter/reduce equivalents) ---
# JS: nums.map(n => n * 2)
doubled = list(map(lambda n: n * 2, nums))   # or better: [n*2 for n in nums]
print(doubled)

# JS: nums.filter(n => n % 2 === 0)
evens = list(filter(lambda n: n % 2 == 0, nums))   # or: [n for n in nums if n % 2 == 0]
print(evens)

# JS: nums.reduce((acc, n) => acc + n, 0)
from functools import reduce
total = reduce(lambda acc, n: acc + n, nums, 0)
print(total)
# In practice, Python devs prefer sum(nums) over reduce for simple sums!
print(sum(nums))

# --- Sorting ---
unsorted = [5, 2, 8, 1]
unsorted.sort()                     # mutates in place, JS: arr.sort((a,b) => a-b)
print(unsorted)
sorted_copy = sorted([3, 1, 2])     # returns NEW list, JS has no built-in non-mutating sort (until toSorted())
print(sorted_copy)

# INTERVIEW: list vs tuple — lists are MUTABLE, tuples are IMMUTABLE.
# See 03_tuples_sets.py for tuples.

# TODO (practice): given nums = [3, 6, 9, 12], use a list comprehension
# to get only the numbers divisible by 6.
