# 1) Below is some simple data about characters from BoJack Horseman:
# The data contains the character name, the voice actor or actress who plays them, and the species of the character.
# Write a for loop that uses destructuring so that you can print each tuple in the following format:
# BoJack Horseman is a horse voiced by Will Arnet.
# Note that you're going to have to change the species information to lowercase when you print it.

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for character, actor, species in main_characters:
    print(f"{character} is a {species.lower()} voiced by {actor}.")

# 2) Unpack the following tuple into 4 variables:
# The data represents a student's name, their student id number, and their major and minor disciplines in that order.

student_data = ("John Smith", 11743, ("Computer Science", "Mathematics"))
student_name, student_id, (major_discipline, minor_discipline) = student_data
# print("Student Name: ", student_name)
# print("Student ID:   ", student_id)
# print("Major Disipline: ", major_discipline)
# print("Minor Discipline: ", minor_discipline)

# 3) Investigate what happens when you try to zip two iterables of different lengths.
# For example, try to zip a list containing three items, and a tuples containing four items.
list_example =  ["apple", "banana", "orange"]
tuple_example = ("grape", "kiwi", "strawberry", "blueberry")

zipped_result = zip(list_example, tuple_example)
print(list(zipped_result))
# The excess item on the tuple doesn't print
