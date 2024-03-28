# 1) Write a short guessing game program using a while loop.
# The user should be prompted to guess a number between 1 and 100,
# and you should tell them whether their guess was too high or too low after each guess.
# The loop should keeping running until the user guesses the number correctly.
import random
secret_number = random.randint(1, 100)
guesses = 0

print("Welcome to the Guessing Game!")
print("I am thinking of a number between 1 and 100, can you guess it? ")

while True:
    num = int(input("What's your guess? "))
    guesses += 1
    if num == secret_number:
        print("Ding! Ding! Ding! You got it right! ")
        print(f"It took you {guesses} attempts!")
        break
    elif num < secret_number:
        print("Your guess is too low. Try again.")
    elif num > secret_number:
        print("Your guess is too high. Try again.")
    # else:
    #     print("Invalid input. Please enter a number between 1 and 100.")


# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
string = "Python"
for char in string:
    if char != 'o':
        print(char)


# 3) Create a program that prints out every prime number between 1 and 100.
for  num in range(2, 101):
    for divisor in range(2, num):
        if num % divisor == 0:
            break
    else:
        print(num)