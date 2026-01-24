# =========================
# Madlibs Generator
# =========================

# =========================
# Terminal Colors
# =========================
class Color:
    HEADER = '\033[95m'
    INFO   = '\033[96m'
    INPUT  = '\033[93m'
    RESULT = '\033[92m'
    ERROR  = '\033[91m'
    BOLD   = '\033[1m'
    END    = '\033[0m'


# =========================
# Game Header
# =========================
print(f"{Color.INFO}{Color.BOLD}")
print("=================================")
print("        Madlibs Generator         ")
print("=================================")
print(f"{Color.END}")


# =========================
# Read Story File
# =========================
with open("story.txt", "r") as file:
    story_text = file.read()


# =========================
# Extract Placeholders < >
# =========================
placeholders = []
start_index = -1

START_TAG = "<"
END_TAG = ">"

for index, character in enumerate(story_text):

    if character == START_TAG:
        start_index = index

    if character == END_TAG and start_index != -1:
        placeholder = story_text[start_index:index + 1]

        if placeholder not in placeholders:
            placeholders.append(placeholder)

        start_index = -1


# =========================
# User Inputs
# =========================
user_inputs = {}

print(f"{Color.INPUT}Please enter the required words:{Color.END}")

for placeholder in placeholders:
    user_input = input(f"  {placeholder} ➜ ")
    user_inputs[placeholder] = user_input


# =========================
# Replace Placeholders
# =========================
for placeholder in placeholders:
    story_text = story_text.replace(placeholder, user_inputs[placeholder])


# =========================
# Final Output
# =========================
print(f"\n{Color.RESULT}{Color.BOLD}Final Story:{Color.END}\n")
print(story_text)
