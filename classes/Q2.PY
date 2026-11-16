# ==========================================
# Question 1: Loop Basics (for loop)
# ==========================================
print("--- Question 1 ---")
print("Numbers from 1 to 10:")

# এখানে range(1, 11) মানে হলো লুপটি ১ থেকে শুরু হবে এবং ১১ এর ঠিক আগ পর্যন্ত (অর্থাৎ ১০ পর্যন্ত) চলবে।
# প্রতিবার i এর মান ১ করে বাড়বে এবং print(i) দিয়ে সেটা স্ক্রিনে প্রিন্ট হবে।
for i in range(1, 11):
    print(i)


# ==========================================
# Question 2: Loop with Condition
# ==========================================
print("\n--- Question 2 ---")
print("Even numbers between 1 and 20:")

# range(1, 21) দিয়ে ১ থেকে ২০ পর্যন্ত সংখ্যাগুলোর ওপর লুপ চালানো হচ্ছে।
for i in range(1, 21):
    # এখানে i % 2 == 0 এর মানে হলো: i কে ২ দিয়ে ভাগ করার পর ভাগশেষ (remainder) কত হয় তা চেক করা।
    # '%' সাইনটিকে 'মডুলাস' (Modulo) অপারেটর বলা হয়, যা ভাগের ভাগশেষ বের করে। 
    # যদি ভাগশেষ '0' হয়, তার মানে সংখ্যাটি ২ দ্বারা নিঃশেষে বিভাজ্য, অর্থাৎ এটি একটি জোড় (Even) সংখ্যা।
    if i % 2 == 0:
        print(i)


# ==========================================
# Question 3: String Manipulation
# ==========================================
print("\n--- Question 3 ---")
user_string_q3 = input("Enter a string for Q3: ")

# .upper() মেথড ব্যবহারকারীর দেওয়া পুরো স্ট্রিংটিকে বড় হাতের অক্ষরে রূপান্তর করে।
print(f"Uppercase: {user_string_q3.upper()}")

# len() ফাংশনটি স্ট্রিংয়ের মোট অক্ষরের সংখ্যা বা দৈর্ঘ্য (length) গুনে বের করে দেয়।
print(f"Length: {len(user_string_q3)}")

# [::-1] হলো পাইথনের একটি স্পেশাল স্লাইসিং টেকনিক, যা পুরো স্ট্রিংটিকে উল্টো দিক থেকে (reversed) সাজিয়ে প্রিন্ট করে।
print(f"Reversed: {user_string_q3[::-1]}")


# ==========================================
# Question 4: String Processing with Loop
# ==========================================
print("\n--- Question 4 ---")
# .lower() দিয়ে ব্যবহারকারীর ইনপুটকে ছোট হাতের অক্ষরে রূপান্তর করা হচ্ছে, যাতে বড় বা ছোট হাতের অক্ষরের কারণে কোনো ভুল না হয়।
user_string_q4 = input("Enter a string for Q4: ").lower()
vowels = "aeiou"
vowel_count = 0

# এই লুপটি স্ট্রিংয়ের প্রতিটি অক্ষরকে একে একে ধরে 'char' নামক ভ্যারিয়েবলে রাখবে।
for char in user_string_q4:
    # 'char in vowels' চেক করছে বর্তমান অক্ষরটি 'aeiou'-এর ভেতরে আছে কি না।
    # যদি মিলে যায় (অর্থাৎ ভাওয়েল হয়), তবে vowel_count এর মান ১ বেড়ে যাবে।
    if char in vowels:
        vowel_count += 1

print(f"Total number of vowels: {vowel_count}")


# ==========================================
# Question 5: List Comprehension
# ==========================================
print("\n--- Question 5 ---")
numbers = [10, 25, 30, 45, 50, 65, 70]

# এটি হলো লিস্ট কম্প্রিহেনশন (List Comprehension), যা খুব সংক্ষেপে এক লাইনে লুপ ও শর্ত পূরণ করে নতুন লিস্ট বানায়।
# এর মানে হলো: numbers লিস্ট থেকে প্রতিটি সংখ্যা (num) এক এক করে নাও, এবং যদি num > 40 শর্তটি সত্যি হয়, 
# তবেই কেবল সেই সংখ্যাটিকে নতুন 'greater_than_40' লিস্টের মধ্যে যুক্ত করো।
greater_than_40 = [num for num in numbers if num > 40]

print("Original List:", numbers)
print("Numbers greater than 40:", greater_than_40)