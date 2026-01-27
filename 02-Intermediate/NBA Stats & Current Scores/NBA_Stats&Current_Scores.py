from nba_api.live.nba.endpoints import scoreboard
import csv

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
# Fetch Games
# =========================
games = scoreboard.ScoreBoard().get_dict()["scoreboard"]["games"]

filename = "nba_scores.csv"

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    # العواميد بالشكل اللي انت عايزه
    writer.writerow(["Home Team", "Away Team", "Home Score", "Away Score", "Clock"])
    
    count = 0
    for game in games:
        if "homeTeam" in game and "awayTeam" in game:
            home = game["homeTeam"]["teamTricode"]
            away = game["awayTeam"]["teamTricode"]
            home_score = game["homeTeam"]["score"]
            away_score = game["awayTeam"]["score"]
            status = game.get("gameStatus", "")
            
            if status == 3:  
                clock = "Match End"
            else:
                clock = game.get("gameClock", "N/A")

            writer.writerow([home, away, home_score, away_score, clock])
            count += 1

            print(
                f"{Color.BLUE}{away}{Color.END} {Color.GREEN}{away_score}{Color.END} vs "
                f"{Color.BLUE}{home}{Color.END} {Color.GREEN}{home_score}{Color.END} | "
                f"Clock: {clock}"
            )

if count == 0:
    print(f"{Color.YELLOW}No valid games to save today.{Color.END}")
else:
    print(f"{Color.CYAN}Saved {count} games to {filename}{Color.END}")
