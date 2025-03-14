## **🔵 Day 9: File Handling**
Handling files in Python allows you to read, write, and manage data stored in text or other file formats. Python provides built-in functions for file operations.  

### **📌 Topics Covered:**
- Reading and Writing Files  
- Working with Text Files  
- Exception Handling  
- File Modes (`r`, `w`, `a`, `r+`)  
- Working with `with` Statement  
- Handling File Paths  
- Handling Different File Formats (Optional)  

---

### **🟢 Reading and Writing Files**
Python provides the `open()` function to work with files.  

#### **Opening and Reading a File**
```python
# Open file in read mode
file = open("example.txt", "r")

# Read full content
content = file.read()
print(content)

# Close the file
file.close()
```

#### **Reading a File Line by Line**
```python
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes extra spaces/newline
```

#### **Writing to a File**
```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a second line.")
```

#### **Appending to a File**
```python
with open("output.txt", "a") as file:
    file.write("\nAppending a new line.")
```

---

### **🟢 File Modes**
| Mode  | Description |
|-------|------------|
| `r`   | Read (default). File must exist. |
| `w`   | Write. Overwrites if file exists. Creates new file if not. |
| `a`   | Append. Adds data to the end of the file. |
| `r+`  | Read and Write. Keeps existing data. |
| `w+`  | Read and Write. Overwrites existing data. |

---

### **🟢 Exception Handling in File Handling**
Handling exceptions prevents errors from crashing your program.  

#### **Handling File Not Found Error**
```python
try:
    with open("non_existent.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
```

#### **Handling Other I/O Errors**
```python
try:
    with open("output.txt", "w") as file:
        file.write("Writing to file.")
except IOError:
    print("Error in file operation.")
finally:
    print("File operation complete.")
```

---

### **🟢 Working with File Paths**
Use the `os` module to work with file paths.
```python
import os

# Get current directory
print("Current Directory:", os.getcwd())

# Check if file exists
if os.path.exists("example.txt"):
    print("File exists!")
else:
    print("File not found.")
```

---

### **💡 Key Takeaways**
✔ Always **close** files after use (`with` statement is preferred).  
✔ Use **exception handling** to manage errors.  
✔ Know **file modes** (`r`, `w`, `a`) to prevent accidental overwrites.  
✔ Use **file paths correctly** when working with multiple directories.  

---
