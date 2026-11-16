fruits = ["apple", "banana", "cherry", "mango"]

for index, fruit in enumerate(fruits):
    print(f"{index} {fruit}")


students = ["Rahim", "Karim", "Ayesha"]
scores = [85, 90, 78]

for student, score in zip(students, scores):
    print(f"{students} scored {score}")


subjects = ("Math", "Physics", "Chemistry", "Biology", "English")
for subject in subjects:
    print(subject)


set1 = {1,2,3,4,5}
set2 = {4,5,6,7}

common_elements = set1 & set2
print("common elements:", common_elements)

unique_elements = set1 - set2
print("unique_elements of set1:", unique_elements)

marks = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85
}

for index, (subject, score) in enumerate(marks.items(), start=1):
    print(f"{index} {subject}: {score}")






    # ==========================================
# Question 1: Enumerate with List
# ==========================================
fruits = ["apple", "banana", "cherry", "mango"]

# enumerate() ব্যবহার করে প্রতিটি ফলের ইনডেক্স (0, 1, 2...) এবং তার নাম একসাথে লুপে নেওয়া হচ্ছে
for index, fruit in enumerate(fruits):
    print(f"{index} {fruit}")


# ==========================================
# Question 2: Zip with Two Lists
# ==========================================
students = ["Rahim", "Karim", "Ayesha"]
scores = [85, 90, 78]

# zip() এর মাধ্যমে দুটি ভিন্ন লিস্টকে একসাথে জোড়া লাগিয়ে শিক্ষার্থী ও তার প্রাপ্ত নম্বর এক লাইনে নেওয়া হচ্ছে
for student, score in zip(students, scores):
    print(f"{student} scored {score}")


# ==========================================
# Question 3: Tuple and Loop
# ==========================================
subjects = ("Math", "Physics", "Chemistry", "Biology", "English")

# tuple-এর উপাদানগুলোর উপর লুপ চালিয়ে প্রতিটি সাবজেক্ট একে একে প্রিন্ট করা হচ্ছে
for subject in subjects:
    print(subject)


# ==========================================
# Question 4: Set Operations
# ==========================================
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}

# '&' অপারেটর ব্যবহার করে সেট দুটির কমন (intersection) উপাদানগুলো বের করা হচ্ছে
common_elements = set1 & set2
print("common elements:", common_elements)

# '-' অপারেটর ব্যবহার করে set1-এর এমন উপাদানগুলো বের করা হচ্ছে যা set2-এ নেই (difference)
unique_elements = set1 - set2
print("unique_elements of set1:", unique_elements)


# ==========================================
# Question 5: Dictionary with Enumerate
# ==========================================
marks = {
    "Math": 80,
    "Physics": 75,
    "Chemistry": 85
}

# marks.items() দিয়ে ডিকশনারির কি-ভ্যালু পেয়ার নিয়ে, enumerate(..., start=1) এর মাধ্যমে ১ থেকে শুরু করে ক্রমিক নম্বর সহ প্রিন্ট করা হচ্ছে
for index, (subject, score) in enumerate(marks.items(), start=1):
    print(f"{index} {subject}: {score}")