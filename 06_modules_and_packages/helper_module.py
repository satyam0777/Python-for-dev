"""
HELPER MODULE — demonstrates how Python "exports" things

JS:
    // helper.js
    export function greet(name) { return `Hello, ${name}`; }
    export const PI = 3.14;

    // main.js
    import { greet, PI } from './helper.js';

Python has NO explicit `export` keyword — EVERYTHING at the top level
of a file is automatically "exportable" by default.
"""

def greet(name):
    return f"Hello, {name}"

PI = 3.14

class Helper:
    @staticmethod
    def double(x):
        return x * 2


# --- The `if __name__ == "__main__"` trick ---
# This is Python's version of checking `require.main === module` in Node,
# or the difference between a script run directly vs imported as a module.
# Code inside this block ONLY runs when you execute THIS file directly
# (python helper_module.py), NOT when another file imports from it.
if __name__ == "__main__":
    print(greet("World"))
    print(PI)
    print(Helper.double(21))

# To use this from another file in the SAME folder:
#     from helper_module import greet, PI, Helper
#     print(greet("Rahul"))
