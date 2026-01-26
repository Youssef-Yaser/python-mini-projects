# =========================
# Alarm Clock
# =========================

import pygame
import time

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
    CLEAR = '\033c'  # Clear terminal


# =========================
# Play sound
# =========================
def play_sound(mp3_file: str):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()
    print(f"{Color.CYAN}{Color.BOLD}Sound is playing...{Color.END}")

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    print(f"{Color.GREEN}{Color.BOLD}Sound finished!{Color.END}")


# =========================
# Alarm 
# =========================
def alarm(total_seconds: int, sound_file: str):
    elapsed = 0
    while elapsed < total_seconds:
        time.sleep(1)
        elapsed += 1

        remaining = total_seconds - elapsed
        minutes_left = remaining // 60
        seconds_left = remaining % 60

        print(f"{Color.YELLOW}Alarm will sound in {minutes_left:02d}:{seconds_left:02d}{Color.END}", end="\r")

    print(f"\n{Color.RED}{Color.BOLD}Time's up!{Color.END}")
    play_sound(sound_file)


# =========================
# Main 
# =========================
def main():
    try:
        mins = int(input(f"{Color.CYAN}Enter minutes to wait: {Color.END}"))
        secs = int(input(f"{Color.CYAN}Enter seconds to wait: {Color.END}"))
    except ValueError:
        print(f"{Color.RED}Invalid input! Please enter numbers only.{Color.END}")
        return

    total_seconds = mins * 60 + secs
    mp3_file = "e3Bd97ayuEU.mp3"  # ضع هنا اسم ملف MP3 الخاص بك
    print(f"{Color.GREEN}Alarm set for {mins} minutes and {secs} seconds.{Color.END}")
    alarm(total_seconds, mp3_file)


if __name__ == "__main__":
    main()
