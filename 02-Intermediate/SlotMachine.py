# =========================
# Slot Machine Game
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
# Symbol Frequency 
# =========================
SYMBOL_FREQUENCY = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# =========================
# Symbol Values 
# =========================
SYMBOL_VALUES = {
    "A": 10,
    "B": 5,
    "C": 3,
    "D": 2
}

SYMBOL_COLORS = {
    "A": Color.A,
    "B": Color.B,
    "C": Color.C,
    "D": Color.D
}

# =========================
# Generate Slot Spin
# =========================
def generate_spin(rows, columns, symbol_frequency):
    symbol_pool = []
    for symbol, count in symbol_frequency.items():
        symbol_pool.extend([symbol] * count)

    columns_result = []

    for _ in range(columns):
        column = []
        available_symbols = symbol_pool[:]

        for _ in range(rows):
            selected = choice(available_symbols)
            available_symbols.remove(selected)
            column.append(selected)

        columns_result.append(column)

    return columns_result


# =========================
# Display Slot Machine
# =========================
def display_slots(columns):
    for row in range(len(columns[0])):
        for col_index, column in enumerate(columns):
            symbol = column[row]
            color = SYMBOL_COLORS[symbol]

            end_char = " | " if col_index < len(columns) - 1 else ""
            print(f"{color}{symbol}{Color.END}", end=end_char)
        print()


# =========================
# Check Winnings
# =========================
def calculate_winnings(columns, lines, bet, symbol_values):
    total_winnings = 0

    for line in range(lines):
        first_symbol = columns[0][line]

        for column in columns:
            if column[line] != first_symbol:
                break
        else:
            total_winnings += symbol_values[first_symbol] * bet

    return total_winnings


# =========================
# User Input Functions
# =========================
def get_deposit():
    while True:
        try:
            amount = int(input("Enter deposit amount: "))
            if amount <= 0:
                raise ValueError
            return amount
        except ValueError:
            print(f"{Color.ERROR}Please enter a positive number.{Color.END}")


def get_lines():
    while True:
        try:
            lines = int(input(f"Number of lines (1-{MAX_LINES}): "))
            if 1 <= lines <= MAX_LINES:
                return lines
            raise ValueError
        except ValueError:
            print(f"{Color.ERROR}Invalid number of lines.{Color.END}")


def get_bet():
    while True:
        try:
            bet = int(input(f"Bet per line ({MIN_BET}-{MAX_BET}): "))
            if MIN_BET <= bet <= MAX_BET:
                return bet
            raise ValueError
        except ValueError:
            print(f"{Color.ERROR}Invalid bet amount.{Color.END}")


# =========================
# Main Game Logic
# =========================
def main():
    balance = get_deposit()
    lines = get_lines()

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"{Color.ERROR}Insufficient balance.{Color.END}")
        else:
            break

    print(f"{Color.SUCCESS}Total Bet: ${total_bet}{Color.END}\n")

    slots = generate_spin(ROWS, COLUMNS, SYMBOL_FREQUENCY)
    display_slots(slots)

    winnings = calculate_winnings(slots, lines, bet, SYMBOL_VALUES)
    print(f"\n{Color.SUCCESS}You won ${winnings}{Color.END}")


if __name__ == "__main__": 
   main()     

