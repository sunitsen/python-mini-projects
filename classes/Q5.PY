# ==============================================================================
# Module 5: Exam Week – Python Programming
# Question: Online Shopping Cart System (30 Marks)
# ==============================================================================

# ==============================================================================
# Part A – Class Creation (7 Marks)
# ==============================================================================

class ShoppingCart:
    """
    ShoppingCart class to represent an e-commerce customer's shopping cart.
    Stores customer name and item prices, and supports calculations, discounts,
    cart management, and cart merging via operator overloading.
    """

    def __init__(self, customer_name, items=None):
        """
        Constructor to initialize attributes.
        - customer_name: Name of the customer (string)
        - items: List of item prices (numbers). Defaults to empty list if none provided.
        """
        self.customer_name = customer_name
        if items is None:
            self.items = []
        else:
            self.items = list(items)

    # ==========================================================================
    # Part B – Core Methods Implementation (12 Marks)
    # ==========================================================================

    def add_item(self, price):
        """
        Adds a new item price to the cart.
        Validates that price is a positive number.
        """
        if isinstance(price, (int, float)) and price > 0:
            self.items.append(price)
            print(f"Added item: ৳{price:.2f} to {self.customer_name}'s cart.")
        else:
            print(f"Error: Invalid price ({price}). Price must be a positive number.")

    def remove_item(self, price):
        """
        Removes one occurrence of the given price from the cart.
        If the item is not found, displays an informative error message.
        """
        if price in self.items:
            self.items.remove(price)
            print(f"Removed item: ৳{price:.2f} from {self.customer_name}'s cart.")
        else:
            print(f"Notice: Item with price ৳{price:.2f} was not found in {self.customer_name}'s cart.")

    def calculate_total(self):
        """
        Calculates and returns the total price of all items in the cart using a loop.
        """
        total = 0.0
        for price in self.items:
            total += price
        return total

    def apply_discount(self):
        """
        Applies discount rules:
        - If Total >= 3000 -> 10% discount applied
        - If Total < 3000  -> No discount applied (0%)
        Returns the final payable amount.
        """
        total = self.calculate_total()
        if total >= 3000:
            discount = total * 0.10
            return total - discount
        return total

    # ==========================================================================
    # Part C – Display & Utility Methods (6 Marks)
    # ==========================================================================

    def display_cart(self):
        """
        Prints the complete shopping cart summary in a well-formatted manner:
        - Customer name
        - Items in the cart
        - Total amount
        - Final amount after discount
        - Number of items in the cart
        """
        total = self.calculate_total()
        final_amount = self.apply_discount()
        discount_amount = total - final_amount
        item_count = len(self.items)

        print("\n" + "=" * 45)
        print(f"🛒 Shopping Cart Summary: {self.customer_name}")
        print("=" * 45)
        print(f"Customer Name      : {self.customer_name}")
        print(f"Number of Items    : {item_count}")
        print(f"Items in Cart (৳)  : {self.items}")
        print(f"Total Amount       : ৳{total:,.2f}")
        if discount_amount > 0:
            print(f"Discount Applied   : 10% (-৳{discount_amount:,.2f})")
        else:
            print(f"Discount Applied   : 0% (৳0.00)")
        print(f"Final Payable Total: ৳{final_amount:,.2f}")
        print("=" * 45 + "\n")

    def clear_cart(self):
        """
        Removes all items from the cart and displays a confirmation message.
        """
        self.items.clear()
        print(f"Confirmation: {self.customer_name}'s cart has been cleared successfully.")

    # ==========================================================================
    # Part D – Operator Overloading (+) (3 Marks)
    # ==========================================================================

    def __add__(self, other):
        """
        Overrides the + operator to combine two ShoppingCart objects.
        Returns a new ShoppingCart object with:
        - Combined customer names (e.g., 'Alice & Bob')
        - Merged item lists
        """
        if isinstance(other, ShoppingCart):
            combined_name = f"{self.customer_name} & {other.customer_name}"
            combined_items = self.items + other.items
            return ShoppingCart(combined_name, combined_items)
        return NotImplemented


# ==============================================================================
# Part E – Object Usage & Output (2 Marks)
# ==============================================================================

if __name__ == "__main__":
    print("\n--- Step 1: Creating Two ShoppingCart Objects ---")
    cart1 = ShoppingCart("Alice")
    cart2 = ShoppingCart("Bob")

    print("\n--- Step 2: Adding and Removing Items from Both Carts ---")
    # Adding items to Cart 1 (Alice)
    cart1.add_item(1200)
    cart1.add_item(800)
    cart1.add_item(1500)
    cart1.add_item(500)
    # Testing invalid price validation
    cart1.add_item(-200)
    # Removing an item from Cart 1
    cart1.remove_item(500)
    # Testing removing a non-existent item
    cart1.remove_item(9999)

    # Adding items to Cart 2 (Bob)
    cart2.add_item(450)
    cart2.add_item(650)
    cart2.add_item(300)
    # Removing an item from Cart 2
    cart2.remove_item(300)

    print("\n--- Step 3: Displaying Individual Cart Details ---")
    cart1.display_cart()
    cart2.display_cart()

    print("\n--- Step 4: Combining Both Carts using Operator Overloading (+) ---")
    combined_cart = cart1 + cart2

    print("\n--- Step 5: Displaying Combined Cart Details ---")
    combined_cart.display_cart()

    print("\n--- Additional Demonstration: Clearing a Cart ---")
    cart2.clear_cart()
    cart2.display_cart()
