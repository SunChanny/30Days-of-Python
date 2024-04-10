# 1) Define a exponentiate function that takes in two numbers.
# The first is the base, and the second is the power to raise the base to.
# The function should return the result of this operation.
def exponentiate(a, b):
    return a ** b
# print(exponentiate(2, 3))

# 2) Define a process_string function which takes in a string
# and returns a new string which has been converted to lowercase,
# and has had any excess whitespace removed.
def process_string(s):
    return s.lower().strip()
# print(process_string("Hello World! "))

# 3) Write a function that takes in a tuple containing information about an actor
# and returns this data as a dictionary. The data should be in the following format:
# ("Tom Hardy", "English", 42)  # name, nationality, age
# You can choose whatever key names you like for the dictionary.
def actor_dict(tuple):
    return  {"name": tuple[0], "nationality": tuple[1], "age": tuple[2]}
# print(actor_dict(("Tom Hardy", "English", 42)))

# 4) Write a function that takes in a single number and returns True or False depending on
# whether or not the number is prime.
def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
        
    return True

# print(is_prime(8))