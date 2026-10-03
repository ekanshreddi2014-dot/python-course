# 1 Project × 40 Marks

# Function Calculator
# Build a calculator that uses a separate function for each operation. The user picks an operation and enters two numbers. Your program handles invalid input and division by zero without crashing.

# What you need to use
# ------------------------------------------------------------------------
# 1.  def and return     →  define 4 functions: add, subtract, multiply, divide
# 2.  try/except         →  catch ZeroDivisionError and ValueError without crashing
# 3.  float(input())     →  to read numbers from the user
# 4.  return values      →  each function must return the correct result
# ------------------------------------------------------------------------

# What you'll be marked on
# ------------------------------------------------------------------------
# 1.  4 functions defined — add, subtract, multiply, divide        →  10 marks
# 2.  Each function returns the correct result for any two numbers →  10 marks
# 3.  ZeroDivisionError caught and prints a clear message          →  10 marks
# 4.  ValueError caught for non-number input                       →   5 marks
# 5.  Program runs without any errors                              →   5 marks
# ========================================================================
# Total  →  40 marks
# ===========================================================
#solution:
def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b
try:
    a = int(input("what is operand 1 : "))
    b = int(input("what is operand 2 : "))
except ValueError:
    print("that is not a number!")
question = input("what is the opration (addition/subtraction/multiplication or division): ").lower()
if question == "addition":
    print(add(a,b))
if question == "subtraction":
    print(sub(a,b))
if question == "multiplication":
    print(mul(a,b))
if question == "division":
    try:
        result1 = div(a,b)
        print(result1)
    except ZeroDivisionError:
        print("please do not divide a number by zero")
    



