import pygame
import random
from pygame.locals import *

pygame.init()

# Game window settings
screen_width = 600
screen_height = 600
cell_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Cute Pink Snake')

# Colors
bg_color = (255, 192, 203)  # Light pink
snake_color = (255, 105, 180)  # Pink
food_color = (255, 20, 147)  # Deep pink
score_color = (0, 0, 0)  # Black

# Snake variables
snake_pos = [(screen_width // 2, screen_height // 2)]
snake_direction = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
snake_length = 1

# Food variables
food_pos = (random.randint(0, (screen_width - cell_size) // cell_size) * cell_size,
            random.randint(0, (screen_height - cell_size) // cell_size) * cell_size)

# Score variables
score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    screen.fill(bg_color)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"
            elif event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"

    # Move the snake
    x, y = snake_pos[0]
    if snake_direction == "UP":
        y -= cell_size
    elif snake_direction == "DOWN":
        y += cell_size
    elif snake_direction == "LEFT":
        x -= cell_size
    elif snake_direction == "RIGHT":
        x += cell_size

    # Check for collisions with food
    if (x, y) == food_pos:
        food_pos = (random.randint(0, (screen_width - cell_size) // cell_size) * cell_size,
                    random.randint(0, (screen_height - cell_size) // cell_size) * cell_size)
        snake_length += 1
        score += 1
    else:
        snake_pos.pop()

    # Check for collisions with walls or itself
    if x < 0 or x >= screen_width or y < 0 or y >= screen_height or (x, y) in snake_pos:
        running = False

    # Update snake position
    snake_pos.insert(0, (x, y))

    # Draw food
    pygame.draw.rect(screen, food_color, (food_pos[0], food_pos[1], cell_size, cell_size))

    # Draw snake
    for pos in snake_pos:
        pygame.draw.rect(screen, snake_color, (pos[0], pos[1], cell_size, cell_size))

    # Draw score
    score_text = font.render(f"Score: {score}", True, score_color)
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.update()

    # Cap the frame rate
    pygame.time.Clock().tick(10)  # You can adjust this value to change the speed of the snake

# Display game over message
screen.fill(bg_color)
game_over_text = font.render("Game Over", True, score_color)
score_text = font.render(f"Your score: {score}", True, score_color)
screen.blit(game_over_text, (screen_width // 2 - 100, screen_height // 2 - 50))
screen.blit(score_text, (screen_width // 2 - 100, screen_height // 2))
pygame.display.update()

# Wait for a while before quitting
pygame.time.wait(2000)

# Quit pygame
pygame.quit()
