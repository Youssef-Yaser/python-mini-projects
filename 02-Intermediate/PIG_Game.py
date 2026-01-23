# =========================
# PIG Project Game 
# =========================

from random import randint

# =========================
# Terminal Colors
# =========================
class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

# =========================
# Game Header
# =========================
print(f"{Color.CYAN}{Color.BOLD}")
print("============================")
print("       PIG Project Game     ")
print("============================")
print(f"{Color.END}")

# =========================
# Get Number of Players
# =========================
while True:
    try:
        number_of_players = int(input("Enter number of players (2 - 4): "))
        if 2 <= number_of_players <= 4:
            break
        else:
            print(f"{Color.RED}Choose between 2 and 4 players.{Color.END}")
    except ValueError:
        print(f"{Color.RED}Invalid input. Enter a number.{Color.END}")

# =========================
# Initialize Scores Using List
# =========================
scores = [0] * number_of_players
current_score = 0
current_player = 0  # index of current player

# =========================
# Dice Roll Function
# =========================
def roll_dice():
    return randint(1, 6)

# =========================
# Show Scoreboard
# =========================
def show_scoreboard():
    print(f"{Color.YELLOW}{Color.BOLD}\n--- Scoreboard ---{Color.END}")
    for i in range(number_of_players):
        print(f"{Color.GREEN}Player {i+1}: {scores[i]}{Color.END}")
    print(f"{Color.YELLOW}------------------{Color.END}\n")

# =========================
# Main Game Loop
# =========================
while True:
    print(f"{Color.CYAN}{Color.BOLD}\nPlayer {current_player + 1}'s Turn{Color.END}")
    print(f"{Color.RED}⚠️ If you roll 1, you lose all points for this turn!{Color.END}")

    print(f"{Color.YELLOW}1.{Color.END} Roll Dice")
    print(f"{Color.YELLOW}2.{Color.END} Hold (Save Score)")

    choice = input(f"{Color.CYAN}Choose an option:{Color.END} ")

    if choice == '1':
        roll = roll_dice()
        print(f"{Color.BLUE}You rolled: {roll}{Color.END}")

        if roll == 1:
            current_score = 0
            print(f"{Color.RED}Turn lost! No points added.{Color.END}")
            show_scoreboard()
            current_player = (current_player + 1) % number_of_players
        else:
            current_score += roll
            print(f"{Color.GREEN}Current turn score: {current_score}{Color.END}")

    elif choice == '2':
        scores[current_player] += current_score
        print(f"{Color.GREEN}Score saved! Total score: {scores[current_player]}{Color.END}")
        current_score = 0
        show_scoreboard()
        current_player = (current_player + 1) % number_of_players

    else:
        print(f"{Color.RED}Invalid choice. Try again.{Color.END}")

    # =========================
    # Check Winner
    # =========================
    if scores[current_player - 1] >= 50:
        print(
            f"{Color.CYAN}{Color.BOLD}\nPlayer {current_player} WINS! 🎉 "
            f"Final Score: {scores[current_player - 1]}{Color.END}"
        )
        break
