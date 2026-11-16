"""CRUD অপারেশন: Create (তৈরি), Read (পড়া), Update (আপডেট), Delete (মুছে ফেলা)"""
from student import Student
import storage


class StudentManager:
    # ইনিশিয়ালাইজার: ফাইলের নাম সেট করা, স্টুডেন্ট ডিকশনারি তৈরি ও আগের ডেটা লোড করা
    def __init__(self, data_file="students.json"):
        self.data_file = data_file
        self.students = {}  # {student_id: Student অবজেক্ট} আকারে মেমোরিতে তথ্য রাখা হয়
        self._next_id = 1   # পরবর্তী স্টুডেন্টের জন্য স্বয়ংক্রিয় ইউনিক আইডি কাউন্টার
        self.load()         # ফাইল থেকে পূর্বের তথ্য লোড করা

    # Create (নতুন স্টুডেন্ট যোগ করা)
    def add(self, name, age, grade):
        # গ্রেড ০ থেকে ১০০ এর মধ্যে আছে কিনা তা যাচাই করা
        if not Student.is_valid_grade(grade):
            raise ValueError("Grade must be between 0 and 100")
        
        # নতুন Student অবজেক্ট তৈরি
        student = Student(self._next_id, name, age, grade)
        # ডিকশনারিতে স্টুডেন্টের আইডি অনুযায়ী স্টোর করা
        self.students[student.student_id] = student
        # পরবর্তী স্টুডেন্টের জন্য আইডি ১ বাড়ানো
        self._next_id += 1
        # ফাইলে স্বয়ংক্রিয়ভাবে সেভ করা
        self.save()
        return student

    # Read (সকল স্টুডেন্টের তালিকা প্রদর্শন করা)
    def list_all(self):
        return list(self.students.values())

    # Read (নাম দিয়ে স্টুডেন্ট খোঁজা - Case insensitive)
    def search(self, keyword):
        # স্টুডেন্টের নামের ভেতরে কি-ওয়ার্ড আছে কিনা তা যাচাই করে লিস্ট তৈরি করা
        return [s for s in self.students.values() if keyword.lower() in s.name.lower()]

    # Update (বিদ্যমান স্টুডেন্টের তথ্য আপডেট করা)
    def update(self, student_id, name=None, age=None, grade=None):
        # আইডি দিয়ে স্টুডেন্ট খোঁজা
        student = self.students.get(student_id)
        if student is None:
            raise KeyError(f"No student with id {student_id}")
        
        # যদি নতুন গ্রেড দেওয়া থাকে, তবে তা ভ্যালিডেট করে আপডেট করা
        if grade is not None:
            if not Student.is_valid_grade(grade):
                raise ValueError("Grade must be between 0 and 100")
            student.grade = grade
            
        # যদি নতুন নাম দেওয়া থাকে
        if name:
            student.name = name
            
        # যদি নতুন বয়স দেওয়া থাকে
        if age is not None:
            student.age = age
            
        # আপডেটের পর স্বয়ংক্রিয়ভাবে ফাইলে সংরক্ষণ করা
        self.save()
        return student

    # Delete (আইডি দিয়ে স্টুডেন্ট ডিলিট করা)
    def delete(self, student_id):
        # আইডি না পাওয়া গেলে এরর রেইজ করা
        if student_id not in self.students:
            raise KeyError(f"No student with id {student_id}")
        # ডিকশনারি থেকে মুছে ফেলা
        del self.students[student_id]
        # পরিবর্তনটি ফাইলে সেভ করা
        self.save()

    # Persistence (ফাইলে ডেটা সংরক্ষণ ও ফাইল থেকে লোড করা)
    def save(self):
        # সব স্টুডেন্টের তথ্যকে JSON ফাইলে সেভ করা
        storage.export_json(self.students.values(), self.data_file)

    def load(self):
        # JSON ফাইল থেকে স্টুডেন্টদের তথ্য পড়ে নিয়ে ডিকশনারিতে অবজেক্ট হিসেবে সাজানো
        for data in storage.import_json(self.data_file):
            s = Student.from_dict(data)
            self.students[s.student_id] = s
        # ডুপ্লিকেট আইডি এড়াতে, সবচেয়ে বড় আইডির পরের সংখ্যাটি _next_id হিসেবে সেট করা
        if self.students:
            self._next_id = max(self.students) + 1
