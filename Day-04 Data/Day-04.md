## Day 4: Conditional Statements
- If, Else, Elif
- Nested Conditions
- Logical Conditions
- Ternary Operator (Conditional Expressions)
- Match Case (Alternative to If-Elif)
***
Conditional statements allow us to control the flow of a program based on conditions.

### 🟢 If, Else, Elif
Conditional statements execute different blocks of code depending on whether conditions evaluate to True or False.

      x = 10
      y = 20
      if x > y:
          print("x is greater than y")
      elif x == y:
          print("x is equal to y")
      else:
          print("x is less than y")
***
### 🟢 Nested Conditions
Conditions can be nested to evaluate multiple levels of logic.

      num = 15
      if num > 0:
          print("Positive number")
          if num % 2 == 0:
              print("Even number")
          else:
              print("Odd number")
      else:
          print("Negative number")
***
### 🟢 Logical Conditions
Python provides logical operators (and, or, not) to combine multiple conditions.

      age = 25
      income = 40000
      if age > 18 and income > 30000:
          print("Eligible for loan")
      else:
          print("Not eligible for loan")
***
### 🟢 Ternary Operator (Conditional Expressions)
A compact way to write if-else conditions.

      x = 10
      y = 20
      min_value = x if x < y else y
      print("The smaller value is", min_value)
***
### 🟢 Match Case (Alternative to If-Elif)
Python 3.10 introduced match for cleaner conditionals.

      def day_type(day):
          match day:
              case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
                  return "Weekday"
              case "Saturday" | "Sunday":
                  return "Weekend"
              case _:
                  return "Invalid day"
      
      print(day_type("Sunday"))
***
