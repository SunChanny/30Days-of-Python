# 1. Ask the user for their name and age, assign theses values to two variables, and then print them.
name = input("What's your name? ")
age = int(input("How old are you? "))

print("Hello " + name + "! You are " + str(age) + " years old. Nice to meet you!")

# 2. Investigate what happens when you try to assign a value to a variable that you’ve already defined. 
#     Try printing the variable before and after you reuse the name.
x = 5
x = "John"
print(x)

# 3. Below you’ll find some code with a number of errors. 
# Try to go through the program line by line and fix the issues in the code. 
# I’d encourage you to try running the program while you’re working on it, 
# as reading the error messages is great practice for debugging your own programs.

hourly_wage = float(input("Please enter your hourly wage: "))
hours_worked = int(input("How many hours did you work this week? "))

print("Hourly wage: " + str(hourly_wage))
print("Hours worked: " + str(hours_worked))

