
"""## Table of Contents
- Introduction to file
- Create and write to a file
- Read content from a file
- Append content in a file
- File Handling using Context Manager
- File handling issues
- Introduction to OOP
- Class and Object
- Attributes and Methods
- Four Pillars of OOP
- Encapsulation
- Inheritance
- Polymorphism
- Abstraction
- Summary: Four Pillar of OOP
- Python OOP Syntax Guide
- Mini Project
- OOP Practice Questions
"""

from google.colab import drive
drive.mount('/content/drive')

# registration
username = input("Enter your username: ")
email = input("Enter your email")
password = input("Enter your password")


# save
print(username)
print(email)
print(password)

# login

print("User login page")
print("="*20)
user_name = input("Enter username to login: ")
pass_word = input("Enter pass: ")


if (username == user_name) and (pass_word == password):
  print("You are logged in; welcome to the website")
else:
  print("credentials did not match")

"""## Introduction to file

#### Why Do We Need Files?
Imagine:

- Your app closes ❌
- Variables disappear ❌
- Data is lost ❌
  
👉 Files solve this problem.

```python
# Variables are temporary
user = "Alice"
print(user)

# After program ends → data gone
```

#### Real-World Use Cases
- Login logs
- Exam results
- Contacts
- Transaction history


#### File Handling Basic Syntax
```python
file = open(filepath, mode)
```

<div style="display: flex; gap: 20px; align-items: flex-start;">
<div>
    
| Mode  | Meaning                  |
| ----- | ------------------------ |
| `"r"` | Read (default)           |
| `"w"` | Write (overwrite)        |
| `"a"` | Append (add at end)      |

</div>
</div>

##  Create and write to a file
```python
file = open(filepath, "w")  # open file in write mode
file.write("Hello World")
file.close()     # file must be closed
```
- Write mode (`"w"`) overwrites existing content.
- If the file does not exist, it will be created
"""

file = open("/content/drive/MyDrive/file_test/sample2.txt", "w")

file.write("Hello World\n")
file.write("Ostad\n")
file.write("Mastering Python : From Zero to Hero\n")

file.close()

# open(filepath, mode)

# mode: write (w), read(r), append(a)

file = open("/content/drive/MyDrive/file_test/sample.txt", "r")

content = file.read()

file.close()


print(content)

file = open("/content/drive/MyDrive/file_test/sample.txt", "a")

file.write("New content added\n")
file.write("Hello Bangladesh\n")

file.close()

# write mode

# 1. if not exists -> creates new file + add content

# 2. if exists -> overwrite

"""## Read content from a file

#### Read entire file
```python
file = open(filepath, "r")  # open file in read mode
content = file.read()
print(content)
file.close()                # file must be closed
```

#### read specific numbers of characters
```python
file = open(filepath, "r")
content = file.read(30)     # reads first 30 characters from the file
print(content)
file.close()                # file must be closed
```

#### Read All Lines (as a List)
```python
file = open(filepath, "r")
lines = file.readlines()   # returns a list of lines
print(lines)               # Example Output: ["line1\n", "line2\n"]
file.close()               # file must be closed
```

#### Read line by line
```python
file = open(filepath, "r")
for line in file:
    print(line)                 # you may use print(line.strip()) to remove extra new line character
file.close()                    # file must be closed
```

"""

file = open("/content/drive/MyDrive/file_test/sample.txt", "r")
content = file.read()
print(content)
file.close()

file = open("/content/drive/MyDrive/file_test/sample.txt", "r")
content = file.read(30)
print(content)
file.close()

file = open("/content/drive/MyDrive/file_test/sample.txt", "r")
lines = file.readlines()
print(lines)
file.close()

file = open("/content/drive/MyDrive/file_test/sample.txt", "r")
for line in file.readlines():
    print(line.strip())
file.close()

file = open("/content/drive/MyDrive/file_test/sample.txt", "r")
for line in file:
    print(line.strip())
file.close()

"""## Append content in a file

```python
file = open(filepath, "a")       # open in append mode
file.write("New content added")  
file.close()                    # file must be closed
```

- Append mode (`"a"`) adds new content at the end of the file.
- It does NOT overwrite existing content.
- If the file does not exist, it will be created.
"""

file = open("/content/drive/MyDrive/file_test/sample.txt", "a")
file.write("New content added\n")
file.close()

file = open("/content/drive/MyDrive/file_test/sample.txt", "r")
print(file.read())
file.close()

file = open("/content/drive/MyDrive/file_test/user_list.txt", "w")
file.write("user3: Shovon\n")
file.write("user4: Sayem\n")
file.close()

# existing file - w - replace
# existing file - a -

# create + write - w
# write - a

"""## File Handling using Context Manager

Instead of manually closing files, use `with`

```python
# writing to a file
with open(filepath, "w") as file:
    file.write("Hello World")

# reading from a file
with open(filepath, "r") as file:
    content = file.read()
    print(content)

# appending to a file
with open(filepath, "a") as file:
    file.write("New Content")
    print(content)
```

- File is automatically closed. No need to manually close the file.
- Cleaner and safer code
"""

file = open("/content/drive/MyDrive/file_test/sample2.txt", "w")

file.write("Hello World\n")
file.write("Ostad\n")
file.write("Mastering Python : From Zero to Hero\n")


file.close()

with open("/content/drive/MyDrive/file_test/sample2.txt", "w") as file:
    file.write("Hello World\n")
    file.write("Ostad\n")
    file.write("Mastering Python : From Zero to Hero\n")


# network



with open("/content/drive/MyDrive/file_test/sample2.txt", "r") as f:
    content = f.read()
    print(content)

with open("/content/drive/MyDrive/file_test/sample2.txt", "r") as file:
    for line in file:
        print(line)

with open("/content/drive/MyDrive/file_test/sample2.txt", "a") as file:
    file.write("New content appended\n")

with open("/content/drive/MyDrive/file_test/sample2.txt", "r") as file:
    print(file.read())

with open("/content/drive/MyDrive/file_test/users.txt", "w") as file:
    file.write("user1: saihan\n")
    file.write("user2: shovon\n")
    file.write("user3: sadia\n")
    file.write("user4: sayma\n")


with open("/content/drive/MyDrive/file_test/users.txt", "a") as file:
    file.write("user5: sayem\n")
    file.write("user6: nirob\n")


with open("/content/drive/MyDrive/file_test/users.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("users.txt", "a") as file:
    file.write("user7: akash\nuser8: hasan\n")

with open("users.txt", "a") as file:
    file.write("user9: samia\n")
    file.write("user10: nira\n")

with open("users.txt", "r") as file:
    for line in file:
        print(line.strip())

"""## File handling issues

### `1.` wrong operation mode e.g. trying to read while using write or read mode

##### Trying to write to a file which is opened in read (`"r"`) mode
```python
with open("sample.txt", "r") as file:
    file.write("Hello")  # Will raise an error, file opened in read mode.
```
##### Trying to read from a file which is opened in write (`"w"`) mode
```python
with open("data.txt", "w") as file:
    file.read()  # Will raise an error, file opened in write mode.
```

##### Solution: Always choose the correct mode:

- If you want to read → use `"r"`
- If you want to write → use `"w"`
- If you want to add → use `"a"`
   
### `2.` Accidentally overwriting a file with write mode
  
Write mode (`"w"`) deletes all previous content before writing.
```python
file = open("data.txt", "w")
file.write("\nNew Content")
file.close()
```
If `data.txt` already had important data → it is permanently lost.

#### Solution:
- Use `"a"` (append mode) if you want to keep old data:
```python
with open("data.txt", "a") as file:
    file.write("\nNew Content")
```
- Or check before writing:
```python
import os

if not os.path.exists("data.txt"):
    with open("data.txt", "w") as file:
        file.write("\nNew Content")
```
- Or open in `"x"` mode (creates file only if it does NOT exist):
    
```python
with open("data.txt", "x") as file:
    file.write("Hello World")
```
"""

with open("sample.txt", "r") as file:
    file.write("Hello")  # Will raise an error, file opened in read mode.

with open("data.txt", "w") as file:
    file.read()  # Will raise an error, file opened in write mode.

with open("data.txt", "x") as file:
    file.write("Hello World")  # if data.txt exists, file won't created, will raise an error







"""## Introduction to OOP

OOP means Object Oriented Programming.

#### The Problem...

Let’s say you're building a simple ML system for students.

You store student data and calculate their result.

❌ Without OOP (just functions + variables)
```python
# Student 1
student1_name = "Rafin"
student1_marks = [80, 75, 90]

# Student 2
student2_name = "Shafin"
student2_marks = [60, 65, 70]

# student 2
student3_name = "Sadai"
student2_marks = [70, 80,57]

def calculate_average(marks):
    return sum(marks) / len(marks)

def print_result(name, marks):
    avg = calculate_average(marks)
    print(f"{name} Average: {avg}")

print_result(student1_name, student1_marks)
print_result(student2_name, student2_marks)
```

#### Problems here
1. ❌ Data is scattered
    - name and marks are separate variables
    - No clear connection between them

2. ❌ Not scalable
Imagine 1000 students:

```python
student1000_name = ...
student1000_marks = ...
```
💀 This becomes unmanageable

3. ❌ Hard to extend

Now you want to:

- add attendance
- add grade
- add prediction (ML model)

You’ll need to:

- create more variables
- update all functions

Messy very quickly.

4. ❌ No structure / real-world mapping

In real life - A student has name, marks, attendance

But here everything is disconnected.

**Solution → OOP (Object Oriented Programming)**

#### WHY OOP?

OOP solves this by grouping:
👉 Data + Behavior together

Instead of:

```
name → separate
marks → separate
functions → separate
```

We do:
```
Student = (name + marks + functions)
```

#### Same thing using OOP
```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")
```

✅ Create objects
```python
s1 = Student("Rafin", [80, 75, 90])
s2 = Student("Shafin", [60, 65, 70])

s1.print_result()
s2.print_result()
```
"""



# Student 1
student1_name = "Rafin"
student1_marks = [80, 75, 90]

# Student 2
student2_name = "Shafin"
student2_marks = [60, 65, 70]

# student 3
student3_name = "Sadai"
student2_marks = [70, 80,57]

def calculate_average(marks):
    return sum(marks) / len(marks)

def print_result(name, marks):
    avg = calculate_average(marks)
    print(f"{name} Average: {avg}")

print_result(student1_name, student1_marks)
print_result(student2_name, student2_marks)
print_result(student3_name, student3_marks)

mylist = list(["apple", "banana", "mango"])

mylist.append("cherry")

mylist.sort()

print(mylist)

print(type(mylist))

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")

    def check_grade(self):
        avg = self.calculate_average()
        if avg >= 80:
            print("A")
        elif avg >= 70:
            print("B")
        else:
            print("C")



s1 = Student("Rafin", [80, 75, 90])
s2 = Student("Shafin", [60, 65, 70])
s3 = Student("Sadia", [70, 80, 90])


s1.print_result()
s1.check_grade()
print()
s2.print_result()
# s2.check_grade()

l = [1, 7, 9]
print(type(l))
l.pop()

students = [
    Student("Rafin", [80, 75, 90]),
    Student("Shafin", [60, 65, 70]),
    Student("Shakil", [80, 75, 90]),
    Student("Jihad", [60, 65, 70]),
    Student("Samia", [60, 65, 70]),
    Student("Sadia", [60, 69, 70]),
    Student("Nirob", [60, 65, 70]),
    Student("Shovon", [60, 65, 70])
]


for std in students:
    std.calculate_average()
    std.print_result()
    # std.check_grade()
    print()

# class -> blueprint , empty form
# object -> filluped form

"""## Class and Objects

![](https://miro.medium.com/1*NxXw72-CDGp7b7pz2kga5g.png)

![](https://nonlineardata.com/wp-content/uploads/2020/11/Car_Class.png)

#### 1. What is a Class in Python?

A `class` is like a blueprint/template.

👉 Think of designing a “Car”:

- Every car has a color
- Every car has a brand
- Every car can drive

So, a class defines:

- data (attributes) → color, brand
- behavior (methods) → drive()

```python
class Car:
    pass
```
#### 2. What is an Object?

An `object` is a real instance of a `class`.

👉 If `class` = blueprint, then `object` = actual thing built from it

```python
car1 = Car()
car2 = Car()
```

Now `car1` and `car2` are objects of class `Car`.



You can think of class/object in other ways:
- Class = Form
- Object = Fille form
"""

# class (oop) -> data, behaviou/tool/method/funtion

class Car:
    def __init__(self, color, brand, model, build_year): # constructor function
        self.color = color
        self.brand = brand
        self.model = model
        self.build_year = build_year

    def drive(self):
        print(f"{self.brand} is driving")

    def breaking(self):
        print("breaking the car...!!!")

    def stop(self):
        print(f"{self.brand} stopping..")



car1 = Car("Red", "Toyota", "Camry", "2024")
car2 = Car("Blue", "BMW", "X5", "2023")

car1.drive()
car2.drive()

car1.breaking()

# form -> class
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")

# filled up form -> object
s1 = Student("Rafin", [80, 75, 90])
s2 = Student("Shafin", [60, 65, 70])

s1.calculate_average()

"""## Attributes and Methods
- Attributes are data inside object. It store information.
- Methods are functions innside class. It defines behavior

- Constructor Method (`__init__`): The constructor is a special method that runs automatically when you create an object
- `self` → refers to current object

- One-Line Intuition
    - Attributes = WHAT the object has
    - Methods = WHAT the object does
    - Constructor = HOW the object is created




![](https://media.geeksforgeeks.org/wp-content/uploads/20250906151500826906/420046617.webp)
"""

# snake case
fathers_name
mohers_name


# CamelCase

FathersName
MothersName

# defining class
class StudentIden():
    pass

# creating object from the class
s = Student()

class Student():
    # constructor method
    def __init__(self, name, marks, attendence=80):
        self.name = name                # attirbute
        self.marks = marks              # attribute
        self.attendence = attendence    # default attribute

    def calculate_average(self):
        print(sum(self.marks) / len(self.marks))

s1 = Student("Sadia", [70, 80])  # default value of attendence is used

print(s1.marks)       # attirbute
print(s1.name)        # attirbute
print(s1.attendence)  # default attribute

s2 = Student("Rafin", [60, 90], 50) #  default value of attendence is overwriten

print(s2.marks)
print(s2.name)
print(s2.attendence)


print(s2.calculate_average())

s3 = Student(name="Shafin", attendence=50, marks=[60, 90])

print(s3.marks)
print(s3.name)
print(s3.attendence)

class Student():
    # constructor method / dunder method (double underscore -> dunder)
    def __init__(self, name, marks, attendence=80):
        self.name = name
        self.marks = marks
        self.attendence = attendence

    # method
    def calculate_avg(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

    # method
    def display_student(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Sadia", [10, 20])

print(s1.marks)
print(s1.name)
print(s1.attendence)
# marks, name, attendence -> attribute

s1.calculate_avg()   # method
s1.display_student()

## Summary

# Defining a class
class Car():
    # construtor method
    def __init__(self, brand, color):
        self.brand = brand     # attribute
        self.color = color     # attribute

    # method
    def start_engine(self):
        print(f"{self.brand} engine starting..Whirrrr... vroom!")


    def get_color(self):
        return self.color


# Creating objects from a class
car1 = Car("Toyota", "White")
car2 = Car(brand="BMW", color="Black")

# Accessing data of an object
print(f"Car 1 color: {car1.color}")
print(f"Car 2 brand: {car2.brand}")

# Calling methods
car1.start_engine()
car2.start_engine()

"""## Four Pillars of OOP

The four pillars of Object-Oriented Programming (OOP)—`Encapsulation`, `Abstraction`, `Inheritance`, and `Polymorphism` are foundational principles that make code modular, reusable, and maintainable.

They enable developers to wrap data with behavior, hide complexity, create hierarchical relationships, and allow objects to take on multiple forms

## Encapsulation
💡 **Idea:** Encapsulation means hiding internal data and allowing access only through methods.

**Real-life analogy**

- ATM machine

- You cannot touch balance directly

- You must use deposit() / withdraw()
"""

class ATM:
    def __init__(self, balance):
        self.__balance = balance  # double underscore makes a property/attribute private


    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount

atm1 = ATM(200)

# atm1.__balance  # you cannont access balance directly. since it is a private data
atm1.check_balance()
atm1.deposit(50)
atm1.check_balance()
atm1.withdraw(30)
atm1.check_balance()

atm1.__balance  # private attribute

atm1 = ATM(200)

# __balance is internally accessed
atm1.check_balance()
atm1.deposit(50)
atm1.check_balance()
atm1.withdraw(30)
atm1.check_balance()



"""## Inheritance
💡 Idea: Create specialized classes from a base class that inherits methods and properties from the base class

![image.png](https://media.geeksforgeeks.org/wp-content/uploads/20251009164207176209/animal_class.webp)


**Using Inheritance:**
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

     def eat(self):
        print(f"{self.name} is eating.")

# Child classes
class Dog(Animal):
    pass

class Cat(Animal):
    pass

class Cow(Animal):
    pass

# Using the classes
dog = Dog("Max")
cat = Cat("Milo")
cow = Cow("Bessie")

dog.eat()
cat.eat()
cow.eat()
```
`Output:`
```shell
Max is eating..
Milo is eating..
Bessie is eating..
```
**Benefit**
- Reuse base logic
- You write eat() once, all animals can use it.
- If later you add sleep() to Animal, all animals get it automatically. ✅


**N.B.** The `pass` keyword
- `pass` is a placeholder that does nothing.
- Python requires some code inside blocks like classes, functions, or loops.
- If you don’t want to write the code yet, you can use `pass` so Python won’t give an error.


**Without Inheritance:**
```python
class Dog:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")

class Cat:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")

class Cow:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating.")


# Using the classes
dog = Dog("Max")
cat = Cat("Milo")
cow = Cow("Bessie")

dog.eat()
cat.eat()
cow.eat()
```
`Output:`
```shell
Max is eating..
Milo is eating..
Bessie is eating..
```

technically, you can just create 3 separate classes (Dog, Cat, Cow) without a parent Animal. But inheritance helps a lot when your program grows. Here’s why:

- You’re repeating the same `__init__()` and `eat()` code 3 times.
- Hard to maintain — if you want to change `eat()`, you have to change it in 3 places.



![](https://www.learnbyexample.org/wp-content/uploads/python/Python-Inheritance-Illustration.png)




#### Another Example


```python

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")

class OnlineStudent(Student):
    def __init__(self, name, marks, internet_score):
        super().__init__(name, marks)
        self.internet_score = internet_score

class OfflineStudent(Student):
    def __init__(self, name, marks, attendance):
        super().__init__(name, marks)
        self.attendance = attendance



students = [
    OnlineStudent("Hasan", [80, 90], 82),
    OfflineStudent("Shayra", [70, 60], 63)
]

for s in students:
    print(f"{s.name}: {s.calculate_average()}")
```
`Output:`
```shell
Hasan: 85.0
Shayra: 65.0
```


**Benefit**
- Reuse base logic
- You didn't have to rewrite the `calculate_average()` for the child classes.  
"""

class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")

class OnlineStudent(Student):
    def __init__(self, name, marks, internet_score):
        super().__init__(name, marks)
        self.internet_score = internet_score

class OfflineStudent(Student):
    def __init__(self, name, marks, attendance):
        super().__init__(name, marks)
        self.attendance = attendance


students = [
    OnlineStudent("Hasan", [80, 90], 82),
    OfflineStudent("Shayra", [70, 60], 63)
]

for s in students:
    print(f"{s.name}: {s.calculate_average()}")

# Parent class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting.")

    def stop(self):
        print(f"{self.brand} has stopped.")

# Child classes
class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} says Beep! 🚗")

class Bike(Vehicle):
    def honk(self):
        print(f"{self.brand} says Beep Beep! 🏍️")

class Truck(Vehicle):
    def honk(self):
        print(f"{self.brand} says HOOOOONK! 🚚")

class Bus(Vehicle):
    def honk(self):
        print(f"{self.brand} says PEEP PEEP! 🚌")

# Using the classes
my_car = Car("Toyota")
my_bike = Bike("Yamaha")
my_truck = Truck("Volvo")
my_bus = Bus("Mercedes")

# Calling methods
my_car.start()
my_car.honk()

my_bike.start()
my_bike.honk()

my_truck.start()
my_truck.honk()

my_bus.start()
my_bus.honk()

"""## Polymorphism
💡 **Idea:** Same method name → different implementation

```python
# parent class
class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")

# child class
class OnlineStudent(Student):  
    def __init__(self, name, marks, online_attendence):
        super().__init__(name, marks)
        self.online_attendence = online_attendence

    def calculate_final_score(self):
        avg = self.calculate_average()
        return avg*0.9 + self.online_attendence * 0.1

# child class
class OfflineStudent(Student):   
    def __init__(self, name, marks, offline_attendence):
        super().__init__(name, marks)
        self.offline_attendence = offline_attendence

    def calculate_final_score(self):
        avg = self.calculate_average()
        return avg*0.7 + self.offline_attendence * 0.3




students = [
    OnlineStudent("Hasan", [80, 90], 82),
    OfflineStudent("Shayra", [70, 60], 63)
]


for s in students:
    print(f"Name: {s.name} | Final Score: {s.calculate_final_score()}")
```
`Output:`
```shell
Name: Hasan | Final Score: 84.7
Name: Shayra | Final Score: 64.4
```

**Magic**
- Same function call → calculate_final_score()
- Different logic runs depending on object type


![](https://www.c-sharpcorner.com/UploadFile/433c33/polymorphism-in-java/Images/0.jpg)

**Another Example**
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child classes
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof! 🐶")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow! 🐱")

class Cow(Animal):
    def speak(self):
        print(f"{self.name} says Moo! 🐮")

# Using the classes
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

dog.speak()
cat.speak()
cow.speak()
```
`Output:`
```shell
Max says Woof! 🐶
Milo says Meow! 🐱
Bessie says Moo! 🐮
```

**Magic**
- Same method call → `speak()`
- Different logic runs depending on animal type
"""

# parent class
class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        return sum(self.marks) / len(self.marks)

    def print_result(self):
        avg = self.calculate_average()
        print(f"{self.name} Average: {avg}")

# child class
class OnlineStudent(Student):
    def __init__(self, name, marks, online_attendence):
        super().__init__(name, marks)
        self.online_attendence = online_attendence

    def calculate_final_score(self):
        avg = self.calculate_average()
        return avg*0.9 + self.online_attendence * 0.1

# child class
class OfflineStudent(Student):
    def __init__(self, name, marks, offline_attendence):
        super().__init__(name, marks)
        self.offline_attendence = offline_attendence

    def calculate_final_score(self):
        avg = self.calculate_average()
        return avg*0.7 + self.offline_attendence * 0.3



students = [
    OnlineStudent("Hasan", [80, 90], 82),
    OfflineStudent("Shayra", [70, 60], 63)
]


for s in students:
    print(f"Name: {s.name} | Final Score: {s.calculate_final_score()}")

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child classes
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof! 🐶")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow! 🐱")

class Cow(Animal):
    def speak(self):
        print(f"{self.name} says Moo! 🐮")


# Using the classes
dog = Dog("Max")
cat = Cat("Milo")
cow = Cow("Bessie")

dog.speak()
cat.speak()
cow.speak()

mylist = list([1, 7, 2, 3, 5])

mylist.sort()

print(mylist)

"""## Abstraction
💡 **Idea:** User doesn’t need to know internal details

**Real-Life Analogy:**
🧠 Think of a remote control.
- You know it can turn on/off and change channels.
- You don’t need to know how the electronics inside work.
- That’s abstraction — hiding details, showing only functionality.

**Another Example**
🧠 Think ML model

User just does:
```
model.predict(data)
```

They don’t care:

- preprocessing
- feature engineering
- math


**Abstraction in ATM**
```python
class ATM:
    def __init__(self, balance):
        self.__balance = balance  # double underscore makes a property/attribute private

    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount


atm = ATM(200)

atm.check_balance()
atm.deposit(50)       
atm.check_balance()
atm.withdraw(30)     
atm.check_balance()
```


**You don’t need to know how the ATM stores money inside. You just know how to `check`, `deposit`, or `withdraw` — that’s `abstraction`!**
"""

class ATM:
    def __init__(self, balance):
        self.__balance = balance  # double underscore makes a property/attribute private

    def check_balance(self):
        print(self.__balance)

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount


atm = ATM(200)

atm.check_balance()
atm.deposit(50)
atm.check_balance()
atm.withdraw(30)
atm.check_balance()



"""## Summary: Four Pillars of OOP

| **Concept**        | **Simple Definition**                                                      | **Example**                                                                              |
| ----------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Encapsulation** | Keep the important data safe inside the class, and give methods to use it. | `ATM` example: `__balance` is hidden, we use `deposit()` & `withdraw()`                  |
| **Abstraction**   | Show only what is needed, hide the complicated details.                    | `ATM`: you just know how to `check_balance()` and `deposit()`, not how balance is stored |
| **Inheritance**   | Let a class use code from another class so you don’t have to rewrite it.   | `Vehicle` → `Car`, `Bike`, `Truck`, `Bus`                                                |
| **Polymorphism**  | Different classes can do the same thing in their own way.                  | `Dog`, `Cat`, `Cow` all have `speak()`, but each says something different                |


**💡Memory Tip for Students:**

- Encapsulation & Abstraction → protect and hide internal details
- Inheritance & Polymorphism → reuse and customize behavior
"""

# def user_story   - snake_case
# class UserStory - CamelCase

# BCarra

"""## Python OOP Syntax Guide

1️⃣ Creating a Class
```python
class ClassName:
    pass
```
A class is like a blueprint for creating objects.

2️⃣ Creating an Object
```python
obj = ClassName()
```
This creates an instance (object) of the class.

3️⃣ Constructor (__init__)
```python
class Car:
    def __init__(self, brand):
        self.brand = brand
```
- __init__ is a constructor → runs automatically when object is created.
- Used to initialize values (attributes).
  
4️⃣ self Keyword
```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print(self.brand)
```
- self means `this object`.
- It is used to access variables and methods inside the class.
  
5️⃣ Adding Methods
```python
class Car:
    def start(self):
        print("Car is starting 🚗")
```
Methods are just functions inside a class.

6️⃣ Inheritance
```python
class Vehicle:
    def start(self):
        print("Vehicle is starting")

class Car(Vehicle):  # inherits from Vehicle
    pass
```
Car can use all methods of Vehicle.

7️⃣ Using super()
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)  # call parent constructor
        self.model = model
```
- `super()` is used to call parent class methods.
- Mostly used with constructors.
  
8️⃣ Method Overriding
```python
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof 🐶")
```
Child class changes the parent method behavior.

9️⃣ Full Example (Everything Together)
```python
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print(f"{self.brand} is starting")

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show(self):
        print(self.brand, self.model)

car = Car("Toyota", "Corolla")

car.start()   # inherited
car.show()    # own method
```

✅ Quick Cheat Sheet
- Class → `class ClassName:`
- Object → `obj = ClassName()`
- Constructor → `def __init__()`
- Inheritance → `class Child(Parent):`
- `self` → current object
- `super()` → call parent methods


💡 Simple Way to Remember:

- Class = blueprint
- Object = real thing
- self = current object
- constructor = setup data
- inheritance = reuse code
- super() = use parent code
"""



"""## Mini Project (Student Grade Calculator)"""

class Student():
    def __init__(self, name, marks, attendence):
        self.name = name
        self.marks = marks
        self.attendence = attendence

    def calculate_avg(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

    def display_student(self):
        print(f"Name: {self.name}, Marks: {self.marks}")

    def check_grade(self):
        avg_mark = self.calculate_avg()
        if avg_mark > 80:
            grade = "A"
        elif avg_mark > 60 and avg_mark < 80:
            grade = "B"
        else:
            grade = "C"
        return grade

    # machine learning / ai system
    def predict_future_grade(self):
        import random
        return random.choice(["A", "B", "C"])

s1 = Student("Sadia", [10, 20], 90)

print(s1.marks)
print(s1.name)
print(s1.attendence)

mylist = ["apple", "mango", "banana"]

mylist.reverse()

print(mylist)

s1.check_grade()

s1.predict_future_grade()

students = [
    Student("Hasan", [80, 90, 30], 85),
    Student("Akash", [70, 60], 9),
    Student("Jahid", [10, 20], 90)
]

print("All students final score")
print("="*30)
for s in students:
    print(s.name, s.check_grade())

print()

print("All students future score")
print("="*30)
for s in students:
    print(s.name, s.predict_future_grade())



"""# OOP Practice Questions

---

## 🟢 1. Student Class

#### 📌 Task

Create a class `Student`:

* Attributes: name, age, grade
* Method: `display_info()`

#### 💡 Hint

Use formatted print to show structured output.

#### ▶ Example

```python
s = Student("Saihan", 20, "A")
s.display_info()
```

#### ✅ Output

```
Student Info:
Name: Saihan
Age: 20
Grade: A
```

---

## 🟢 2. Rectangle Class

#### 📌 Task

* Attributes: length, width
* Methods: `area()`, `perimeter()`

#### 💡 Hint

Use formulas: area = l*w, perimeter = 2*(l+w)

#### ▶ Example

```python
r = Rectangle(10, 5)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
```

#### ✅ Output

```
Area: 50
Perimeter: 30
```

---

## 🟢 3. BankAccount (Encapsulation)

#### 📌 Task

* Private attribute: `__balance`
* Methods: deposit, withdraw, get_balance

#### 💡 Hint

Never access `__balance` directly outside the class.

#### ▶ Example

```python
acc = BankAccount("Saihan", 1000)

acc.deposit(500)
acc.withdraw(200)

print("Current Balance:", acc.get_balance())
```

#### ✅ Output

```
Deposited: 500
Withdrawn: 200
Current Balance: 1300
```

---

## 🟢 4. Book Class (State Handling)

#### 📌 Task

* Track book availability

#### 💡 Hint

Use `is_available = True/False`

#### ▶ Example

```python
b = Book("Python Basics", "John Doe")

b.borrow_book()
b.borrow_book()

b.return_book()
b.return_book()
```

#### ✅ Output

```
Book 'Python Basics' borrowed successfully
Book 'Python Basics' is already borrowed
Book 'Python Basics' returned successfully
Book 'Python Basics' was not borrowed
```

---

## 🟢 5. Employee Class

#### 📌 Task

* Apply salary raise

#### 💡 Hint

Increase salary using percentage

#### ▶ Example

```python
e = Employee("Saihan", 50000)

e.apply_raise(10)
print("Updated Salary:", e.salary)
```

#### ✅ Output

```
Salary increased by 10%
Updated Salary: 55000
```

---

## 🟡 6. Car Class

#### 📌 Task

* Drive reduces fuel
* Refuel increases fuel

#### 💡 Hint

Assume 1 km = 1 fuel unit

#### ▶ Example

```python
c = Car("Toyota", 50)

c.drive(60)   # edge case
c.drive(10)
c.refuel(20)
```

#### ✅ Output

```
Not enough fuel to drive 60 km
Drove 10 km
Fuel left: 40
Refueled: 20
Fuel now: 60
```

---

## 🟡 7. Product & Cart (Composition)

#### 📌 Task

* Cart stores multiple products

#### 💡 Hint

Use a list to store items

#### ▶ Example

```python
cart = Cart()

cart.add_product(Product("Pen", 10))
cart.add_product(Product("Notebook", 50))

cart.show_items()
print("Total:", cart.total_price())
```

#### ✅ Output

```
Added: Pen (10)
Added: Notebook (50)

Cart Items:
- Pen: 10
- Notebook: 50

Total: 60
```

---

## 🟡 8. Classroom System

#### 📌 Task

* Store multiple students

#### 💡 Hint

Append student objects to a list

#### ▶ Example

```python
c = Classroom()

c.add_student(Student("Saihan", 20, "A"))
c.add_student(Student("Samia", 19, "B"))

c.show_students()
```

#### ✅ Output

```
Student 'Saihan' added to classroom
Student 'Samia' added to classroom

Classroom Students:
- Saihan (Grade A)
- Samia (Grade B)
```

---

## 🟡 9. User (Encapsulation)

#### 📌 Task

* Private password

#### 💡 Hint

Compare input with stored password

#### ▶ Example

```python
u = User("Saihan")

u.set_password("1234")

print("Login attempt:", u.check_password("1234"))
print("Login attempt:", u.check_password("0000"))
```

#### ✅ Output

```
Password set successfully
Login attempt: True
Login attempt: False
```

---

## 🟠 10. Animal → Dog (Inheritance)

#### 📌 Task

* Override method

#### 💡 Hint

Child method replaces parent method

#### ▶ Example

```python
d = Dog()
d.speak()
```

#### ✅ Output

```
Dog says: Bark
```

---

## 🟠 11. Multiple Inheritance

#### 📌 Task

* Child inherits from two classes

#### 💡 Hint

Use: class Child(Father, Mother)

#### ▶ Example

```python
c = Child()

c.skill1()
c.skill2()
```

#### ✅ Output

```
Skill from Father: Coding
Skill from Mother: Cooking
```

---

## 🟠 12. Shape Polymorphism

#### 📌 Task

* Same method name, different implementations

#### 💡 Hint

Loop through objects

#### ▶ Example

```python
shapes = [Circle(5), Rectangle(10, 5)]

for s in shapes:
    print(f"{type(s).__name__} Area:", s.area())
```

#### ✅ Output

```
Circle Area: 78.5
Rectangle Area: 50
```

---

## 🟠 13. Bird Polymorphism

#### 📌 Task

* Same method behaves differently

#### ▶ Example

```python
birds = [Sparrow(), Penguin()]

for b in birds:
    b.fly()
```

#### ✅ Output

```
Sparrow: Flying in the sky
Penguin: Cannot fly, swims instead
```

---

## 🔴 14. ATM System (Encapsulation + Validation)

#### 📌 Task

* Private balance
* Handle invalid operations

#### ▶ Example

```python
atm = ATM(1000)

atm.withdraw(1200)
atm.deposit(500)
atm.withdraw(300)

atm.show_balance()
```

#### ✅ Output

```
Insufficient balance
Deposited: 500
Withdrawn: 300
Current Balance: 1200
```

---

## 🔴 15. Course System

#### 📌 Task

* Students enroll in course

#### ▶ Example

```python
course = Course("Python Programming")

course.enroll(Student("Saihan"))
course.enroll(Student("Samia"))

course.show_students()
```

#### ✅ Output

```
Saihan enrolled in Python Programming
Samia enrolled in Python Programming

Students in Python Programming:
- Saihan
- Samia
```

---

## 🔴 16. Library System

#### 📌 Task

* Store books in library

#### ▶ Example

```python
lib = Library()

lib.add_book(Book("Python", "John"))
lib.add_book(Book("AI Basics", "Alice"))

lib.show_books()
```

#### ✅ Output

```
Book 'Python' added to library
Book 'AI Basics' added to library

Library Collection:
- Python by John
- AI Basics by Alice
```

---

## 🔴 17. Person → Teacher/Student (Inheritance)

#### 📌 Task

* Common base class

#### ▶ Example

```python
t = Teacher("Mr. Rahim", "Math")
t.show_info()
```

#### ✅ Output

```
Teacher Name: Mr. Rahim
Subject: Math
```

---

## 🔴 18. Calculator (Flexible Arguments)

#### 📌 Task

* Support 2 or 3 numbers

#### 💡 Hint

Use default parameter

#### ▶ Example

```python
c = Calculator()

print("Sum:", c.add(5, 10))
print("Sum:", c.add(5, 10, 15))
```

#### ✅ Output

```
Sum: 15
Sum: 30
```

---

## 🔴 19. Order System

#### 📌 Task

* Manage multiple products

#### ▶ Example

```python
order = Order()

order.add_product(Product("Pen", 10))
order.add_product(Product("Book", 50))

order.show_order()
```

#### ✅ Output

```
Added to order: Pen (10)
Added to order: Book (50)

Order Summary:
- Pen: 10
- Book: 50
Total Price: 60
```

---

## 🔴 20. Abstract-like Shape Design

#### 📌 Task

* Base class enforces method implementation

#### 💡 Hint

Raise error in base class

#### ▶ Example

```python
s = Rectangle(10, 5)
print("Area:", s.area())
```

#### ✅ Output

```
Area: 50
```


"""

# Parent class / Super class
class Vehicle:
    def __init__(self, brand, color, engine):
        self.brand = brand
        self.color = color
        self.engine = engine

    def start(self):
        print(f"{self.brand} is starting.")

    def stop(self):
        print(f"{self.brand} has stopped.")


class UsedCar(Vehicle):
    def __init__(self, brand, color, engine, miles_run):
        super().__init__(brand, color, engine)
        self.miles_run = miles_run

    def start(self):
      print("starting..........")

class VehicleInterface:
    def start(self):
        raise NotImplementedError


class Vehicle(VehicleInterface):
    def start(self):
        print("Vehicle starting...")


car = Vehicle()
car.start()

