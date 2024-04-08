# 1) Define four functions: add, subtract, divide, and multiply.
# Each function should take two arguments, and they should print
# the result of the arithmetic operation indicated by the function name.
# When orders matters for an operation, the first argument should be treated as the left operand,
# and the second argument should be treated as the right operand. 
# You should also make sure that the user can’t pass in 0 as the second argument for divide.
# If the user provides 0, you should print a warning instead of calculating their division.
def add(x, y):
    print(x + y)

def subtract(x, y):
    print(x - y)

def divide(x, y):
    if y == 0:
        print("You can't divide by zero!")
    else:
        print(x / y)

def multiply(x, y):
    print(x * y)

# 2) Define a function called print_show_info that has a single parameter.
# The argument passed to it will be a dictionary with some information about a T.V. show. For example:

# The print_show_info function should print the information stored in the dictionary, in a nice way. For example:

# Breaking Bad (2008) - 5 seasons

# Remember you must define your function before calling it!
def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} seasons")

tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
    }

print_show_info(tv_show)

# 3) Below you’ll find a list containing details about multiple TV series.
# Use your function, print_show_info, and a for loop, to iterate over the series list,
# and call your function once for each iteration, passing in each dictionary.
# You should end up with each series printed in the appropriate format.

series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

for s in series:
    print_show_info(s)

# 4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether
# read forwards or backwards. 
def is_palindrome(word):
    word = word.lower().strip()
    drow = word[::-1]

    if word == drow:
        print(f"{word.title()} is a palindrome.")
    else:
        print(f"{word.title()} is not a palindrome.")

is_palindrome("Joker")