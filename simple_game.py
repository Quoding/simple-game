import pygame
import sys
from square import Square
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

init_result = pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("My simple game")

# Set up
game_running = True
pos_x = 0
pos_y = 0

# Make the user controlled square spawn at pos_x, pos_y
game_square = Square(pos_x, pos_y)

# Spawn an objective square randomly on the canvas
objective_square = Square(random.randint(0, 31) * 25, random.randint(0, 23) * 25)
score = 0


def preventOutOfBounds(square):
    """Check to make sure that the player square isn't out of bounds. If he is about to make, prevent it."""
    if square.pos_x > 775:
        square.pos_x = 775
    if square.pos_y > 575:
        square.pos_y = 575
    if square.pos_x < 0:
        square.pos_x = 0
    if square.pos_y < 0:
        square.pos_y = 0

    return square


def gotObjective(game_square, obj_square):
    """Check if player got the objective. If he did, change coordinates of the objective square
    """
    if game_square.pos_x == obj_square.pos_x and game_square.pos_y == obj_square.pos_y:
        obj_square.pos_x = random.randint(0, 31) * 25
        obj_square.pos_y = random.randint(0, 23) * 25
        return True
    return False


while game_running:
    # Game content
    for event in pygame.event.get():
        # Insures user can quit using the X button or exit on wms
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            # Process keydown events
            if event.key == pygame.K_w:
                print("Move forwards")
                game_square.pos_y -= 25
            elif event.key == pygame.K_s:
                print("Move backwards")
                game_square.pos_y += 25
            elif event.key == pygame.K_a:
                print("Move left")
                game_square.pos_x -= 25
            elif event.key == pygame.K_d:
                print("Move right")
                game_square.pos_x += 25

    # Content here
    game_window.fill(WHITE)
    preventOutOfBounds(game_square)
    # print("Current position {} {}".format(game_square.pos_x, game_square.pos_y))
    if gotObjective(game_square, objective_square):
        score += 1
    # ---- Draw shapes here ----
    filled_rect = pygame.Rect(game_square.pos_x, game_square.pos_y, 25, 25)
    pygame.draw.rect(game_window, (0, 0, 0), filled_rect)

    empty_rect = pygame.Rect(objective_square.pos_x, objective_square.pos_y, 25, 25)
    pygame.draw.rect(game_window, (255, 0, 0), empty_rect, 3)

    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()
