"""
INHERITANCE — Python vs JS

JS:
    class Animal {
      constructor(name) { this.name = name; }
      speak() { return `${this.name} makes a sound`; }
    }
    class Dog extends Animal {
      speak() { return `${this.name} barks`; }
    }
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):          # JS: class Dog extends Animal
    def speak(self):        # method overriding, same concept as JS
        return f"{self.name} barks"


class Cat(Animal):
    def speak(self):
        # super() = JS's super. Calls the PARENT class's method.
        parent_sound = super().speak()
        return f"{parent_sound}, specifically {self.name} meows"


dog = Dog("Rex")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())

# --- isinstance() = JS's instanceof ---
print(isinstance(dog, Animal))   # True -- Dog IS an Animal (inheritance)
print(isinstance(dog, Dog))      # True

# --- Multiple inheritance (Python allows this, JS does NOT natively) ---
class Flyable:
    def fly(self):
        return "I can fly!"

class FlyingDog(Dog, Flyable):    # inherits from BOTH classes
    pass

fd = FlyingDog("Sky")
print(fd.speak())   # from Dog
print(fd.fly())      # from Flyable

# INTERVIEW: Python resolves multiple inheritance conflicts using MRO
# (Method Resolution Order) — left to right, depth-first.
print(FlyingDog.__mro__)   # shows the resolution order

# --- Abstract base classes (Python's version of interfaces/abstract classes) ---
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass   # subclasses MUST implement this, or they can't be instantiated

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

sq = Square(4)
print(sq.area())

# shape = Shape()   # TypeError! Can't instantiate an abstract class

# TODO (practice): create a `Vehicle` base class and `Car`, `Bike` subclasses
# that override a `describe()` method.
