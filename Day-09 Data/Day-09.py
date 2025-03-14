#### **file_handling.py**  
```python
# Writing to a file
with open("test.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("This is the second line.\n")

# Reading from a file
with open("test.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending to a file
with open("test.txt", "a") as file:
    file.write("This line is appended.\n")

# Reading file line by line
with open("test.txt", "r") as file:
    for line in file:
        print("Reading Line:", line.strip())

# Handling file errors with try-except
try:
    with open("non_existent_file.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("Error: File not found.")
```

#### **exercises.py**  
```python
# 1. Write a program to read the contents of a file and print them.
# 2. Create a program to append data to an existing file.
# 3. Write a program to count the number of words in a file.
# 4. Create a program that checks if a file exists before reading it.
# 5. Read a file and print only the first 3 lines.
```
