### **🔵 Examples for `dictionaries_sets.py`**
```python
# Creating and accessing a dictionary
person = {"name": "John", "age": 25, "city": "New York"}
print("Name:", person["name"])  # Accessing a value

# Adding and updating key-value pairs
person["profession"] = "Engineer"
person["age"] = 26  # Updating a value
print(person)  

# Removing an item
del person["city"]
print("After deletion:", person)

# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")

# Creating and manipulating sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Set operations
print("Union:", A | B)  # {1, 2, 3, 4, 5, 6}
print("Intersection:", A & B)  # {3, 4}
print("Difference (A - B):", A - B)  # {1, 2}
print("Symmetric Difference:", A ^ B)  # {1, 2, 5, 6}

# Adding and removing elements from a set
A.add(7)
A.remove(2)
print("Updated Set A:", A)
```

---

### **🔵 Updated Exercises for `exercises.py`**
```python
# 1. Create a dictionary of students with their grades and print it.
students = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}
print("Student Grades:", students)

# 2. Find the union of two sets.
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
union_set = set1 | set2  # or set1.union(set2)
print("Union of sets:", union_set)

# 3. Write a program to count the occurrences of each character in a string.
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print("Character Count:", char_count)

# 4. Remove duplicate elements from a list using a set.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique Numbers:", unique_numbers)

# 5. Check if a given key exists in a dictionary.
student_info = {"name": "Alice", "age": 21, "grade": "A"}
key_to_check = "age"
print(f"Does '{key_to_check}' exist in dictionary?", key_to_check in student_info)
```

---
