

"""## Loop intro and `for` loop basics

A loop is used when we want to repeat the same code multiple times without writing it again and again. This makes our code shorter, cleaner, and easier to manage.

**printing `Hello World!` without using loop**

```python
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
print("Hello World!")
```
`Output:`

```shell
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
```
>As you can see, we had to write the same line many times. This is not efficient, especially if we want to print it 20, 50, or 100 times.

**printing `Hello World!` multiple times using loop**
```python
for i in range(5):
    print("Hello World")
```
`Output:`
```shell
Hello World!
Hello World!
Hello World!
Hello World!
Hello World!
```

> Here, the loop automatically repeats the print statement 5 times, so we only write the code once.


> Don’t worry if the loop syntax looks confusing right now. We’ll break it down step by step and understand how it works


#### The `for` loop

```
for item in container:
    codeblock
```

`for item in container` means *"Take one item at a time from the container and do something with it"*

```
for item in container:  --> Take one item at a time from the container
    codeblock  -----------> and do something
```



**What is a container?** A container is something that holds multiple values. for example:

<div style="display: flex; gap: 30px; align-items: flex-start;">
<div>

| Container | What it holds | Example  |
| --------- | ------------- |----------|
| String    | characters    | `"python"` holds multiple character|
| `range()` | numbers       | `range(5)` holds(generates) numbers from 0 to 4 |

</div>
</div>


`Example:` For each character in the word Python, print the character.
```python
for character in "Python":  # Take one item (in this case a character) at a time from the container (here string `Python` is the container)
    print(character)        # and do something (in this case print the character)
```
`Output:`
```shell
P
y
t
h
o
n
```

So, to sum up a `loop` have mainly 2 usage:

**Usage 1:** Iteration

Iteration means going through items one by one.

`Example:` You have a list of fruits. You check each fruit.
```python
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print("I like", fruit)
```
`Output:`
```shell
I like Apple
I like Banana
I like Mango
```
`Explanation:` Loop goes through each item in the list.

✔ This is called iteration over a collection.

**Usage 2:** Repetition

Repetition means doing something again and again.

`Example:` Print "Good Morning" 3 times.
```python
for i in range(3):
    print("Good Morning")
```
`Output:`
```shell
Good Morning
Good Morning
Good Morning
```
`Explanation:` Same task repeated 3 times.
"""

## repeation

print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")

for i in range(5):
    print("Hello world!")

## iteration -> go thorugh items one by one

name = "Ostad"

for character in name:
    print(character)



"""## The `range()` function

The `range()` function is used to generate a sequence (container) of numbers.
It is commonly used with loops.

#### Different ways to use `range()`

**1.** `range(end)`

Starts from `0` and goes up to `end - 1`

```python
for num in range(5):
    print(num)
```

`Output:`

```shell
0
1
2
3
4
```

**2.** `range(start, end)`
Starts from `start` and goes up to `end - 1`

```python
for num in range(2, 6):
    print(num)
```
`Output:`

```shell
2
3
4
5
```

**3.** `range(start, end, step)`

Starts from `start`, increases by `step`, and stops before `end`

```python
for i in range(1, 10, 2):
    print(i)
```

`Output:`

```shell
1
3
5
7
9
```

>N.B. The end value is exclusive, meaning it is not included.
"""

number = 0
print(number)
number = 1
print(number)
number = 2
print(number)

for number in range(3):
    print(number)

list(range(1, 21, 2))

list(range(2, 21, 2))



"""## Using for loop with numbers"""

for number in range(1, 10):
    print(number)

for number in range(1, 10):
    print(number**2)  # (**) -> square operator

for number in range(1, 10):
    print(f"Number: {number}, Square of {number} = {number**2}")

# print odd numbers
for number in range(1, 10, 2):
    print(number)

# print even numbers
for number in range(0, 10, 2):
    print(number)

"""## Using for loop with `strings`"""

language = "Python"

for char in language:
    print(char)

number = 10
print(number)
number = number + 5
print(number)
number = number + 10
print(number)

number = 10
print(number)
number += 5    # number = number + 5
print(number)
number += 10   # number = number + 10
print(number)

word = "Python"

c = 0

for character in word:
    c = c + 1

print(f"The number of character in the word \"{word}\" is {c}.")

sentence = "I have a cat"

word_count = 0

for word in sentence.split():
    word_count += 1

print(f"The number of word in the sentence \"{sentence}\" is {word_count}.")



"""## Loop Nesting: Nested `for` loops

Loop nesting means putting one loop inside another loop.

>In simple words: A loop inside another loop is called a nested loop.

`Example:`
```python
for i in range(1, 4):      # outer loop → i = 1, 2, 3
    for j in range(1, 3):  # inner loop → j = 1, 2
         print(f"({i},{j})")
```
`Output:`
```shell
(1,1)
(1,2)
(2,1)
(2,2)
(3,1)
(3,2)
```
`Explanation:`

For each One iteration of the outer loop, the inner loop runs completely.

- Outer loop starts
- When i = 1

    - inner loop starts

    - j = 1 → print (1,1)
    
    - j = 2 → print (1,2)
    
    - inner loop ends

- When i = 2

    - inner loop starts

    - j = 1 → print (2,1)
    
    - j = 2 → print (2,2)
    
    - inner loop ends

- When i = 3

    - inner loop starts

    - j = 1 → print (3,1)
    
    - j = 2 → print (3,2)
    
    - inner loop ends

- Outer loop ends
"""

for i in range(1, 4):      # outer loop → i = 1, 2, 3
    for j in range(1, 3):  # inner loop → j = 1, 2
         print(f"({i},{j})")

## Outfit combinations generator

shirts = ["Red T-shirt", "Black Panjabi", "Blue Shirt"]
pants = ["Jeans Pant", "Khaki Pant"]

for shirt in shirts:
    for pant in pants:
        print(shirt, "+", pant)

"""## `break`, `continue` and `pass` statements

- `break` stops the loop immediately and completely
- `continue` skips current step and moves to next.
- `pass` does nothing. It is just a placeholder


"""

user_list = ["user1@mail.com", "user2@mail.com", "user3@mail.com", "user4@mail.com"]

for user in user_list:
    print(f"Sending email to {user}")

## Suppose, user3 unsubscribed from the mailing list. so, we will not send mail to user3

for user in user_list:
    if user == "user3@mail.com":
        continue
    print(f"Sending email to {user}")

## Example: Teacher is looking for a specific student

students = ["Shovon", "Hasan", "Sadia", "Ramim", "Ayesha"]

for student in students:
    if student == "Sadia":
        print("Sadia is present!")
        break
    print("Not Sadia, checking next...")

## Example: Game continues until player loses.

lives = 3

for attempt in range(1, 6):
    if lives == 0:
        print("Game Over!")
        break    # When lives become 0 → loop stops.

    print("Playing level", attempt)
    lives = lives - 1

## User gets 3 attempts. If correct password entered → stop asking.

correct_password = "1234"
attempts = ["1111", "0000", "1234", "3724", "1359"]

for password in attempts:
    if password == correct_password:
        print("Login Successful!")
        break
    print("Wrong Password")

"""
Run this cell to understand the difference between break, continue and pass.
"""

print("Using pass:")
for i in range(5):
    if i == 2:
        pass   # does nothing
    print(i)


print("\nUsing continue:")
for i in range(5):
    if i == 2:
        continue   # skips when i == 2
    print(i)


print("\nUsing break:")
for i in range(5):
    if i == 2:
        break   # stops loop when i == 2
    print(i)



"""## List Basics

- In Python, a `list` is a built-in data structure used to store a collection of items in a single variable.
- You create a `list` by placing items inside square brackets `[]`, separated by commas.

"""

mylist1 = ["Apple", "Banana", "Vegetables"]      # only strings
mylist2 = [2, 7, -35, 20.5, 8, 9]                # only number (int, float)
mylist3 = ["Apple", 2, True, 19.9, "Saihan"]     # mix data types
mylist4 = ["Hello", 10, True, [2, 1, "World"]]   # multiple data types and nested list
mylist5 = [[2, 4, 5], [3, 4, 7]]                 # matrix -> nested list

mylist6 = list(range(1,30,3)) # list() -> list constructor function
print(mylist6)

"""## List Indexing

```python
fruit_list = ["Apple", "Banana", "Cherry", "Orange", "Mango", "Pineapple"]
```

<div style="display: flex; gap: 20px; align-items: flex-start;">

<div>

| List Items        | Apple | Banana | Cherry | Orange | Mango | Pineapple |
|-------------------|-------|--------|--------|--------|-------|-----------|
| **Position**      | 1     | 2      | 3      | 4      | 5     | 6         |
| **Positive Index**| 0     | 1      | 2      | 3      | 4     | 5         |
| **Negative Index**| -6    | -5     | -4     | -3     | -2    | -1        |


</div>

</div>


"""

fruits = ["Apple", "Banana", "Mango", "Pineapples"]
print(fruits)

print(fruits[0])    # using positive index
print(fruits[-4])   # using negative index


print(fruits[3])   # using positive index
print(fruits[-1])  # using negative index

"""## `List` methods

[W3 School: List Methods](https://www.w3schools.com/python/python_lists_methods.asp)

```python
fruits = ["Apple", "Banana"]
```

| Method   | Description | Comment | Example Code | Output |
|-----------|-------------|----------|--------------|------|
| append() | Adds an element at the end of the list | Adds one item only |```fruits.append("Mango")``` | ```['Apple','Banana','Mango']``` |
| extend() | Adds elements of another list | Adds multiple items | ```fruits.extend(["Orange","Pineapple"])``` | ```['Apple','Banana','Orange','Pineapple']``` |
| insert() | Adds element at position | Needs index & value | ```fruits.insert(1,"Grapes")``` | ```['Apple','Grapes','Banana']``` |
| pop() | Removes element by index | Default index = -1 (last) | ```fruits.pop()``` | ```['Apple']```|
| count() | Returns number of occurrences | Counts specific value | ```fruits.count("Apple")``` | ```1``` |
| remove() | Removes item by value | Removes first match | ```fruits.remove("Apple")``` | ```[`Banana`]```|
| reverse() | Reverses list order | Permanent change | ```fruits.reverse()```| ```['Banana', 'Apple']```|
| sort() | Sorts the list | Ascending by default | ```fruits.sort()``` |
"""

fruits  = ["Apple", "Banana", "Guava", "Pineapple"]
print(fruits)

new_fruit = "jackfruit"
fruits.append(new_fruit)  # insert at the end
print(fruits)

new_fruit = "jackfruit"
fruits.insert(2, new_fruit)
print(fruits)

fruits  = ["Apple", "Banana", "Guava", "Banana", "Pineapple"]
fruits.remove("Banana")
print(fruits)

fruits.pop()
print(fruits)

fruits  = ["Apple", "Banana", "Guava", "Banana", "Pineapple"]
fruits.pop(2)
print(fruits)

fruits  = ["Pineapple", "Apple", "Banana", "Guava"]

fruits.index("Guava")

fruits  = ["Pineapple", "Apple", "Banana", "Guava"]
fruits.sort()
fruits



"""## Looping through `list`"""

## directly looping over items

fruits  = ["Pineapple", "Apple", "Banana", "Guava"]

for item in fruits:
    print(item)

## looping through indexing

fruits  = ["Pineapple", "Apple", "Banana", "Guava"]
print(f"Lenght: {len(fruits)}")

for ix in range(len(fruits)):  # ix -> 0, 1, 2, 3
    print(f"Index: {ix}, Item: {fruits[ix]}")

for ix in range(len(fruits)):  # ix -> 0, 1, 2, 3
    print(f"Index: {ix}, Item: {fruits[ix]}")

"""## `List` comprehension

In python, Comprehension is a short and clean way to create collections like lists, dictionaries, and sets in a single line of code. Instead of writing long for loops, we use comprehensions.

List Comprehension: Creates a new list.
- Uses square brackets `[]`.
- Syntax: `[expression for item in iterable if condition]`
- Example: Creating a list of square numbers
```python
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(squares) # output: [1, 4, 9, 16, 25]
```
- Mapping: `[expression for item in iterable]`
- Filtering: `[expression for item in iterable if condition]`
"""

numbers = [1, 2, 3, 4]

squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers)

numbers = [1, 2, 3, 4]

squared_numbers = [num**2 for num in numbers]

print(squared_numbers)

numbers = [1, 2, 3, 4, 5, 6, 7 , 8 , 9]

evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)

numbers = [1, 2, 3, 4, 5, 6, 7 , 8 , 9]

evens = [num for num in numbers if num % 2 == 0]

print(evens)



"""## **Practice Questions**
- Q1. Given `a = [10, 20, 30, 40, 50]`, how would you slice it to get `[20, 40]` using step?
- Q2. Given `level = ["high", "medium", "low"]`, reverse the list using slicing.
- Q3. Given `colors = ["red", "blue", "green", "yellow", "black"]`, get `["red", "green", "black"]`
- Q4. Use the `range()` function to print all even numbers between 1 and 20.
- Q5. Use list comprehension to generate the squares of all odd numbers from 1 to 10.

## **Simple Project: Shopping Cart Total Calculator**

🎯 Goal:

Build a simple program that stores item prices in a list and calculates the final bill.

💻 Problem Statement:

Write a program that:

1. Takes prices of items one by one
2. Stores them in a list
3. Calculates:
  - Total bill
  - Number of items
  - Average price per item
4. Prints a bill summary

**`Project Code`**
```python
prices = []

# Step 1: Take input using loop
n = int(input("How many items did you buy? "))

for i in range(n):
    price = float(input(f"Enter price of item {i+1}: "))
    prices.append(price)

# Step 2: Calculate total using loop
total = 0

for p in prices:
    total += p

# Step 3: Extra calculations
count = len(prices)
average = total / count

# Step 4: Display bill
print("\n--- Shopping Bill ---")
print("Items:", prices)
print("Total Items:", count)
print("Total Bill:", total)
print("Average Price:", average)
```
"""

