# ==========================================
# Q1. Simple Calculator Program
# ==========================================

# A. Input & Setup (10 marks)
# 1. Ask the user to input two numbers and 
# 2. Convert inputs into floats (or integers) to allow decimal handling
num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))

# B. Calculations (10 marks)
# Compute the basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2  # Standard division operator

# C. Code Style & Clearly Labeled Outputs (5 marks)
# Print the results with clear labels
print("\n--- Calculation Results ---")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")



# ==========================================
# Q2. User Introduction Program
# ==========================================

# A. Inputs (10 marks)
# Collect name, city, and favourite hobby from the user
name = input("Enter your name: ")
city = input("Enter your city: ")
hobby = input("Enter your favourite hobby: ")

# B. Output (8 marks) & C. Code Quality (2 marks)
# Print a clean, formatted introduction sentence using an f-string
print(f"Hello {name}! You live in {city} and you enjoy {hobby}.")




# ==========================================
# Q3. Temperature Converter
# ==========================================

# A. Input (5 marks)
# 1. Take the temperature in Celsius from the user and 2. Convert it to a float
celsius = float(input("Enter temperature in Celsius: "))

# B. Calculation (10 marks)
# Convert Celsius to Fahrenheit using the formula: F = (C * 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# C. Output (5 marks)
# Print Fahrenheit with a clear message and proper formatting
print(f"Temperature in Fahrenheit is: {fahrenheit}°F")





# ==========================================
# Q4. Billing Program
# ==========================================

# A. Inputs (10 marks)
# Collect the item name, price, and quantity from the user
item_name = input("Enter the item name: ")
price = float(input("Enter the price per item: "))
quantity = float(input("Enter the quantity: ")) # float or int to handle any amount

# B. Calculation (6 marks)
# Compute the total bill using the formula: Total = price * quantity
total = price * quantity

# C. Output (4 marks)
# Print the bill with correct formatting and clear labeling
print(f"Total Bill for {item_name} = {total}")



# ==========================================
# Q5. Student Information Card
# ==========================================

# A. Input (6 marks)
# Collect student name, class/section, and school name from the user
student_name = input("Enter Student Name: ")
class_section = input("Enter Class and Section: ")
school_name = input("Enter School Name: ")

# B. Formatting (7 marks) & C. Code Quality (2 marks)
# Display a cleanly formatted Student ID Card using f-strings and decorative lines
print("\n----- STUDENT ID CARD -----")
print(f"Name: {student_name}")
print(f"Class: {class_section}")
print(f"School: {school_name}")
print("----------------------------")