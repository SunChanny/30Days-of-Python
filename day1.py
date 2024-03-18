# Print your age to the console.
# Calculate and print the number of days, weeks, and months in 27 years. 
# Don’t worry about leap years!
# Calculate and print the area of a circle with a radius of 5 units. 
# You can be as accurate as you like with the value of pi.

#task 1
print("Hello user") 
age = int(input("Please input your age: "))
print("You are "  + str(age) + " years old.") #went a little overboard

#task 2
years = 27
days = years * 365
weeks = days / 7
months = 12 * years

print("There are approximately " + str(days) + " days, " + str(round(weeks)) 
      + " weeks, and " + str(round(months)) + " months in 27 years.")
       
#task 3
area_of_a_circle = (22 / 7) * (5 ** 2)

print("The area of a circle with a radius of 5 units is " + str(area_of_a_circle) + " sq units.")