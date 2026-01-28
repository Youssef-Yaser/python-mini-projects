import random
import pygame
import math
import time

pygame.init()

# =====================
# Window Setup
# =====================
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

# =====================
# Game Settings
# =====================
TARGET_EVENT = pygame.USEREVENT
TARGET_INCREMENT = 400
TARGET_PADDING = 40

GAME_TIME = 30  # seconds

BG_COLOR = (0, 0, 0)

FONT = pygame.font.SysFont("arial", 26)
SMALL_FONT = pygame.font.SysFont("arial", 20)

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 80, 80)
BLUE = (0, 150, 255)


# =====================
# Target Class
# =====================
class Target:
    MAX_SIZE = 30
    GROWTH_RATE = 0.4
    COLOR = (255, 0, 0)
    SECOND_COLOR = (255, 255, 255)

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 0
        self.grow = True

    def update(self):
        if self.size >= self.MAX_SIZE:
            self.grow = False

        if self.grow:
            self.size += self.GROWTH_RATE
        else:
            self.size -= self.GROWTH_RATE

    def draw(self, win):
        if self.size > 0:
            pygame.draw.circle(win, self.COLOR, (self.x, self.y), int(self.size))
            pygame.draw.circle(win, self.COLOR, (self.x, self.y), int(self.size * 0.7))
            pygame.draw.circle(win, self.SECOND_COLOR, (self.x, self.y), int(self.size * 0.4))

    def collide(self, x, y):
        dist = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return dist <= self.size


# =====================
# Draw Everything
# =====================
def draw(win, targets, hits, misses, clicks, time_left):

    win.fill(BG_COLOR)

    for target in targets:
        target.draw(win)

    # ---- SCORE ----
    hits_text = FONT.render(f"Hits: {hits}", True, GREEN)
    misses_text = FONT.render(f"Misses: {misses}", True, RED)

    win.blit(hits_text, (10, 10))
    win.blit(misses_text, (10, 40))

    # ---- ACCURACY ----
    accuracy = (hits / clicks * 100) if clicks > 0 else 0
    acc_text = FONT.render(f"Accuracy: {accuracy:.1f}%", True, BLUE)
    win.blit(acc_text, (10, 70))

    # ---- TIMER ----
    timer_text = FONT.render(f"Time: {int(time_left)}", True, WHITE)
    win.blit(timer_text, (WIDTH - 140, 10))

    # ---- PROGRESS BAR ----
    bar_width = 200
    bar_height = 20
    bar_x = WIDTH - 220
    bar_y = 50

    progress = time_left / GAME_TIME

    pygame.draw.rect(win, WHITE, (bar_x, bar_y, bar_width, bar_height), 2)
    pygame.draw.rect(win, BLUE, (bar_x, bar_y, bar_width * progress, bar_height))

    pygame.display.update()


# =====================
# Main Game Loop
# =====================
def main():

    clock = pygame.time.Clock()
    run = True
    targets = []

    hits = 0
    misses = 0
    clicks = 0

    start_time = time.time()

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:

        clock.tick(60)

        elapsed = time.time() - start_time
        time_left = GAME_TIME - elapsed

        if time_left <= 0:
            break

        click = False
        mouse_x, mouse_y = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING, HEIGHT - TARGET_PADDING)
                targets.append(Target(x, y))

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets[:]:

            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            elif click and target.collide(mouse_x, mouse_y):
                targets.remove(target)
                hits += 1

        draw(WIN, targets, hits, misses, clicks, time_left)

    # =====================
    # Game Over Screen
    # =====================
    WIN.fill(BG_COLOR)

    accuracy = (hits / clicks * 100) if clicks > 0 else 0

    over_text = FONT.render("GAME OVER", True, WHITE)
    score_text = FONT.render(f"Hits: {hits}   Misses: {misses}", True, GREEN)
    acc_text = FONT.render(f"Accuracy: {accuracy:.1f}%", True, BLUE)

    WIN.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 80))
    WIN.blit(score_text, (WIDTH // 2 - 140, HEIGHT // 2 - 30))
    WIN.blit(acc_text, (WIDTH // 2 - 120, HEIGHT // 2 + 10))

    pygame.display.update()

    pygame.time.delay(3000)

    pygame.quit()


if __name__ == "__main__":
    main()
