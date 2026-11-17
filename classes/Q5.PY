# ==============================================================================
# মডিউল ৫: পরীক্ষার সপ্তাহ – পাইথন প্রোগ্রামিং
# প্রশ্ন: অনলাইন শপিং কার্ট সিস্টেম (মোট নম্বর: ৩০)
# ==============================================================================

# ==============================================================================
# পার্ট A – ক্লাস তৈরি (৭ নম্বর)
# ==============================================================================

class ShoppingCart:
    """
    ShoppingCart ক্লাসটি একজন কাস্টমারের ই-কমার্স শপিং কার্ট তৈরি করে।
    এটি কাস্টমারের নাম ও আইটেমের মূল্য সংরক্ষণ করে এবং মোট হিসাব, ছাড় (ডিসকাউন্ট),
    কার্টের বিবরণ প্রদর্শন ও দুটি কার্ট একত্রিত করার সুবিধা প্রদান করে।
    """

    def __init__(self, customer_name, items=None):
        """
        কনস্ট্রাক্টর: কাস্টমারের নাম এবং আইটেমের লিস্ট ইনিশিয়ালাইজ করা।
        - customer_name: কাস্টমারের নাম (স্ট্রিং)
        - items: আইটেমের মূল্যের তালিকা (লিস্ট)। কোনো লিস্ট না দিলে ডিফল্ট খালি লিস্ট [] হবে।
        """
        self.customer_name = customer_name
        if items is None:
            self.items = []
        else:
            self.items = list(items)

    # ==========================================================================
    # পার্ট B – মূল মেথডসমূহ ইমপ্লিমেন্টেশন (১২ নম্বর)
    # ==========================================================================

    def add_item(self, price):
        """
        ১. add_item(price): কার্টে নতুন আইটেমের মূল্য যোগ করে।
        শর্ত: মূল্য অবশ্যই ধনাত্মক সংখ্যা (positive number) হতে হবে।
        """
        if isinstance(price, (int, float)) and price > 0:
            self.items.append(price)
            print(f"আইটেম যোগ হয়েছে: ৳{price:.2f} ({self.customer_name}-এর কার্ট)")
        else:
            print(f"ভুল মূল্য: ({price})। পণ্যের মূল্য অবশ্যই একটি ধনাত্মক সংখ্যা হতে হবে।")

    def remove_item(self, price):
        """
        ২. remove_item(price): কার্ট থেকে নির্দিষ্ট মূল্যের একটি আইটেম সরিয়ে ফেলে।
        যদি আইটেমটি না থাকে, তবে একটি উপযুক্ত বার্তা প্রদর্শন করে।
        """
        if price in self.items:
            self.items.remove(price)
            print(f"আইটেম অপসারণ করা হয়েছে: ৳{price:.2f} ({self.customer_name}-এর কার্ট)")
        else:
            print(f"বিজ্ঞপ্তি: ৳{price:.2f} মূল্যের আইটেমটি {self.customer_name}-এর কার্টে পাওয়া যায়নি।")

    def calculate_total(self):
        """
        ৩. calculate_total(): লুপ ব্যবহার করে কার্টের সকল পণ্যের মোট মূল্য হিসাব করে রিটার্ন করে।
        """
        total = 0.0
        for price in self.items:
            total += price
        return total

    def apply_discount(self):
        """
        ৪. apply_discount(): ডিসকাউন্টের নিয়ম প্রয়োগ করে চূড়ান্ত প্রদেয় টাকা রিটার্ন করে।
        নিয়ম:
        - মোট টাকা >= ৩০০০ হলে ১০% ডিসকাউন্ট প্রযোজ্য
        - মোট টাকা < ৩০০০ হলে কোনো ডিসকাউন্ট নেই
        """
        total = self.calculate_total()
        if total >= 3000:
            discount = total * 0.10
            return total - discount
        return total

    # ==========================================================================
    # পার্ট C – প্রদর্শন ও ইউটিলিটি মেথডসমূহ (৬ নম্বর)
    # ==========================================================================

    def display_cart(self):
        """
        ১. display_cart(): সুন্দর ফরম্যাটে কার্টের বিস্তারিত বিবরণ প্রিন্ট করে।
        - কাস্টমারের নাম
        - কার্টের আইটেমসমূহ
        - মোট মূল্য
        - ডিসকাউন্টের পর চূড়ান্ত প্রদেয় মূল্য
        - মোট আইটেমের সংখ্যা
        """
        total = self.calculate_total()
        final_amount = self.apply_discount()
        discount_amount = total - final_amount
        item_count = len(self.items)

        print("\n" + "=" * 45)
        print(f"🛒 শপিং কার্টের বিবরণ: {self.customer_name}")
        print("=" * 45)
        print(f"কাস্টমারের নাম       : {self.customer_name}")
        print(f"মোট আইটেম সংখ্যা    : {item_count} টি")
        print(f"কার্টের পণ্যসমূহ (৳) : {self.items}")
        print(f"মোট মূল্য            : ৳{total:,.2f}")
        if discount_amount > 0:
            print(f"প্রযোজ্য ডিসকাউন্ট   : ১০% (-৳{discount_amount:,.2f})")
        else:
            print(f"প্রযোজ্য ডিসকাউন্ট   : ০% (৳০.০০)")
        print(f"চূড়ান্ত প্রদেয় বিল   : ৳{final_amount:,.2f}")
        print("=" * 45 + "\n")

    def clear_cart(self):
        """
        ২. clear_cart(): কার্টের সমস্ত আইটেম মুছে ফেলে এবং নিশ্চিতকরণ বার্তা প্রদর্শন করে।
        """
        self.items.clear()
        print(f"নিশ্চিতকরণ: {self.customer_name}-এর কার্ট সম্পূর্ণ খালি করা হয়েছে।")

    # ==========================================================================
    # পার্ট D – অপারেটর ওভারলোডিং (+) (৩ নম্বর)
    # ==========================================================================

    def __add__(self, other):
        """
        + অপারেটর ওভাররাইড করা, যাতে দুটি ShoppingCart অবজেক্ট যোগ করলে একটি নতুন কার্ট তৈরি হয়।
        নতুন কার্টে:
        - উভয় কাস্টমারের নাম যুক্ত হবে (যেমন: Alice & Bob)
        - উভয় কার্টের আইটেমের লিস্ট একসাথে মার্জ হবে
        """
        if isinstance(other, ShoppingCart):
            combined_name = f"{self.customer_name} & {other.customer_name}"
            combined_items = self.items + other.items
            return ShoppingCart(combined_name, combined_items)
        return NotImplemented


# ==============================================================================
# পার্ট E – অবজেক্ট তৈরি, ব্যবহার ও আউটপুট প্রদর্শন (২ নম্বর)
# ==============================================================================

if __name__ == "__main__":
    print("\n--- ধাপ ১: দুটি ShoppingCart অবজেক্ট তৈরি ---")
    cart1 = ShoppingCart("Alice")
    cart2 = ShoppingCart("Bob")

    print("\n--- ধাপ ২: উভয় কার্টে আইটেম যোগ এবং অপসারণ করা ---")
    # Alice-এর কার্টে আইটেম যোগ করা
    cart1.add_item(1200)
    cart1.add_item(800)
    cart1.add_item(1500)
    cart1.add_item(500)

    # ভুল (নেগেটিভ) মূল্যের ক্ষেত্রে ভ্যালিডেশন চেক
    cart1.add_item(-200)

    # কার্ট থেকে আইটেম অপসারণ করা
    cart1.remove_item(500)

    # কার্টে নেই এমন আইটেম অপসারণের চেষ্টা
    cart1.remove_item(9999)

    # Bob-এর কার্টে আইটেম যোগ করা
    cart2.add_item(450)
    cart2.add_item(650)
    cart2.add_item(300)

    # Bob-এর কার্ট থেকে একটি আইটেম অপসারণ করা
    cart2.remove_item(300)

    print("\n--- ধাপ ৩: প্রতিটি কার্টের নিজস্ব বিবরণ প্রদর্শন ---")
    cart1.display_cart()
    cart2.display_cart()

    print("\n--- ধাপ ৪: (+) অপারেটর ব্যবহার করে দুটি কার্ট একত্রিত করা ---")
    combined_cart = cart1 + cart2

    print("\n--- ধাপ ৫: একত্রিত করা নতুন কার্টের বিবরণ প্রদর্শন ---")
    combined_cart.display_cart()

    print("\n--- অতিরিক্ত প্রদর্শন: কার্ট খালি করার মেথড পরীক্ষা ---")
    cart2.clear_cart()
    cart2.display_cart()
