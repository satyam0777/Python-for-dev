"""
STRINGS — Python vs JavaScript
Strings behave a lot like JS strings (immutable, indexable) but the
method names are different and Python has more built-in slicing power.
"""

s = "Hello World"

# --- Indexing & slicing (like JS but with more power) ---
print(s[0])          # 'H'          same as JS s[0]
print(s[-1])         # 'd'          last char — JS needs s[s.length - 1]
print(s[0:5])        # 'Hello'      slicing — JS needs s.slice(0, 5)
print(s[::-1])       # 'dlroW olleH' reverse a string — no direct JS equivalent (JS: s.split('').reverse().join(''))

# --- Common methods (compare to JS) ---
print(s.upper())              # JS: s.toUpperCase()
print(s.lower())               # JS: s.toLowerCase()
print(s.replace("World", "Python"))  # JS: s.replace("World", "Python")
print(s.split(" "))            # JS: s.split(" ")  -> returns a list, same idea
print(len(s))                  # JS: s.length      -> Python uses len() function, NOT a property!
print(s.strip())               # JS: s.trim()
print(s.find("World"))         # JS: s.indexOf("World")
print("World" in s)            # JS: s.includes("World")  -> Python uses the `in` keyword

# --- f-strings vs template literals ---
name = "Rahul"
score = 95.456
# JS: `${name} scored ${score.toFixed(1)}%`
print(f"{name} scored {score:.1f}%")   # :.1f formats float to 1 decimal place

# --- String immutability (same concept as JS) ---
# s[0] = "Y"   # This would raise TypeError — strings are immutable, just like JS

# --- Joining (opposite direction from JS array.join) ---
words = ["Python", "is", "fun"]
sentence = " ".join(words)      # JS: words.join(" ")  -- note: called ON the separator in Python!
print(sentence)

# --- Multiline strings ---
multiline = """
This is line 1
This is line 2
"""   # JS equivalent: template literals with backticks
print(multiline)

# TODO (practice): Given full_name = "rahul sharma", capitalize each word
# (hint: look up .title() method)
