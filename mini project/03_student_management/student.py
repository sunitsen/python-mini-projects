"""স্টুডেন্ট ডাটা মডেল (Student model)"""


class Student:
    # কনস্ট্রাক্টর: নতুন স্টুডেন্ট অবজেক্ট তৈরির সময় আইডি, নাম, বয়স ও গ্রেড ইনিশিয়ালাইজ করে
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id  # স্টুডেন্টের ইউনিক আইডি
        self.name = name              # স্টুডেন্টের নাম
        self.age = age                # স্টুডেন্টের বয়স
        self.grade = grade            # স্টুডেন্টের গ্রেড বা নম্বর

    # গ্রেড ০ থেকে ১০০ এর সীমার মধ্যে আছে কিনা তা যাচাই করার স্ট্যাটিক মেথড
    @staticmethod
    def is_valid_grade(grade):
        return 0 <= grade <= 100

    # ফাইলে সেভ থাকা ডিকশনারি (Dictionary) ডেটা থেকে পুনরায় Student অবজেক্ট তৈরি করার ক্লাস মেথড
    @classmethod
    def from_dict(cls, data):
        """সংরক্ষিত ডিকশনারি ডেটা থেকে Student অবজেক্ট তৈরি করা (ইম্পোর্ট করার সময় ব্যবহৃত হয়)"""
        return cls(data["student_id"], data["name"], data["age"], data["grade"])

    # Student অবজেক্টের ডেটাকে ডিকশনারিতে রূপান্তর করে (JSON/CSV তে সেভ করার সুবিধার জন্য)
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "grade": self.grade
        }

    # অবজেক্টটি প্রিন্ট করার সময় মানুষ পড়ার উপযোগী সুন্দর ফরম্যাটে দেখানোর মেথড
    def __str__(self):
        return f"[{self.student_id}] {self.name}, age {self.age}, grade {self.grade}"
