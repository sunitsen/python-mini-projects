# ==========================================
# 1. DISPLAYING TEXT & CHECKING DATA TYPES
# ==========================================

print("Hello world")

num1 = 20     # Integer data type
num2 = 50.5   # Float data type

# Checking the data types of values and variables using type()
print(type("Hello world"))  # Output: <class 'str'>
print(type(num1))           # Output: <class 'int'>
print(type(num2))           # Output: <class 'float'>

print(200 + 200)            # Simple addition


# ==========================================
# 2. VARIABLES & OUTPUT FORMATTING
# ==========================================

name = "ostad"
print("this is", name)
print("how are you", name)


# ==========================================
# 3. TAKING USER INPUT IN PYTHON
# ==========================================
# Note: input() always returns user input as a string (str) by default.

username = input("enter your name: ")
email = input("enter your email: ")
password = input("enter your password: ")
print(username, email, password)


# ==========================================
# 4. ARITHMETIC OPERATIONS WITH INTEGER CONVERSION
# ==========================================
# Using int() to convert user input from string to integer for math

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# ==========================================
# 5. TYPE CONVERSION (USING FLOAT)
# ==========================================
# Using float() to handle decimal numbers from user input

num1 = float(input("Enter num1 (decimal): "))
num2 = float(input("Enter num2 (decimal): "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)


# ==========================================
# 6. STRING CONCATENATION AND REPETITION
# ==========================================

name = "sunit"
greet = "Hello "

# String Concatenation (+): Joining strings together
newVer = greet + name

print("-" * 30)  # Prints the '-' character 30 times as a separator line
print(newVer)

# String Repetition (*): Repeating a string multiple times
print("hello" * 30)