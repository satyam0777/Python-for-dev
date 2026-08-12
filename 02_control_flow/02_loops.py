"""
LOOPS — Python vs JavaScript

Python's `for` loop is really a "for...of" loop from JS — it iterates
over ITEMS, not indexes. There is no classic C-style for(;;) loop in Python.
"""

fruits = ["apple", "banana", "mango"]

# JS: for (const fruit of fruits) { console.log(fruit); }
for fruit in fruits:
    print(fruit)

# --- Need the index too? use enumerate() ---
# JS: fruits.forEach((fruit, index) => console.log(index, fruit));
for index, fruit in enumerate(fruits):
    print(index, fruit)

# --- range() replaces the classic for(let i=0; i<n; i++) ---
# JS: for (let i = 0; i < 5; i++) { console.log(i); }
for i in range(5):          # 0,1,2,3,4
    print(i)

for i in range(2, 10, 2):   # start, stop, step -> 2,4,6,8
    print(i)

# --- while loop: basically identical to JS ---
count = 0
while count < 3:
    print("count is", count)
    count += 1     # NOTE: Python has NO ++ or -- operators! must use += 1

# --- break / continue: same keywords as JS ---
for num in range(10):
    if num == 5:
        break        # same as JS break
    if num % 2 == 0:
        continue      # same as JS continue
    print("odd number:", num)

# --- List comprehension: Python's superpower, no direct JS equivalent ---
# JS: const squares = [1,2,3,4].map(n => n * n);
squares = [n * n for n in [1, 2, 3, 4]]
print(squares)

# JS: const evens = [1,2,3,4,5,6].filter(n => n % 2 === 0);
evens = [n for n in [1, 2, 3, 4, 5, 6] if n % 2 == 0]
print(evens)

# combine map + filter in ONE line (very common interview question)
even_squares = [n * n for n in range(10) if n % 2 == 0]
print(even_squares)

# TODO (practice): use a list comprehension to get the length of each
# word in ["python", "js", "ai"] -> [6, 2, 2]
