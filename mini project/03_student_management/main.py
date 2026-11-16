# manager.py ফাইল থেকে StudentManager ক্লাস ইম্পোর্ট করা হচ্ছে
from manager import StudentManager

# storage.py মডিউলটি ইম্পোর্ট করা হচ্ছে (CSV/JSON ফাইলে ডেটা সেভ ও এক্সপোর্টের জন্য)
import storage

# কনসোল মেনু: ব্যবহারকারীর সামনে প্রদর্শনের জন্য অপশনগুলোর টেক্সট
MENU = """
1. Add student     2. List all     3. Search
4. Update student  5. Delete       6. Export CSV
0. Exit
"""


def main():
    # StudentManager ক্লাসের অবজেক্ট তৈরি করা হচ্ছে (যা স্টুডেন্টদের পুরো ডেটা পরিচালনা করবে)
    manager = StudentManager()

    # প্রোগ্রামটি সচল রাখার জন্য ইনফিনিট (Infinite) লুপ, যতক্ষণ না ব্যবহারকারী '0' চেপে বের হন
    while True:
        # মেনু অপশনগুলো স্ক্রিনে প্রিন্ট করা
        print(MENU)

        # ব্যবহারকারীর কাছ থেকে চয়েস ইনপুট নেওয়া (strip() দিয়ে বাড়তি স্পেস মুছে ফেলা হয়)
        choice = input("Choose: ").strip()

        # ভুল ইনপুট বা রানটাইম এরর নিরাপদে সামলানোর জন্য try-except ব্লক
        try:
            # অপশন ১: নতুন স্টুডেন্ট যোগ করা
            if choice == "1":
                # নাম (স্ট্রিং), বয়স (পূর্ণসংখ্যা/int), এবং গ্রেড (দশমিক/float) ইনপুট নেওয়া এবং manager.add-এ পাঠানো
                s = manager.add(input("Name: "), int(input("Age: ")), float(input("Grade: ")))
                # সফলভাবে যোগ হওয়া স্টুডেন্টের তথ্য প্রদর্শন
                print("Added:", s)

            # অপশন ২: সকল স্টুডেন্টের তালিকা দেখা
            elif choice == "2":
                # manager.list_all() থেকে সব স্টুডেন্টের তালিকা পেয়ে লুপ দিয়ে একে একে প্রিন্ট করা
                for s in manager.list_all():
                    print(s)

            # অপশন ৩: নাম দিয়ে স্টুডেন্ট খোঁজা (Search)
            elif choice == "3":
                # যে অক্ষর বা নাম খোঁজা হচ্ছে তা ইনপুট নিয়ে search ফাংশনে পাঠানো এবং ফলাফল প্রিন্ট করা
                for s in manager.search(input("Name contains: ")):
                    print(s)

            # অপশন ৪: বিদ্যমান স্টুডেন্টের তথ্য (গ্রেড) আপডেট করা
            elif choice == "4":
                # কোন স্টুডেন্টকে আপডেট করা হবে তার আইডি (int) নেওয়া
                sid = int(input("Student id: "))
                # নতুন গ্রেড চাওয়া হচ্ছে (খালি বা ব্ল্যাঙ্ক এন্টার দিলে আগেরটাই বহাল থাকবে)
                grade = input("New grade (blank to skip): ")
                # যদি grade ইনপুট থাকে তবে float-এ কনভার্ট হবে, অন্যথায় None যাবে
                print("Updated:", manager.update(sid, grade=float(grade) if grade else None))

            # অপশন ৫: তালিকা থেকে স্টুডেন্ট মুছে ফেলা (Delete)
            elif choice == "5":
                # স্টুডেন্ট আইডি ইনপুট নিয়ে delete মেথডে পাঠানো
                manager.delete(int(input("Student id: ")))
                # সফলভাবে ডিলিট হওয়ার বার্তা দেওয়া
                print("Deleted.")

            # অপশন ৬: সকল স্টুডেন্টের তথ্য CSV ফাইলে এক্সপোর্ট করা
            elif choice == "6":
                # সব স্টুডেন্টের তালিকা নিয়ে students.csv ফাইলে রাইট করা
                storage.export_csv(manager.list_all(), "students.csv")
                print("Exported to students.csv")

            # অপশন ০: প্রোগ্রাম বন্ধ করে বের হওয়া
            elif choice == "0":
                # লুপ ভেঙে (break) প্রোগ্রাম সমাপ্ত করা
                break

            # যদি মেনুর বাইরের কোনো অপশন চাপ দেওয়া হয়
            else:
                print("Invalid choice.")

        # যদি সংখ্যার জায়গায় অক্ষর টাইপ করা হয় (ValueError) অথবা স্টুডেন্ট আইডি না মেলে (KeyError)
        except (ValueError, KeyError) as err:
            print("Error:", err)


# স্ক্রিপ্টটি যখন সরাসরি রান করা হবে, তখনই কেবল main() ফাংশনটি কল হবে
if __name__ == "__main__":
    main()
