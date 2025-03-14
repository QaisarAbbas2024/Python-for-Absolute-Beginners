## **🔵 Day 8: Dictionaries and Sets**
- Creating and Accessing Dictionaries
- Adding and Removing Items
- Set Operations
---
Dictionaries and sets are fundamental data structures in Python. **Dictionaries** store key-value pairs, while **sets** hold unique unordered items.

### **🟢 Creating and Accessing Dictionaries**  
A **dictionary** (`dict`) is a collection of key-value pairs. Each key must be unique and immutable (e.g., strings, numbers, or tuples), while values can be of any data type.  

#### **Example: Creating a Dictionary**
```python
# Creating a dictionary
student = {
    "name": "Alice",
    "age": 22,
    "major": "Physics"
}

# Accessing values
print(student["name"])  # Output: Alice
print(student.get("age"))  # Output: 22
```

#### **Updating Values in a Dictionary**
```python
student["age"] = 23
print(student)  # {'name': 'Alice', 'age': 23, 'major': 'Physics'}
```

#### **Iterating Over a Dictionary**
```python
for key, value in student.items():
    print(key, ":", value)
```

---

### **🟢 Adding and Removing Items in Dictionaries**
#### **Adding a New Key-Value Pair**
```python
student["GPA"] = 3.8
print(student)  
# {'name': 'Alice', 'age': 23, 'major': 'Physics', 'GPA': 3.8}
```

#### **Removing an Item**
```python
del student["major"]  # Removes "major" from the dictionary
print(student)
```

#### **Using `pop()` Method**
```python
gpa = student.pop("GPA")  # Removes and returns the value
print("Removed GPA:", gpa)
```

---

### **🟢 Set Operations**
A **set** is an unordered collection of unique elements. It does not allow duplicate values.

#### **Creating a Set**
```python
fruits = {"apple", "banana", "cherry", "apple"}  # Duplicate "apple" will be ignored
print(fruits)  # Output: {'banana', 'cherry', 'apple'}
```

#### **Adding and Removing Elements**
```python
fruits.add("mango")  # Add an element
fruits.remove("banana")  # Remove an element
print(fruits)
```

#### **Set Operations (Union, Intersection, Difference)**
```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)  # Union: {1, 2, 3, 4, 5, 6}
print(A & B)  # Intersection: {3, 4}
print(A - B)  # Difference: {1, 2}
print(A ^ B)  # Symmetric Difference: {1, 2, 5, 6}
```

---
