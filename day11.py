# 1) Create an empty set and assign it to a variable.
set()
fruits = set()

# 2) Add three items to your empty set using either several add calls, or a single call to update.
# fruits.add("watermelons")
fruits.update(["mangoes", "tomatoes", "oranges"])
# print(fruits)

# 3) Create a second set which includes at least one common element with the first set.
vegetables = {"tomatoes", "onions", "carrots"}

# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
print(fruits.union(vegetables))
print(fruits.difference(vegetables))
print(fruits.intersection(vegetables))

# 5) Create a sequence of numbers using range, then ask the user to enter a number.
# Inform the user whether or not their number was within the range you specified.
# If you want an extra challenge, also tell the user if their number was too high or too low.
sequence = list(range(0, 30, 3))
print(sequence)
user_input = int(input("Enter a number: "))
if user_input in sequence:
    print("Your number is in the sequence!")
else:
    if  user_input < sequence[0]:
        print("Sorry, that's too low. Try again.")
    elif user_input > sequence[-1]:
        print("Sorry, that's too high. Try again.")
    else:
        print("Invalid input.")