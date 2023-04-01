import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the color of the bars
bar_colors = []

# Set the width and height of the bars
bar_width = 60
bar_height = 30

# Set the number of bars
num_bars = 10

# Add more colors to bar_colors to match the number of bars
while len(bar_colors) < num_bars:
    #bar_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    bar_colors.append((0, 255, 0))

# Set the initial positions and speeds of the bars
bars = []
for i in range(num_bars):
    bar_x = 0
    bar_y = (i + 1) * (bar_height + 10)
    bar_speed = 8
    bars.append((bar_x, bar_y, bar_speed))

# Set the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the bars
    for i in range(num_bars):
        bar_x, bar_y, bar_speed = bars[i]
        bar_x += bar_speed

        # Check if the bar has reached the right edge of the screen
        if bar_x + bar_width > screen_width:
            bar_x = 0

        bars[i] = (bar_x, bar_y, bar_speed)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the bars
    for i in range(num_bars):
        bar_x, bar_y, bar_speed = bars[i]
        pygame.draw.rect(screen, bar_colors[i], (bar_x, bar_y, bar_width, bar_height))

    # Update the screen
    pygame.display.update()

    # Pause the game loop to control the frame rate
    clock.tick(60)
