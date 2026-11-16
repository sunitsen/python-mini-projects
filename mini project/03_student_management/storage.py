"""ডাটা ইম্পোর্ট ও এক্সপোর্ট হেল্পার (JSON এবং CSV ফাইল)"""
import csv
import json
import os


# স্টুডেন্টদের তালিকা JSON ফাইলে সংরক্ষণ (Write) করা
def export_json(students, path):
    with open(path, "w") as f:
        # প্রতিটি স্টুডেন্ট অবজেক্টকে ডিকশনারিতে রূপান্তর করে ইন্ডেন্টেশন সহ সুন্দরভাবে লেখা
        json.dump([s.to_dict() for s in students], f, indent=2)


# JSON ফাইল থেকে ডেটা পড়া (Read)
def import_json(path):
    # যদি ফাইলটি তৈরি না হয়ে থাকে, তবে খালি লিস্ট রিটার্ন করা
    if not os.path.exists(path):
        return []
    with open(path) as f:
        return json.load(f)


# স্টুডেন্টদের তালিকা CSV (স্প্রেডশিট বা এক্সেল উপযোগী) ফাইলে এক্সপোর্ট করা
def export_csv(students, path):
    with open(path, "w", newline="") as f:
        # কলামের হেডারগুলো নির্ধারণ করা
        writer = csv.DictWriter(f, fieldnames=["student_id", "name", "age", "grade"])
        # হেডার রো ফাইলে লেখা
        writer.writeheader()
        # প্রতিটি স্টুডেন্টের ডিকশনারি ডেটাকে এক এক সারি আকারে ফাইলে লেখা
        writer.writerows(s.to_dict() for s in students)
