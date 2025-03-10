## Day 5: Loops (For and While)
- For Loops
- While Loops
- Break and Continue
- Nested Loops
- Else Clause with Loops
***
Loops allow us to execute a block of code multiple times, making programs more efficient.

### 🟢 For Loops
A for loop is used to iterate over a sequence (list, tuple, string, etc.).

      fruits = ["apple", "banana", "cherry"]
      for fruit in fruits:
          print(fruit)

Using range() with for:

      for i in range(5):  # 0 to 4
          print("Iteration:", i)
***
### 🟢 While Loops
A while loop runs as long as a condition remains True.

      x = 0
      while x < 5:
          print("Value of x:", x)
          x += 1
***
### 🟢 Break and Continue

break exits the loop immediately.

continue skips the current iteration and proceeds to the next.

      for num in range(10):
          if num == 5:
              break  # Stops loop when num is 5
          print(num)

      for num in range(10):
          if num % 2 == 0:
              continue  # Skips even numbers
          print(num)
***
### 🟢 Nested Loops
Loops inside loops are called nested loops.

      for i in range(3):
          for j in range(2):
              print(f"i={i}, j={j}")
***
### 🟢 Else Clause with Loops
A for or while loop can have an else clause that executes when the loop finishes normally (without break).

      for num in range(3):
          print(num)
      else:
          print("Loop completed!")
***
