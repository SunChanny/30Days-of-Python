# 1)Try to approximate the behaviour of the is operator using ==.
# Remember we have the id function for finding the memory address for a given value,
# and we can compare memory addresses to check for identity.

# 2) Try to use the is operator or the id function to investigate the difference between this:

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(id(numbers)) #2320239203072
print(id(new_numbers)) #2320240681536
print(numbers is new_numbers) #False

# # And this:

numbers = [1, 2, 3, 4]
print(id(numbers)) #2320240588736
print(numbers is numbers) #True
numbers.append(5)
print(id(numbers)) #2320240588736
print(numbers is numbers) #True
# Are new_numbers and numbers the same thing? NO  What about numbers before and after we append 5? N9

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
number = float(input("Enter a number: "))
if float(number) > 0:
    print(f"{number} is positive.")
elif float(number) < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# 4) Write a program to determine whether an employee is owed any overtime.
# You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
employee_name = input("Enter employee's name: ").strip().title()
hours_worked = float(input(f"How many hours has {employee_name} worked this week? "))
hourly_wage = float(input(f"What is {employee_name}'s hourly wage? "))

# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay,
# as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. 
# In effect, the employees get paid 110% of their hourly wage for any overtime.

if hours_worked > 40.0:
    overtime_hours = hours_worked - 40.0
    overtime_pay = overtime_hours * 0.1 * hourly_wage
    print(f"{employee_name} is due additional pay of ${overtime_pay}")