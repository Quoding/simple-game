import pygame
import sys
from square import Square
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FPS = 7

# Set up
game_running = True
POS_X = 400
POS_Y = 300
vel_x = 0
vel_y = 0
score = 0

# Init pygame
init_result = pygame.init()

# Create a game window
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Set title
pygame.display.set_caption("My simple game")
clock = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 32)

# Make the user controlled square spawn at pos_x, pos_y
game_square = Square(POS_X, POS_Y)

# Spawn an objective square randomly on the canvas
objective_square = Square(random.randint(0, 31) * 25, random.randint(0, 23) * 25)


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


def isOutOfBounds(square):
    """Check to make sure that the player square isn't out of bounds. If he is, return True, else return False"""
    if square.pos_x > 775:
        return True
    if square.pos_y > 575:
        return True
    if square.pos_x < 0:
        return True
    if square.pos_y < 0:
        return True


def gotObjective(game_square, obj_square):
    """Check if player got the objective. If he did, change coordinates of the objective square"""
    if game_square.pos_x == obj_square.pos_x and game_square.pos_y == obj_square.pos_y:
        obj_square.pos_x = random.randint(0, 31) * 25
        obj_square.pos_y = random.randint(0, 23) * 25
        return True
    return False


while game_running:
    clock.tick(FPS)
    for event in pygame.event.get():
        # Insures user can quit using the X button or exit on wms
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.KEYDOWN:
            # Process keydown events
            if event.key == pygame.K_w:
                # print("Move forwards")
                game_square.vel_y = -25
                game_square.vel_x = 0
            elif event.key == pygame.K_s:
                # print("Move backwards")
                game_square.vel_y = 25
                game_square.vel_x = 0
            elif event.key == pygame.K_a:
                # print("Move left")
                game_square.vel_x = -25
                game_square.vel_y = 0
            elif event.key == pygame.K_d:
                # print("Move right")
                game_square.vel_x = 25
                game_square.vel_y = 0

    # Make canvas white (i.e. reset the display to the current game state)
    game_window.fill(WHITE)

    # Handle velocity of the square
    game_square.pos_x += game_square.vel_x
    game_square.pos_y += game_square.vel_y

    # Check if player out of bounds
    if isOutOfBounds(game_square):
        game_running = False
        break

    # Check if player acquired the objective square, if so, change objective square coordinates
    if gotObjective(game_square, objective_square):
        score += 1

    # Display user controlled square
    filled_rect = pygame.Rect(game_square.pos_x, game_square.pos_y, 25, 25)
    pygame.draw.rect(game_window, (0, 0, 0), filled_rect)

    # Display objective square
    empty_rect = pygame.Rect(objective_square.pos_x, objective_square.pos_y, 25, 25)
    pygame.draw.rect(game_window, (255, 0, 0), empty_rect, 3)

    # Display scoreboard
    text = font.render("Score: " + str(score), True, BLACK)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, 25)
    game_window.blit(text, textRect)

    # Update display
    pygame.display.update()

# Exit gracefully
pygame.quit()
sys.exit()
