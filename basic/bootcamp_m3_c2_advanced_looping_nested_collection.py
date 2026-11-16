
"""## Iterating over list, tuple, set and dictionary"""

## orderded collection (list, tuple)

# list
fruit_list = ["Apple", "Mango", "Banana"]

for item in fruit_list:
    print(f"Processing: {item}")


# tuple
fruit_tuple = ("Apple", "Mango", "Banana")

for item in fruit_tuple:
    print(f"Processing: {item}")

## unordered collection (set)
user_ids = {"001", "002", "003", "004"}

for user in user_ids:
    print(f"Sending notification to user: {user}")

# --- Dictionaries ---

students = {"Alvi": 23, "Sadia": 4, "Abir": 3}

## loop over keys
for student in students:
    print(student)

## loop over keys
for name in students.keys():
    print(name)

## loop over values
for roll in students.values():
    print(roll)

list(students.items())

## loop over items (key, value pair)

for name, roll in students.items():
    print(f"Name: {name}, Roll: {roll}")

for student in students.items():
    print(student)    # here student is a tuple

for student in students.items():
    name, roll = student  # tuple unpacking
    print(name, roll)

for name, roll in students.items(): # unpacke tuples directly in the loop head
    print(f"Name: {name}, Roll: {roll}")

sorted(students.items(), key= lambda x: x[1])

"""## Comprehension

In python, `Comprehension` is a `short and clean way` to create collections like `lists`, `dictionaries`, and `sets` in a single line of code.
Instead of writing long `for loops`, we use `comprehensions`.

1. List Comprehension: Creates a new list.
    - Uses square brackets [].
    - Syntax: `[expression for item in iterable if condition]`
    - Example: Creating a list of squares of even numbers from a range
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) # output: [1, 4, 9, 16, 25]
```

2. Dictionary Comprehension: Creates a new dictionary.
    - Uses curly braces {} and a key-value pair syntax.
    - Syntax: `{key_expression: value_expression for item in iterable if condition}`
    - Example: Creating a dictionary where keys are numbers and values are their cubes.
```python
cubes_dict = {x: x ** 3 for x in range(1, 6)}
print(cubes_dict) # Output: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
```

3. Set Comprehension: Creates a new set (which automatically eliminates duplicate values).
    - Uses curly braces {}.
    - Syntax: `{expression for item in iterable if condition}`
    - Example: Extracting unique even numbers from a list with duplicates.
```python
unique_even = {x for x in [1, 2, 3, 2, 4, 4, 5] if x % 2 == 0}
print(unique_even) # Output: {2, 4} (order may vary as sets are unordered)
```

- Mapping: `[expression for item in iterable]`
- Filtering: `[expression for item in iterable if condition]`
"""

# map

numbers = [1, 2, 3, 4, 5]

squared_numbers = []
for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)

# map

numbers = [1, 2, 3, 4, 5]

squared_numbers = [num**2 for num in numbers]  # list comprehension

print(squared_numbers)

# map

price_list = {"Rice": 60, "Salt": 30, "Sugar": 100}

discount_price_list = {}
for item, price in price_list.items():
    discount_price_list[item] = price*0.9

print(discount_price_list)

discount_price_list = {}
print(discount_price_list)
discount_price_list["rice"] = 30
print(discount_price_list)
discount_price_list["sugar"] = 50
print(discount_price_list)

# map

price_list = {"Rice": 60, "Salt": 30, "Sugar": 100}

discount_price_list = {"item": 50}

discount_price_list = { item:price*0.9 for item, price in price_list.items()}  # dictionary comprehension

print(discount_price_list)

# filter

numbers = list(range(1,21))

odd_numbers = []

for num in numbers:
    if num % 2 == 1:
        odd_numbers.append(num)

print(odd_numbers)

# filter

numbers = list(range(1,21))

odd_numbers = [num for num in numbers if num % 2 == 1]

print(odd_numbers)

# filter

product_list = {"Bread": False, "Milk": True, "Juice": False, "Buiscuits": True}  # True -> Date over

new_product_list = {}

for product, is_date_over in product_list.items():
    if not is_date_over:
        new_product_list[product] = is_date_over

new_product_list

# filter
product_list = {"Bread": False, "Milk": True, "Juice": False, "Buiscuits": True}  # True -> Date over

new_product_list = {product:is_date_over for product, is_date_over in product_list.items() if not is_date_over}

new_product_list  # only unexpired items/products

## filter + map

numbers = list(range(1,21))

cubic_evens = []

for num in numbers:
    if num % 2 == 0:
        cubic_evens.append(num**3)

print(cubic_evens)

numbers = list(range(1,21))

cubic_evens = [num**3 for num in numbers if num %2 == 0]

print(cubic_evens)

## filter + map

results = {"Alvi": 68, "Sadia": 75, "Abir": 80, "Saihan": 60, "Rasel": 65, "Samia": 80}

final_results = {}

for name, mark in results.items():
    if mark > 70: # filter students
        final_results[name] = 100 - mark  # map

final_results

results = {"Alvi": 68, "Sadia": 75, "Abir": 80, "Saihan": 60, "Rasel": 65, "Samia": 80}

final_results = {name: 100-mark for name, mark in results.items() if mark > 70 }

final_results

"""## Nested Collection

1️⃣ API Responses: When you call an API (weather, AI, news, etc.), the response is usually a nested dictionary + list.

2️⃣ AI / LLM Results: When you use APIs like OpenAI or Gemini, responses are nested.

3️⃣ E-commerce Orders: Online shopping systems store orders with multiple products can be represented as nested collection
"""

lst = [1, 3, True, "hello"]
lst = [1, 3, ["x", "y"], True]
t = ("RED", "GREEN", "BLUE")
t = ("RED", ("GREEN", "preffered"), "BLUE")
d = {"Alvi":  234575, "Sadia": 347659}
d = {"Alvi": {"city": "Dhaka", "nid": 234575}, "Sadia": {"city": "Dhaka", "nid": 347659}}
name = "Samia"
l = [1, 3, ("RED", "GREEN", "BLUE"), True, name, {"Alvi":  234575, "Sadia": 347659}, [{"Apple":"Red", "Guava": "Green"}, 3.1416]]

lst = [1, 3, True, "hello"]

lst[3]

lst = [1, 3, ["apple", "mango"], True]

print(lst[2][1])

lst = [1, 3, ["apple", "mango"], True]

nested = lst[2]
print(nested)
print(nested[1])
print(lst[2][1])

t = ("RED", ("GREEN", "preffered"), "BLUE")

t[1][0]

d = {"Alvi": {"city": "Dhaka", "nid": 234575}, "Sadia": {"city": "Dhaka", "nid": 347659}}

d["Sadia"]

d = {"Alvi": {"city": "Dhaka", "nid": 234575}, "Sadia": {"city": "Dhaka", "nid": 347659}}

sadias_info = d["Sadia"]
print(sadias_info)
print(sadias_info["city"])
print(d["Sadia"]["city"])

l = [1, 3, ("RED", "GREEN", "BLUE"), True, name, {"Alvi":  234575, "Sadia": 347659}, [{"Apple":"Red", "Guava": "Green"}, 3.1416]]


# Extract the following values from the list l:

# 1. Alvi's NID

# 2. Value of Pi

# 3. Color of Guava

# 1. Alvi's NID
l[5]["Alvi"]

# 2. Value of Pi
l[6][1]

# 3. Color of Guava
l[6][0]["Guava"]  # nesting depth = 3

# 3. Color of Guava
print(l[6])              # depth = 1
print(l[6][0])           # depth = 2
print(l[6][0]["Guava"])  # depth = 3

## website -  show all the users informations

users = {
    "Alvi": {"city": "Dhaka",  "age": 17, "phone": 217457},
    "Sadia": {"city": "New York", "age": 22, "phone": 12763},
    "Samia": {"city": "Rajshahi", "age": 14, "phone": 169463},
    "Jahid": {"city": "London", "age": 20, "phone": 76435},
    "Hasan": {"city": "Istambl", "age": 23, "phone": 76435},
}


for name, info in users.items():
     # showing names
    print("Name:", name,  end = " | ")
    ## showing informations
    for info_key, info_value in info.items():
        print(f"{info_key}: {info_value}", end = " | ")
    print()

print("Hello", "bd", end=" | ")
print("world", end=" - ")

## website - hide senstive informations (e.g. phone number) for underage users


for name, info in users.items():
    # showing names
    print("Name:", name, end = " | ")

    ## showing informations
    if info["age"] >= 18:
        # show all informations
        for info_key, info_value in info.items():
            print(f"{info_key}: {info_value}", end = " | ")
    else:
        # show information without phone
        for info_key, info_value in info.items():
            if not info_key == "phone":
                print(f"{info_key}: {info_value}", end = " | ")

    print()

"""## Notes on `enumerate()`
- `enumerate()` gives you index + value at the same time when looping
- Syntax : `enumerate(iterable)` | `enumerate(iterable, start=0)`
- `start` gives you the start index, default is `0`



"""

user_list = ["alvi@mail.com", "sadia@gmail.com", "abir@yahoo.com"]

for user in user_list: # access only values
    print(user)

for i in range(5):
  print(i)

user_list = ["alvi@mail.com", "sadia@gmail.com", "abir@yahoo.com"]

for user_id in range(len(user_list)): # access index
    print(user_id)

user_list = ["alvi@mail.com", "sadia@gmail.com", "abir@yahoo.com"]

for user_id in range(len(user_list)):     # len(user_list) = 3 range(3) = 0, 1, 2
    print(user_id+1, user_list[user_id])  # basically index

list(enumerate(user_list))

for user_id, user_mail in enumerate(user_list):  # index + value
    print(user_id, user_mail)



fruits = ["Apple", "Banana", "Mango"]

for idx, value in enumerate(fruits, start=1):
    print(idx, value)

fruits = ["Apple", "Banana", "Mango"]
list(enumerate(fruits, start=0))

"""## Notes on `zip()`

- `zip()` is used to combine multiple iterables (list, set, tuple etc) element-by-element.

- It returns an iterator of tuples, where each tuple contains elements from the input iterables at the same position.

- The length of the zipped result is determined by the smallest collection.
"""

user_id = ["001", "002", "003"]
user_names = ["Alvi", "Sadia", "Abir"]
user_mails = ["alvi@mail.com", "sadia@gmail.com", "abir@yahoo.com"]
user_age = [22, 20, 21]


## user_id, user_names,... -> database column

idx = 1

user_id = ["001", "002", "003"]
user_names = ["Alvi", "Sadia", "Abir"]
user_mails = ["alvi@mail.com", "sadia@gmail.com", "abir@yahoo.com"]
user_age = [22, 20, 21]

print(user_id[idx], user_names[idx], user_mails[idx], user_age[idx])

for idx in range(len(user_id)):
    print(user_id[idx], user_names[idx], user_mails[idx], user_age[idx], sep = " | ")

list(zip(user_id, user_names, user_mails, user_age))

for idx, name, email, age in zip(user_id, user_names, user_mails, user_age):
    print(idx, name, email, age)

user_id = ["001", "002", "003", "004", "005"]   # 5
user_names = ["Alvi", "Sadia", "Abir", "Jahid"] # 4
user_mails = ["alvi@mail.com", "sadia@gmail.com", "abir@yahoo.com"]  # 3
user_age = [22, 20]  # 2

list(zip(user_id, user_names, user_mails, user_age)) # zipped result length depends on the smallest collection

for idx, name, email, age in zip(user_id, user_names, user_mails, user_age):
    print(idx, name, email, age)

## Mini Problem: Total price calculation
products = ["Rice", "Salt", "Sugar"]
quantity = [100, 80, 50]
price_list = [60.5, 30.5, 40.0]

total = 0

for qty, price in zip(quantity, price_list):
    total = total + qty*price

print(total)

## Mini Problem: Per Product price + Total price calculation

products = ["Rice", "Salt", "Sugar"]
quantity = [100, 80, 50]
price_list = [60.5, 30.5, 40.0]

total = 0

for item, qty, price in zip(products, quantity, price_list):
    print(f"Item: {item}, Cost: {qty*price}")
    total = total + qty*price

print(f"Total Cost: {total}")

