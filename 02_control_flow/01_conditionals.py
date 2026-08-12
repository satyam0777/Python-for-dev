"""
CONDITIONALS — Python vs JavaScript

Biggest visual difference: Python uses INDENTATION instead of curly braces {}.
No semicolons. No parentheses required around the condition.
"""

age = 20

# JS:
# if (age >= 18) {
#   console.log("Adult");
# } else if (age >= 13) {
#   console.log("Teen");
# } else {
#   console.log("Child");
# }

if age >= 18:
    print("Adult")
elif age >= 13:          # Python's "else if" is ONE word: elif
    print("Teen")
else:
    print("Child")

# INTERVIEW: Python indentation is NOT optional style — it's part of the syntax.
# Mixing tabs and spaces will cause an IndentationError.

# --- Truthy / Falsy values (compare carefully to JS!) ---
# JS falsy: false, 0, "", null, undefined, NaN
# Python falsy: False, 0, 0.0, "", [], {}, (), None
if []:
    print("this won't print, empty list is falsy")
else:
    print("empty list is falsy, just like empty string")

# --- No switch statement in older Python! ---
# Python 3.10+ introduced `match` (similar to switch)
day = "Mon"
match day:
    case "Mon":
        print("Start of week")
    case "Fri":
        print("Almost weekend")
    case _:                       # `_` is the default case, like JS `default:`
        print("Regular day")

# TODO (practice): write nested if/elif to grade a score:
# >=90 A, >=75 B, >=50 C, else F
