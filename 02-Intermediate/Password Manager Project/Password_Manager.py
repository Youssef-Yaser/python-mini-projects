# =========================
# Password Manager Project
# =========================

from cryptography.fernet import Fernet
from os.path import exists

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
# Key Management
# =========================

def write_key():
    """
    Generate a new encryption key and save it to a file.
    Should be called once if key does not exist.
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    """
    Load the encryption key from file.
    """
    with open("key.key", "rb") as key_file:
        return key_file.read()


# Create key file if it does not exist
if not exists("key.key"):
    write_key()

key = load_key()
fer = Fernet(key)


# =========================
# Ensure passwords file exists
# =========================

if not exists("passwords.txt"):
    open("passwords.txt", "w").close()


# =========================
# View Passwords
# =========================

def view_passwords():
    """
    Read and decrypt all saved passwords.
    """
    print(f"\n{Color.CYAN}{Color.BOLD}Saved Accounts{Color.END}")
    print(f"{Color.BLUE}{'-'*40}{Color.END}")

    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print(f"{Color.YELLOW}No passwords stored yet.{Color.END}")
                return

            for line in lines:
                user, password = line.strip().split("|")
                decrypted_password = fer.decrypt(password.encode()).decode()

                print(
                    f"{Color.GREEN}User:{Color.END} {user.strip()} | "
                    f"{Color.YELLOW}Password:{Color.END} {decrypted_password}"
                )

    except Exception as e:
        print(f"{Color.RED}Error reading passwords file.{Color.END}")

    print(f"{Color.BLUE}{'-'*40}{Color.END}\n")


# =========================
# Add Password
# =========================

def add_password():
    """
    Add a new encrypted password.
    """
    print(f"\n{Color.CYAN}{Color.BOLD}Add New Password{Color.END}")

    account = input(f"{Color.BLUE}Account Name:{Color.END} ")
    password = input(f"{Color.BLUE}Password:{Color.END} ")

    encrypted_password = fer.encrypt(password.encode()).decode()

    with open("passwords.txt", "a") as file:
        file.write(account + "|" + encrypted_password + "\n")

    print(f"{Color.GREEN}Password saved successfully!{Color.END}\n")


# =========================
# Main Menu
# =========================

print(f"{Color.BLUE}{Color.BOLD}")
print("===================================")
print("     PASSWORD MANAGER (CLI)        ")
print("===================================")
print(f"{Color.END}")

while True:
    print(f"{Color.YELLOW}1.{Color.END} View passwords")
    print(f"{Color.YELLOW}2.{Color.END} Add password")
    print(f"{Color.YELLOW}3.{Color.END} Quit")

    choice = input(f"\n{Color.CYAN}Choose an option:{Color.END} ")

    if choice == "1":
        view_passwords()
    elif choice == "2":
        add_password()
    elif choice == "3":
        print(f"{Color.RED}Goodbye. Stay secure.{Color.END}")
        break
    else:
        print(f"{Color.RED}Invalid choice. Try again.{Color.END}\n")
