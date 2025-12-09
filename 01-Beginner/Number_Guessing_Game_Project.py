#Guessing Game 
import random

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

# Generate a random number between 1 and 100
rand = random.randint(1, 100)
number_of_guesses = 0
print(GREEN +"Welcome to the Number Guessing Game! I hope you enjoy it."+RESET)

while True:
    try:
        # Get user's guess
        user_guess = int(input("Enter your guess between 1 and 100: "))

        number_of_guesses +=1 

        if user_guess == rand:
            print(GREEN +"Correct guess! You win 🎉"+RESET)
            print(GREEN +f"Total Guesses :  {number_of_guesses}"+RESET)
            break  
        elif user_guess > rand:
            print(RED +"Try a lower number."+RESET)
        else:
            print(RED +"Try a higher number." +RESET)
    except ValueError:
        # For Check that  input in only intger
        print("Please enter a valid integer between 1 and 100.")
