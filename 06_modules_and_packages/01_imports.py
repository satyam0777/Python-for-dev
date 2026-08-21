"""
MODULES & PACKAGES — Python vs JS/Node

JS/Node:
    import express from 'express';
    import { useState } from 'react';
    npm install express

Python:
    import os
    from math import sqrt
    pip install requests
"""

# --- Importing built-in modules (like Node's built-in fs, path, etc) ---
import math
print(math.sqrt(16))       # JS: Math.sqrt(16)
print(math.pi)               # JS: Math.PI

# --- Importing specific functions (JS named imports) ---
from math import sqrt, pi
print(sqrt(25))

# --- Importing with an alias (JS: import numpy as np -- same idea) ---
import math as m
print(m.sqrt(9))

# --- import everything (rarely recommended, pollutes namespace) ---
# from math import *   # JS equivalent: import * as math from 'math' but auto-flattened -- AVOID this

# --- Importing your OWN modules ---
# If you have a file `utils.py` in the same folder with:
#     def greet(name): return f"Hello {name}"
# You can import it like:
#     from utils import greet
# (There's a mini example: see helper_module.py in this same folder)
from importlib import import_module
helper = import_module("06_modules_and_packages.helper_module") if False else None
# ^ note: relative dotted imports only work cleanly when run as a package.
# Simplest real-world usage shown in helper_module.py comments.

# --- Package management: pip vs npm ---
# npm install axios          -->   pip install requests
# npm install --save-dev X   -->   pip install X  (Python doesn't split dev deps by default,
#                                                    but tools like poetry/pipenv do)
# package.json                -->  requirements.txt (just a plain list of packages + versions)
# node_modules/                --> virtual environment (venv) -- Python installs globally
#                                    or into an isolated venv folder, not per-project by default

# Example requirements.txt content:
# numpy==1.26.4
# pandas==2.2.2
# requests==2.31.0

# --- Virtual environments (Python's version of an isolated node_modules) ---
# python -m venv venv          # create a virtual environment
# source venv/bin/activate      # activate it (Mac/Linux)
# venv\\Scripts\\activate        # activate it (Windows)
# pip install -r requirements.txt

print("See helper_module.py for a custom-module import example")
