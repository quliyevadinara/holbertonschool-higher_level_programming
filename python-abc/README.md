# Python ABC (Abstract Base Classes) Exercises

This project contains 5 comprehensive exercises demonstrating advanced Python object-oriented programming concepts including Abstract Base Classes, inheritance, duck typing, mixins, and multiple inheritance.

## Exercises

### 0. Abstract Animal Class and its Subclasses
**File:** `task_00_abc.py`

Learn how to create abstract base classes using Python's ABC module.

- Create an abstract `Animal` class with an abstract method `sound()`
- Implement `Dog` class that returns "Bark"
- Implement `Cat` class that returns "Meow"
- Attempting to instantiate `Animal` directly raises `TypeError`

**Test:** `./main_00_abc.py`

### 1. Shapes, Interfaces, and Duck Typing
**File:** `task_01_duck_typing.py`

Understand duck typing and how Python handles polymorphism without explicit type checking.

- Create abstract `Shape` class with `area()` and `perimeter()` methods
- Implement `Circle` class with radius parameter
- Implement `Rectangle` class with width and height parameters
- Create `shape_info()` function that uses duck typing (no type checking)

**Test:** `./main_01_duck_typing.py`

### 2. Extending the Python List with Notifications
**File:** `task_02_verboselist.py`

Learn how to extend built-in classes to customize their behavior.

- Create `VerboseList` class extending the built-in `list`
- Override `append()` to print "Added [item] to the list."
- Override `extend()` to print "Extended the list with [x] items."
- Override `remove()` to print "Removed [item] from the list."
- Override `pop()` to print "Popped [item] from the list."

**Test:** `./main_02_verboselist.py`

### 3. CountedIterator - Keeping Track of Iteration
**File:** `task_03_countediterator.py`

Create custom iterators by extending iterator functionality.

- Create `CountedIterator` class that wraps any iterable
- Override `__next__()` to increment a counter
- Implement `get_count()` method to retrieve iteration count
- Properly raise `StopIteration` when exhausted

**Test:** `./main_03_countediterator.py`

### 4. The Enigmatic FlyingFish - Multiple Inheritance
**File:** `task_04_flyingfish.py`

Explore multiple inheritance and Method Resolution Order (MRO).

- Create `Fish` class with `swim()` and `habitat()` methods
- Create `Bird` class with `fly()` and `habitat()` methods
- Create `FlyingFish` inheriting from both `Fish` and `Bird`
- Override all three methods in `FlyingFish`
- Understand MRO using `FlyingFish.mro()`

**Test:** `./main_04_flyingfish.py`

### 5. The Mystical Dragon - Mastering Mixins
**File:** `task_05_dragon.py`

Learn how to use mixins for composable behavior.

- Create `SwimMixin` class with `swim()` method
- Create `FlyMixin` class with `fly()` method
- Create `Dragon` class inheriting from both mixins
- Add `roar()` method to `Dragon`
- Demonstrate composition over complex inheritance

**Test:** `./main_05_dragon.py`

## Running the Exercises

Make the task files executable:
```bash
chmod +x task_00_abc.py
chmod +x task_01_duck_typing.py
chmod +x task_02_verboselist.py
chmod +x task_03_countediterator.py
chmod +x task_04_flyingfish.py
chmod +x task_05_dragon.py
