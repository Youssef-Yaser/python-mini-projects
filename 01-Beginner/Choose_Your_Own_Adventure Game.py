# ================================
# Choose Your Own Adventure Game
# Egyptian Archaeologist Version
# ================================

# ANSI color codes
GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
RESET  = "\033[0m"


def print_intro():
    print(YELLOW + "\nWelcome To Egyptian Choose Your Own Adventure Game\n" + RESET)
    print(
        "You are a young archaeologist who arrives at an oasis in the Western Desert\n"
        "after hearing rumors about a hidden royal tomb that has never been discovered.\n"
        "At the entrance to the oasis, you find two possible paths:\n"
    )


def get_choice(option1, option2):
    while True:
        player_input = input("Choose your path: ").lower().strip()
        
       
        if player_input in ["1", option1.lower()]:
            return ("1", option1)
        
        
        elif player_input in ["2", option2.lower()]:
            return ("2", option2)
        
        print(RED + "Invalid choice. Please type 1 or 2!" + RESET)


def show_story_log(history):
    print(YELLOW + "\n======================= Your Full Story =========================" + RESET)
    for step_index, step in enumerate(history, start=1):
        print(GREEN + f"|Step {step_index}: You chose → {step[1]} " + RESET)
    print(YELLOW + "=================================================================\n" + RESET)



story_log = []     # Store all choices made by the player

print_intro()

# ------------------------------------------------------------
# FIRST CHOICE
# ------------------------------------------------------------

print(GREEN + "1. Entry through the old stone archway" + RESET)
print(GREEN + "2. Explore the remains of the Temple of Amun\n" + RESET)

first_choice = get_choice(
    "Entry through the old stone archway",
    "Explore the remains of the Temple of Amun"
)
story_log.append(first_choice)

print(RED + f"\nYou chose Path {first_choice[0]}: {first_choice[1]}\n" + RESET)

# ------------------------------------------------------------
# PATH 1: Stone Archway
# ------------------------------------------------------------
if first_choice[0] == "1":
    print(
        "You enter a narrow corridor filled with faded pharaonic inscriptions.\n"
        "After several meters, you hear strong winds behind you. You must decide:\n"
    )

    print(GREEN + "1. Examine the inscriptions" + RESET)
    print(GREEN + "2. Go deeper without stopping\n" + RESET)

    second_choice = get_choice(
        "Examine the inscriptions",
        "Go deeper without stopping"
    )
    story_log.append(second_choice)

    print(RED + f"You chose Path {second_choice[0]}: {second_choice[1]}\n" + RESET)

    if second_choice[0] == "1":
        print(
            YELLOW +
            "You study the inscriptions and discover they warn about a deadly trap.\n"
            "Thanks to your quick thinking, you disable a pressure stone and pass safely.\n"
            "You walk forward and find a massive golden gate leading to the lost royal treasure room!" +
            RESET
        )
        print(GREEN + "\n*** WINNING ENDING – You uncovered the royal chamber! ***\n" + RESET)

    else:
        print(
            YELLOW +
            "You step on a hidden pressure stone!\n"
            "The corridor collapses and seals you inside the ancient tomb forever." +
            RESET
        )
        print(RED + "\n*** LOSS ENDING – Trapped in the ancient corridor ***\n" + RESET)

# ------------------------------------------------------------
# PATH 2: Temple of Amun
# ------------------------------------------------------------

else:
    print(
        "You enter the courtyard of Amun’s ancient temple.\n"
        "Beside the giant statue lies a mysterious papyrus scroll.\n"
        "You must choose:\n"
    )

    print(GREEN + "1. Take the papyrus and read it" + RESET)
    print(GREEN + "2. Enter the underground crypt\n" + RESET)

    second_choice = get_choice(
        "Take the papyrus and read it",
        "Enter the underground crypt"
    )
    story_log.append(second_choice)

    print(RED + f"You chose Path {second_choice[0]}: {second_choice[1]}\n" + RESET)

    if second_choice[0] == "1":
        print(
            YELLOW +
            "You unroll the papyrus and discover a complete map!\n"
            "It reveals the exact location of the lost tomb—just 400 meters behind the oasis.\n"
            "You follow the map and unlock the entrance with no traps at all!" +
            RESET
        )
        print(GREEN + "\n*** WINNING ENDING – You discovered the lost tomb! ***\n" + RESET)

    else:
        print(
            YELLOW +
            "You descend into the crypt. Suddenly, the torches go out.\n"
            "Bats fly everywhere, and the stone door shuts behind you.\n"
            "There is no way out…" +
            RESET
        )
        print(RED + "\n*** LOSS ENDING – Trapped in Amun’s crypt ***\n" + RESET)

# ------------------------------------------------------------
# SHOW COMPLETE STORY HISTORY
# ------------------------------------------------------------

show_story_log(story_log)
