#### oop.py
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        return f"Car: {self.brand} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car.display_info())
```
#### **oop.py**  
```python
# Creating a simple class and object
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def show_info(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

# Creating an object
s1 = Student("John", "A")
s1.show_info()

# Inheritance example
class Teacher(Student):
    def __init__(self, name, subject):
        super().__init__(name, "N/A")
        self.subject = subject

    def show_info(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

t1 = Teacher("Ms. Smith", "Mathematics")
t1.show_info()
```

#### **exercises.py**  
```python
# 1. Create a class called "Book" with attributes for title and author.
# 2. Add a method to display book details.
# 3. Create a child class "EBook" that inherits from "Book" and has an additional attribute for file size.
# 4. Implement a method in "EBook" to show details including the file size.
# 5. Create instances of "Book" and "EBook" and display their details.
# 6. Implement a class for a bank account with deposit and withdrawal methods.
# 7. Create a class for a student with attributes name and age.
```
