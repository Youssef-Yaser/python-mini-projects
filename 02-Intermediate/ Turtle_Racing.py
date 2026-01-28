# =========================
# Turtle Racing  
# =========================

import turtle 
import time 
import random

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
print(f"{Color.GREEN}{Color.BOLD}")
print("==========================")
print("        Turtle Racing     ")
print("==========================")
print(f"{Color.END}")

# =========================
# Game Settings
# =========================
SCREEN_WIDTH , SCREEN_HEIGHT = 500 , 500
AVAILABLE_COLORS = ['red','blue','green','orange','yellow','black','purple','pink','brown' ,'cyan']

# =========================
# Functions
# =========================
def get_number_of_racers():
    """
    Ask the user to enter the number of racers (2-10).
    Handles invalid input and keeps prompting until a valid number is entered.
    Returns the number of racers as an integer.
    """
    while True:
        try:
            num_racers = int(input("Enter number of racers (2 - 10): \n"))
            if 2 <= num_racers <= 10:
                return num_racers
            else:
                print(f"{Color.RED}Please enter a number between 2 and 10.{Color.END}")
        except ValueError:
            print(f"{Color.RED}Invalid input, try again.{Color.END}")


def init_turtle_screen():
    """
    Initialize the turtle graphics screen with the given width and height.
    Sets the title of the window for the Turtle Racing game.
    """
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title("Turtle Racing")


def create_turtle_racers(colors):
    """
    Create turtle racers for each color in the provided list.
    Positions each turtle at the starting line with proper spacing.
    Returns a list of turtle objects ready for the race.
    """
    racers = []
    spacing_x = SCREEN_WIDTH // (len(colors) + 1)

    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-SCREEN_WIDTH//2 + (i + 1) * spacing_x, -SCREEN_HEIGHT//2 + 20)
        racer.pendown()
        racers.append(racer)
    
    return racers


def start_race(colors):
    """
    Starts the race by moving turtles forward randomly until one reaches the finish line.
    Returns the color of the winning turtle.
    """
    racers = create_turtle_racers(colors)
    finish_line = SCREEN_HEIGHT // 2 - 10

    while True:
        for racer in racers:
            step = random.randint(1, 20)
            racer.forward(step)

            _, y_pos = racer.pos() 
            if y_pos >= finish_line:
                winner_index = racers.index(racer)
                return colors[winner_index]

# =========================
# Main Game
# =========================
def main () :
    num_racers = get_number_of_racers()
    init_turtle_screen()

    random.shuffle(AVAILABLE_COLORS)
    race_colors = AVAILABLE_COLORS[:num_racers]

    print(f"{Color.CYAN}{Color.BOLD}Starting the race with {num_racers} turtles!{Color.END}")
    time.sleep(1)

    winner_color = start_race(race_colors)
    print(f"{Color.GREEN}{Color.BOLD}🏆 The winner is the turtle with color: {winner_color.upper()}!{Color.END}")
    time.sleep(3)

if __name__ == "__main__" :
    main()
