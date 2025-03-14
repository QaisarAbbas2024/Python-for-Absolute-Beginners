## 🔵 Day 2: Variables, Data Types, and Input/Output
- Variables and Assignment
- Data Types: Numbers, Strings, Booleans
- Type Conversion
- User Input and Output
---
### 🟢 Variables and Assignment
A variable is a container for storing data values. In Python, variables do not need explicit declaration; they are created when a value is assigned:

      name = "Alice"
      age = 25
      height = 5.6

Here, name stores a string, age an integer, and height a float. Python dynamically assigns data types based on the value.
***
### 🟢 Data Types: Numbers, Strings, Booleans
Python supports various data types:

**Numbers:** Integers (int), Floating-point numbers (float), Complex numbers (complex)

**Strings:** Sequence of characters, enclosed in single or double quotes ("Hello" or 'World')

**Booleans:** Logical values, either True or False

      num = 10    # Integer
      pi = 3.14   # Float
      message = "Hello"  # String
      is_active = True  # Boolean
***
### 🟢 Type Conversion
You can convert one data type to another using type conversion functions:

      x = 5        # Integer
      y = "10"     # String
      z = float(x) # Convert integer to float
      w = int(y)   # Convert string to integer

The functions int(), float(), and str() help in type conversion.
***
### 🟢 User Input and Output
Python allows user input using the input() function, which always returns a string. You may need to convert it to another data type:

      name = input("Enter your name: ")
      age = int(input("Enter your age: "))
      print("Hello,", name, "You are", age, "years old.")

The print() function is used for displaying output. It can take multiple arguments, separated by commas.
***
