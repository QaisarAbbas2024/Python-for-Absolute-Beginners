## Day 6: Functions
Functions allow us to group code into reusable blocks, making programs more organized and efficient.
- Defining Functions
- Function Arguments and Return Values
- Types of Function Arguments
  - Positional Arguments
  - Default Arguments
  - Keyword Arguments (`*args`)
  - Arbitrary Keyword Arguments (`**kwargs`)
- Scope of Variables
***
### 🟢 Defining Functions
A function is defined using the `def` keyword.

      def greet():
          print("Hello, welcome to Python!")
      
      greet()  # Calling the function
***
### 🟢 Function Arguments and Return Values
Functions can take parameters (inputs) and return values (outputs).

      def add(a, b):
          return a + b
      
      result = add(5, 3)
      print("Sum:", result)
***
### Types of Function Arguments

1. **Positional Arguments:** Passed in the correct order.

```python
def info(name, age):
    print(f"Name: {name}, Age: {age}")

info("Alice", 25)
```

2. **Default Arguments:** Have default values if not provided.

```python
def greet(name="Guest"):
    print("Hello,", name)

greet()  # Uses default value
```

3. **Keyword Arguments:** Passed using key-value pairs.

```python
def person(name, age):
    print(f"Name: {name}, Age: {age}")

person(age=30, name="Bob")
```

4. **Arbitrary Arguments (`*args`)**: Allows multiple positional arguments.

```python
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))
```

5. **Arbitrary Keyword Arguments (`**kwargs`)**: Allows multiple key-value arguments.

```python
def person_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

person_details(name="Eve", age=22, city="New York")
```

🟢 **Scope of Variables**
Variables can have local or global scope:

- **Local Scope:** Variables inside a function.
- **Global Scope:** Variables outside a function.

```python
global_var = "I am global"

def example():
    local_var = "I am local"
    print(local_var)
    print(global_var)

example()
print(global_var)
```

Using `global` keyword to modify global variables inside a function:

```python
def modify():
    global global_var
    global_var = "Modified global variable"

modify()
print(global_var)
```

---

#### functions.py
```python
def multiply(a, b):
    return a * b

print(multiply(4, 5))
```

#### exercises.py
```python
# 1. Write a function that calculates the area of a circle given the radius.
# 2. Create a function that takes a name as input and prints a greeting.
# 3. Write a function that returns the largest of three numbers.
# 4. Implement a function that checks whether a given number is prime.
# 5. Write a function to generate the Fibonacci series up to a given number.
# 6. Create a function that accepts keyword arguments and prints student details.
```
