# 1. Create a movies list containing a single tuple.
# The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
movies = [("The Martian", "Ridley Scott", 2015, "$108 million")]

# 2. Use the input function to gather information about another movie.
# You need a title, director’s name, release year, and budget.
title = input("Enter the movie's title: ").title().strip()
director = input("Enter the director's name: ").title().strip()
year = int(input("Enter the release year: "))
budget = input("Enter the budget: $")

# 3. Create a new tuple from the values you gathered using input. 
# Make sure they’re in the same order as the tuple you wrote in the movies list.
new_movie = ((title, director, year, budget))

# 4. Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{new_movie[0]}: {new_movie[2]}")

# 5. Add the new movie tuple to the movies collection using append.
movies.append(new_movie)
print(movies)

# 6. Print both movies in the movies collection.
print(movies[0][0])
print(movies[1][0])

# 7. Remove the first movie from movies. Use any method you like.
del movies[0]
print(movies)