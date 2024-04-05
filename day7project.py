# Below you'll find a list which contains the relevant data about a selection of movies.
# Each item in the list is a tuple containing a movie name and movie budget in that order:

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# For this project, your program should do the following:

# 1. Calculate the average budget of all movies in the data set.
total = 0
above_average = []

for movie in movies:
    total += movie[1]
    
    # print("The total budget of all movies is: ", total)

average = int(total / len(movies))
print("The average budget of all movies is: $", round(average,  2))

# 2. Print out every movie that has a budget higher than the average you calculated.
# You should also print out how much higher than the average the movie's budget was.
for movie in movies:
    if movie[1] > average:
        above_average.append(movie)
        print(f"{movie[0]} is above average by  ${movie[1] - average}.")

# 3. Print out how many movies spent more than the average you calculated.
for movie in movies:
    if movie[1] > average:
        print(len(above_average), " movies spent more than average.")
        break