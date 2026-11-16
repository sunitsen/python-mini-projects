# print("Hello world this is sunit sen")

# life= 50
# job = 50

# print(f"life", "job")

# print(type(job))

# print(float(job))

# username = "What you want"
# email = "What you can left"
# password = "own dream"

# print(username, email, password)


# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)


# num1 = float(input("Enter num1 (decimal): "))
# num2 = float(input("Enter num2 (decimal): "))

# print("Addition:", num1 + num2)
# print("Subtraction:", num1 - num2)
# print("Multiplication:", num1 * num2)
# print("Division:", num1 / num2)


# name = "sunit"
# greet = "Hello"

# newVer = greet + name
# print(newVer)
# print("1" * 30)
# print(" ".join("Hare Krishna, Hare Rama" * 108))





# name1 = "Harekrishna"
# name2 = "Harerama"

# # Combine them as a single phrase, then repeat 108 times with spaces between them
# phase  = f"{name1}, {name2}"
# print(" ".join([phase] * 108))

# x = float(input("Enter temperature in Celsius: "))



# fahrenhit = (x * 9/5) + 32 
# print(f"{fahrenhit}")

# for i in range(1, 11):
#     print(i)

# for i in range(1, 21):
#         if i % 2 == 0:
#            print(i)

# user_string_q3 = input("enter")
# print(len(user_string_q3))
# print(f"x: {user_string_q3[::-1]}")

# user_string_q4 = input("Enter a string for Q4: ").lower()
# vowels = "aeiou"
# vowel_count = 0

# for char in user_string_q4: 
#     if char in vowels:
#         vowel_count += 1

# print(f"Total nuber of vowel:{vowel_count}")
# numbers = [10, 25, 30, 45, 50, 65, 70]
# greate30 = [num for num in numbers if num > 25]
# print(greate30)

# fruits = ["apple", "banana", "cherry", "mango"]

# for index, fruit in enumerate(fruits):
#     print(f"{index} {fruit}")

# students = ["Rahim", "Karim", "Ayesha"]
# scores = [85, 90, 78]

# for stu, scr in zip(students, scores):
    # print(f"{stu} scored {scr}")

# subjects = ("Math", "Physics", "Chemistry", "Biology", "English")

# for subject in subjects:
#     print(subject)

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7}

# # '&' অপারেটর ব্যবহার করে সেট দুটির কমন (intersection) উপাদানগুলো বের করা হচ্ছে
# common_elements = set1 & set2
# print("common elements:", common_elements)

# # '-' অপারেটর ব্যবহার করে set1-এর এমন উপাদানগুলো বের করা হচ্ছে যা set2-এ নেই (difference)
# unique_elements = set1 - set2
# print("unique_elements of set1:", unique_elements)


# marks = {
#     "Math": 80,
#     "Physics": 75,
#     "Chemistry": 85
# }

# # marks.items() দিয়ে ডিকশনারির কি-ভ্যালু পেয়ার নিয়ে, enumerate(..., start=1) এর মাধ্যমে ১ থেকে শুরু করে ক্রমিক নম্বর সহ প্রিন্ট করা হচ্ছে
# for index, (subject, score) in enumerate(marks.items(), start=1):
#     print(f"{index} {subject}: {score}")



# # ফাইল তৈরি করে লেখা এবং বন্ধ করা
# file = open("sample.txt", "w")
# file.write("Welcome to Python Programming!")
# file.close()


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def display_info(self):
#         print(f"Student Name: {self.name}, Marks: {self.marks}")

# # অবজেক্ট তৈরি এবং মেথড কল করা
# student1 = Student("Ayesha", 92)
# student1.display_info()


# file = open("sample.txt", "w")
# file.write("Welcome to Python Programming!")
# file.write("Ostad\n")
# file.write("Mastering Python : From Zero to Hero\n")
# file.close()


# file = open("/content/drive/MyDrive/file_test/sample.txt", "r")

# content = file.read()

# file.close()


# print(content)

# file = open("/content/drive/MyDrive/file_test/sample.txt", "a")

# file.write("New content added\n")
# file.write("Hello Bangladesh\n")

# file.close()

class Stu:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_ave(self):
        return sum(self.marks) / len(self.marks)

s1 = Stu("sunit", [90, 60, 50])
s1.calculate_ave()
print(s1.calculate_ave()) 