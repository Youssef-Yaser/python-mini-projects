# =========================
# Mastermind 4 Color Match
# =========================

import random

# =========================
# Terminal Colors
# =========================
class Color:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'
    CLEAR = '\033c'



COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


def guess_code():
    while True:
        guess = input("Guess (space separated): ").upper().split()

        if len(guess) != CODE_LENGTH:
            print(f"You must enter exactly {CODE_LENGTH} colors.")
            continue

        if not all(color in COLORS for color in guess):
            print("Invalid color used. Use only:", COLORS)
            continue

        return guess


def check_code(guess, real_code):
    correct_pos = 0
    color_count = {}

    # Count colors in real code
    for color in real_code:
        color_count[color] = color_count.get(color, 0) + 1

    # First pass: correct position
    for i in range(CODE_LENGTH):
        if guess[i] == real_code[i]:
            correct_pos += 1
            color_count[guess[i]] -= 1

    # Second pass: correct color wrong position
    incorrect_pos = 0
    for i in range(CODE_LENGTH):
        if guess[i] != real_code[i]:
            if color_count.get(guess[i], 0) > 0:
                incorrect_pos += 1
                color_count[guess[i]] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"{Color.CYAN}Welcome to Mastermind!{Color.END}")
    print(f"You have {TRIES} tries to guess the code.")
    print("Available colors:", COLORS)

    code = generate_code()

    for attempt in range(1, TRIES + 1):
        print(f"\nAttempt {attempt}/{TRIES}")
        guess = guess_code()

        correct_pos, incorrect_pos = check_code(guess, code)

        if correct_pos == CODE_LENGTH:
            print(f"{Color.GREEN}You cracked the code in {attempt} tries!{Color.END}")
            return

        print(f"Correct position: {correct_pos} | Correct color wrong position: {incorrect_pos}")

    print(f"{Color.RED}Out of tries! The code was:{Color.END}", *code)


if __name__ == "__main__":
    game()
