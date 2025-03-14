## 🔵 **Day 10: Object-Oriented Programming (OOP)**
- Classes and Objects
- Methods and Attributes
- Inheritance
---
Object-Oriented Programming (OOP) is a programming paradigm that organizes code using objects and classes. It helps structure programs in a way that models real-world entities, making the code more modular, reusable, and easier to maintain.

### 🟢 **Classes and Objects**
A **class** is a blueprint for creating objects, and an **object** is an instance of a class.

```python
# Defining a class
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    def display_info(self):
        print(f"This car is a {self.brand} {self.model}")

# Creating objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Accessing attributes and calling methods
car1.display_info()  # Output: This car is a Toyota Corolla
car2.display_info()  # Output: This car is a Honda Civic
```

### 🟢 **Methods and Attributes**
- **Methods** are functions defined inside a class that perform actions.
- **Attributes** store data related to an object.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object
p1 = Person("Alice", 30)
p1.greet()  # Output: Hello, my name is Alice and I am 30 years old.
```

### 🟢 **Inheritance**
Inheritance allows one class (child) to inherit attributes and methods from another class (parent), promoting code reusability.

```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic sound")

# Child class inheriting from Animal
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

# Creating objects
dog1 = Dog("Buddy")
dog1.make_sound()  # Output: Woof! Woof!
```

---
