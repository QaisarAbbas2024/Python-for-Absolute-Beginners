### **🟢`lists_tuples.py`**
```python
# Creating and accessing lists
fruits = ["apple", "banana", "cherry", "orange"]
print("First fruit:", fruits[0])  # Accessing the first element

# Modifying elements
fruits[1] = "mango"
print("Modified list:", fruits)

# Adding elements
fruits.append("grape")  # Add to the end
fruits.insert(1, "kiwi")  # Insert at index 1
print("After adding elements:", fruits)

# Removing elements
fruits.remove("cherry")  # Removes 'cherry' by value
print("After removing cherry:", fruits)

popped_fruit = fruits.pop()  # Removes the last element and returns it
print("Popped fruit:", popped_fruit)

del fruits[1]  # Deletes item at index 1
print("After deleting second item:", fruits)

# Sorting and reversing lists
numbers = [5, 3, 8, 1, 4]
numbers.sort()  # Ascending order
print("Sorted:", numbers)

numbers.reverse()  # Reverse the list
print("Reversed:", numbers)

# Tuples (Immutable)
colors = ("red", "green", "blue")
print("First color:", colors[0])

# Trying to modify a tuple (will cause an error)
# colors[0] = "yellow"  # Uncommenting this line will raise a TypeError

# Tuple unpacking
x, y, z = colors
print("Extracted Colors:", x, y, z)
```

---

### **🟢`exercises.py`**
```python
# Exercise: Lists and Tuples

# 1. Create a list of numbers and calculate the sum and average.
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Total:", total)
print("Average:", average)

# 2. Reverse a list without using the reverse() method.
original_list = [1, 2, 3, 4, 5]
reversed_list = original[::-1]  # Using slicing
print("Reversed List:", reversed_list)

# 3. Find the largest and smallest numbers in a list.
num_list = [15, 3, 9, 22, 8]
print("Max value:", max(num_list))
print("Min value:", min(num_list))

# 4. Remove duplicates from a list
nums = [1, 2, 3, 4, 2, 3, 5, 6, 1]
unique_nums = list(set(nums))
print("List without duplicates:", unique_nums)

# 5. Check if an item exists in a list
if "apple" in fruits:
    print("Apple is in the list.")

# 6. Tuple unpacking
person = ("Alice", 25, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# 7. Convert a tuple to a list and modify its elements
tuple_colors = ("blue", "green", "yellow")
color_list = list(tuple_colors)
color_list.append("red")
print("Modified list from tuple:", color_list)
```

---
