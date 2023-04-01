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
bar_colors = [(0, 255, 0), (255, 0, 0)]

# Set the width and height of the bars
bar_width = 60
bar_height = 30

# Set the number of bars
num_bars = 10

# Add more colors to bar_colors to match the number of bars
# while len(bar_colors) < num_bars:
#     #bar_colors.append((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     bar_colors.append((0, 255, 0))

# Set the initial positions and speeds of the bars
bars = []
bar_identifier = 0
for i in range(num_bars):
    bar_x = 0
    bar_y = (i + 1) * (bar_height + 10)
    bar_speed = 8
    bar_identifier += 1
    bars.append((bar_x, bar_y, bar_speed, bar_identifier))

# Set the clock
clock = pygame.time.Clock()

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    # Move the bars from left to right
    for i in range(num_bars):
        bar_width += 0.8
        if bar_width >= screen_width:
            bar_width = 0

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the bars
    for i in range(num_bars):
        bar_x, bar_y, bar_speed, bar_identifier = bars[i]
        if bar_identifier % 2 == 0:
            pygame.draw.rect(screen, bar_colors[1], (bar_x, bar_y, bar_width, bar_height))
        else:
            pygame.draw.rect(screen, bar_colors[0], (bar_x, bar_y, bar_width, bar_height))


    # Update the screen
    pygame.display.update()

    # Pause the game loop to control the frame rate
    clock.tick(60)
