# =========================
# Timed Math Challenge
# =========================

from random import randint, choice
from time import time

# =========================
# Terminal Colors
# =========================
class Color:
    INFO   = '\033[96m'
    INPUT  = '\033[93m'
    RESULT = '\033[92m'
    ERROR  = '\033[91m'
    BOLD   = '\033[1m'
    END    = '\033[0m'


# =========================
# Header
# =========================
print(f"{Color.INFO}{Color.BOLD}")
print("====================================")
print("       Timed Math Challenge         ")
print("====================================")
print(Color.END)


OPERATORS = ["+", "-", "*", "/"]
MIN_OPERAND = 0
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


# =========================
# Generate Operation
# =========================
def generate_operation():
    operator = choice(OPERATORS)

    if operator == "/":
        right = randint(1, MAX_OPERAND)   # مستحيل يطلع صفر
        left = right * randint(0, MAX_OPERAND)
    else:
        left = randint(MIN_OPERAND, MAX_OPERAND)
        right = randint(MIN_OPERAND, MAX_OPERAND)

    return left, right, operator


# =========================
# Loop
# =========================
problem_number = 1
generate_new = True
wrong_attempts = 0

start_time = time()

while problem_number <= TOTAL_PROBLEMS:

    print(f"\nProblem #{problem_number}")

    if generate_new:
        left, right, operator = generate_operation()

    print(f"{Color.INPUT}{left} {operator} {right} = {Color.END}", end="")

    try:
        user_input = input().strip()
        if user_input == "":
            raise ValueError
        user_answer = int(user_input)

    except ValueError:
        print(f"{Color.ERROR}Invalid input! Enter a valid number.{Color.END}")
        wrong_attempts += 1
        generate_new = False
        continue

    # =========================
    # Calculate Answer
    # =========================
    if operator == "+":
        correct_answer = left + right
    elif operator == "-":
        correct_answer = left - right
    elif operator == "*":
        correct_answer = left * right
    else:  # division
        correct_answer = left // right

    # =========================
    # Check Answer
    # =========================
    if user_answer == correct_answer:
        print(f"{Color.RESULT}Correct!{Color.END}")
        problem_number += 1
        generate_new = True
    else:
        print(f"{Color.ERROR}Wrong answer. Try again.{Color.END}")
        wrong_attempts += 1
        generate_new = False


end_time = time()
total_time = round(end_time - start_time, 2)

# =========================
# Final Result
# =========================
print("\n=============================================")
print(f"{Color.BOLD}{Color.RESULT}Amazing 🎉! You completed all {TOTAL_PROBLEMS} problems! ")
print(f"Completed in {total_time} seconds.{Color.END}")
print(f"{Color.BOLD}{Color.ERROR}Wrong attempts: {wrong_attempts}{Color.END}")
print("=============================================")
