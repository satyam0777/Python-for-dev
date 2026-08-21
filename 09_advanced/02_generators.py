"""
GENERATORS — Python's `yield`, closest JS equivalent is generator functions
(function* ... yield ...), which JS also has but is rarely used day-to-day.

Key idea: a generator produces values ONE AT A TIME, on demand, instead of
building the entire list in memory upfront. Crucial for big data / AI workloads
(e.g., streaming a huge dataset without loading it all into RAM).
"""

# --- Normal function: builds the ENTIRE list in memory ---
def get_squares_list(n):
    result = []
    for i in range(n):
        result.append(i * i)
    return result

print(get_squares_list(5))   # [0, 1, 4, 9, 16] -- all computed & stored immediately

# --- Generator function: computes values LAZILY, one at a time ---
def get_squares_gen(n):
    for i in range(n):
        yield i * i          # `yield` pauses the function and returns a value
                              # JS equivalent: function* getSquares(n) { yield i*i; }

gen = get_squares_gen(5)
print(gen)                    # <generator object ...> -- nothing computed yet!
print(next(gen))              # 0  -- computes ONLY the first value
print(next(gen))              # 1  -- computes ONLY the second value

# You can also loop through a generator like a normal iterable:
for val in get_squares_gen(5):
    print(val)

# --- Why generators matter: MEMORY EFFICIENCY ---
# Imagine processing a file with 10 million lines.
def read_large_file_lines(filepath):
    with open(filepath) as f:
        for line in f:
            yield line.strip()
# This NEVER loads the whole file into memory — reads one line at a time.
# Directly relevant to AI/ML: streaming huge datasets/token batches this way.

# --- Generator expressions (like list comprehensions, but lazy) ---
squares_list_comp = [x * x for x in range(1000000)]   # allocates ALL 1M items in memory NOW
squares_gen_exp = (x * x for x in range(1000000))       # allocates NOTHING until you iterate
print(type(squares_gen_exp))

# INTERVIEW: "What's the difference between a list comprehension and a
# generator expression?" -> syntax: [] vs (), and generators are LAZY
# (computed on demand) while list comprehensions are EAGER (computed immediately).

# TODO (practice): write a generator `fibonacci(n)` that yields the first
# n Fibonacci numbers, one at a time.
