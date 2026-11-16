def calculate_area(length, width):
    return length * width

# ফাংশনটি কল করা এবং ফলাফল প্রিন্ট করা
result = calculate_area(5, 4)
print("Area of the rectangle:", result)


def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# টেস্ট করার জন্য
greet("Rahim")                # ডিফল্ট গ্রিটিং "Hello" ব্যবহার করবে
greet("Ayesha", "Welcome")     # কাস্টম গ্রিটিং "Welcome" ব্যবহার করবে


import math

# ২৫ এর বর্গমূল এবং ২ এর উপর পাওয়ার ৩ হিসাব করা
sqrt_result = math.sqrt(25)
pow_result = math.pow(2, 3)

print("Square root of 25 is:", sqrt_result)
print("2 raised to the power 3 is:", pow_result)


# ফাইল তৈরি করে লেখা এবং বন্ধ করা
file = open("sample.txt", "w")
file.write("Welcome to Python Programming!")
file.close()

# ফাইলটি আবার রিড মোডে ওপেন করে পড়া এবং প্রিন্ট করা
file = open("sample.txt", "r")
content = file.read()
file.close()

print("File Content:", content)


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def display_info(self):
        print(f"Student Name: {self.name}, Marks: {self.marks}")

# অবজেক্ট তৈরি এবং মেথড কল করা
student1 = Student("Ayesha", 92)
student1.display_info()