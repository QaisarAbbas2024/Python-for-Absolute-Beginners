## 🔵 Day 7: Lists and Tuples
- Creating Lists and Tuples
- Accessing and Modifying Elements
- Looping Through Lists
***
Lists and tuples are fundamental data structures in Python that allow storing multiple values in a single variable.  

### 🟢 **Lists in Python**
A **list** is an ordered, mutable (changeable) collection that can store different data types.  

#### **Creating Lists**
```python
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed = [1, "hello", 3.14, True]
```

#### **Accessing and Modifying Elements**
```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # Output: apple
fruits[1] = "mango"  # Modify an element
print(fruits)  # ['apple', 'mango', 'cherry']
```

#### **Adding Elements**
```python
fruits.append("orange")  # Adds to the end
fruits.insert(1, "grape")  # Inserts at index 1
```

#### **Removing Elements**
```python
fruits.remove("banana")  # Removes by value
popped_item = fruits.pop()  # Removes last item
del fruits[0]  # Deletes by index
```

#### **Looping Through a List**
```python
for fruit in fruits:
    print(fruit)
```

---

### 🟢 **Tuples in Python**
A **tuple** is similar to a list but **immutable** (unchangeable). Tuples are used for fixed collections of items.  

#### **Creating Tuples**
```python
colors = ("red", "green", "blue")
single_item = ("hello",)  # Note the comma!
```

#### **Accessing Tuple Elements**
```python
print(colors[0])  # Output: red
```

#### **Tuple Unpacking**
```python
x, y, z = colors
print(x)  # red
```

---

### 🟢 **List vs Tuple**
| Feature | List | Tuple |
|---------|------|-------|
| Mutable? | ✅ Yes | ❌ No |
| Performance | Slower | Faster |
| Syntax | `[]` | `()` |

---

### 🟢 **Extra: List Comprehensions**
A compact way to create lists.
```python
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```
