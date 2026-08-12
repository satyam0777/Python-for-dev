"""
CLASSES — Python vs JS ES6 Classes
The concepts map almost 1:1, syntax differs.

JS:
    class User {
      constructor(name, age) {
        this.name = name;
        this.age = age;
      }
      greet() {
        return `Hi, I'm ${this.name}`;
      }
    }
"""

class User:
    # __init__ is the constructor. Python: NO word "constructor".
    def __init__(self, name, age):
        # `self` = JS's `this`. Must be the FIRST parameter of every method, explicitly.
        self.name = name
        self.age = age

    def greet(self):     # every instance method needs `self` as first param
        return f"Hi, I'm {self.name}"

    # __str__ controls what print(obj) shows -- like JS's toString()
    def __str__(self):
        return f"User({self.name}, {self.age})"

user1 = User("Rahul", 25)      # JS: new User("Rahul", 25) -- Python has NO `new` keyword!
print(user1.greet())
print(user1)                    # calls __str__ automatically

# --- Class variables vs instance variables ---
class Counter:
    total_created = 0            # class variable — shared across ALL instances (like a static prop)

    def __init__(self):
        Counter.total_created += 1
        self.id = Counter.total_created   # instance variable — unique per object

c1 = Counter()
c2 = Counter()
print(Counter.total_created)     # 2
print(c1.id, c2.id)               # 1 2

# --- Methods that don't need an instance: @staticmethod / @classmethod ---
class MathUtils:
    @staticmethod                 # JS: static add(a, b) { return a + b; }
    def add(a, b):
        return a + b

    @classmethod                  # receives the CLASS itself as first arg (cls), not an instance
    def describe(cls):
        return f"This is the {cls.__name__} class"

print(MathUtils.add(3, 4))
print(MathUtils.describe())

# --- Properties (like JS getters/setters) ---
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property                     # JS: get area() { return Math.PI * this.radius ** 2; }
    def area(self):
        return 3.14159 * self.radius ** 2

circle = Circle(5)
print(circle.area)     # NOTE: called WITHOUT parentheses, looks like a plain attribute!

# TODO (practice): create a class `BankAccount` with balance, deposit(amount)
# and withdraw(amount) methods. Raise an error if withdrawal exceeds balance.
