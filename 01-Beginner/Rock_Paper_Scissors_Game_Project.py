# Rock Paper Scissors game 

import random 

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

print(GREEN + "Welcome to the Rock, Paper, Scissors Game! I hope you enjoy it." + RESET)

flag = True  # Controls replay

while flag:

    computer_score = 0
    user_score = 0

    # Best of 3 → game continues until someone reaches 3
    while user_score < 3 and computer_score < 3:

        computer = random.choice(["rock", "paper", "scissors"])

        user_choice = input("Choose between [Rock, Paper, Scissors]: ").lower()

        if user_choice not in ["rock", "paper", "scissors"]:
            print(RED + "Invalid choice. Try again." + RESET)
            continue

        print(f"Computer chose: {computer}")

        # Draw
        if user_choice == computer:
            print("Draw")

        # User wins
        elif (user_choice == "rock" and computer == "scissors") or \
             (user_choice == "paper" and computer == "rock") or \
             (user_choice == "scissors" and computer == "paper"):
            
            print(GREEN + "You Win!" + RESET)
            user_score += 1

        # Computer wins
        else:
            print(RED + "Computer Wins!" + RESET)
            computer_score += 1

        print(f"YOU: {user_score} | COMPUTER: {computer_score}")
        print("-" * 30)

        if user_score == 3:
            print(GREEN + "Congratulation! You Win!" + RESET)
        elif computer_score == 3:
            print(RED + "You lost my friend." + RESET)
    

    # After someone reaches 3 → ask to play again
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        flag = False

print(GREEN + "Thanks for playing!" + RESET)
