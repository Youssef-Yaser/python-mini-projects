# =========================
#  Password Generator
# =========================

import random
import string


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


# =========================
# Password Function
# =========================

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters

    if numbers:
        characters += digits

    if special_characters:
        characters += special

    password = ""
    has_number = False
    has_special = False

    while len(password) < min_length or not (
        (not numbers or has_number) and 
        (not special_characters or has_special)
    ):
        char = random.choice(characters)
        password += char

        if char in digits:
            has_number = True
        if char in special:
            has_special = True

    return password


# =========================
# Safe Input Functions
# =========================

def get_length():
    while True:
        try:
            value = int(input("Enter minimum password length: "))

            if value <= 0:
                print(Color.RED + "Length must be greater than 0!" + Color.END)
                continue

            return value

        except ValueError:
            print(Color.RED + "Please enter a valid number!" + Color.END)


def get_yes_no(message):
    while True:
        choice = input(message).lower()

        if choice in ('y', 'n'):
            return choice == 'y'

        print(Color.RED + "Please enter only y or n!" + Color.END)


# =========================
# Main Program
# =========================

print(Color.CLEAR)
print(Color.CYAN + Color.BOLD + "=== PASSWORD GENERATOR ===\n" + Color.END)

min_length = get_length()

use_numbers = get_yes_no("Include numbers? (y/n): ")

use_special = get_yes_no("Include special characters? (y/n): ")


password = generate_password(
    min_length,
    use_numbers,
    use_special
)

print("\n" + Color.YELLOW + "-" * (min_length+20) + Color.END)
print(Color.GREEN + f"Generated Password: {password}" + Color.END)
print(Color.YELLOW + "-" * (min_length+20)  + Color.END)
