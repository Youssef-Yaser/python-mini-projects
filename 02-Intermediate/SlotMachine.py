# =========================
# Slot Machine Game (Full Version With Balance & Validation)
# =========================
from random import choice

# =========================
# Terminal Colors
# =========================
class Color:
    HEADER = '\033[96m'
    A = '\033[95m'
    B = '\033[94m'
    C = '\033[93m'
    D = '\033[92m'
    ERROR = '\033[91m'
    SUCCESS = '\033[92m'
    BOLD = '\033[1m'
    END = '\033[0m'


# =========================
# Game Header
# =========================
print(f"{Color.HEADER}{Color.BOLD}")
print("================================")
print("        SLOT MACHINE GAME       ")
print("================================")
print(Color.END)

# =========================
# Game Settings
# =========================
ROWS = 3
COLUMNS = 3
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100

# =========================
# Symbols
# =========================
SYMBOL_FREQUENCY = {
    "A": 5,
    "B": 6,
    "C": 7,
    "D": 8
}

SYMBOL_VALUES = {
    "A": 15,
    "B": 8,
    "C": 4,
    "D": 2
}

SYMBOL_COLORS = {
    "A": Color.A,
    "B": Color.B,
    "C": Color.C,
    "D": Color.D
}


# =========================
# Generate Spin
# =========================
def generate_spin(rows, columns, frequency):
    pool = []

    for symbol, count in frequency.items():
        pool.extend([symbol] * count)

    result = []

    for _ in range(columns):
        column = []
        available = pool[:]

        for _ in range(rows):
            selected = choice(available)
            available.remove(selected)
            column.append(selected)

        result.append(column)

    return result


# =========================
# Display Slots
# =========================
def display_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            symbol = column[row]
            color = SYMBOL_COLORS[symbol]
            end_char = " | " if i < len(columns) - 1 else ""
            print(f"{color}{symbol}{Color.END}", end=end_char)
        print()


# =========================
# Calculate Winnings
# =========================
def calculate_winnings(columns, lines, bet):
    winnings = 0

    for line in range(lines):
        first = columns[0][line]

        for column in columns:
            if column[line] != first:
                break
        else:
            winnings += SYMBOL_VALUES[first] * bet

    return winnings


# =========================
# Input Functions
# =========================
def get_deposit():
    while True:
        try:
            amount = int(input("Enter your balance: "))
            if amount > 0:
                return amount
            raise ValueError
        except ValueError:
            print(f"{Color.ERROR}Enter positive number only.{Color.END}")


def get_lines():
    while True:
        try:
            lines = int(input(f"Lines to bet on (1-{MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            raise ValueError
        except ValueError:
            print(f"{Color.ERROR}Invalid lines.{Color.END}")


def get_bet():
    while True:
        try:
            bet = int(input(f"Bet per line ({MIN_BET}-{MAX_BET}): "))
            if MIN_BET <= bet <= MAX_BET:
                return bet
            raise ValueError
        except ValueError:
            print(f"{Color.ERROR}Invalid bet.{Color.END}")


# =========================
# Main Game Loop
# =========================
def game():
    balance = get_deposit()

    print(f"\n{Color.SUCCESS}Starting Balance: ${balance}{Color.END}\n")

    while balance > 0:

        print(f"{Color.BOLD}{Color.D}Current Balance: ${balance}{Color.END}")

        lines = get_lines()
        bet = get_bet()

        total_bet = lines * bet

        if total_bet > balance:
            print(f"{Color.ERROR}Not enough balance!{Color.END}")
            continue

        balance -= total_bet

        print(f"\nYou bet ${total_bet}\n")

        slots = generate_spin(ROWS, COLUMNS, SYMBOL_FREQUENCY)
        display_slots(slots)

        winnings = calculate_winnings(slots, lines, bet)
        balance += winnings

        if winnings > 0:
            print(f"\n{Color.SUCCESS}You won ${winnings}!{Color.END}")
        else:
            print(f"\n{Color.ERROR}You lost ${total_bet}.{Color.END}")

        print(f"{Color.BOLD}Remaining Balance: ${balance}{Color.END}")

        # =========================
        # Continue Validation
        # =========================
        while True:
            choice_input = input("\nDo you want to continue? (y/n): ").lower().strip()

            if choice_input == "y":
                break

            elif choice_input == "n":
                print("\nThanks for playing!")
                return

            else:
                print(f"{Color.ERROR}Please enter only 'y' or 'n'.{Color.END}")

    print(f"\n{Color.ERROR}You ran out of money! Game Over.{Color.END}")


# =========================
# Start Game
# =========================
if __name__ == "__main__":
    game()
