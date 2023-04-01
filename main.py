import pygame
import sys
import networkFunctions
import threading


def ping_and_draw(ip_address, bar_x, bar_y, bar_width, bar_height):
    if networkFunctions.ping(ip_address):
        pygame.draw.rect(screen, bar_colors[0], (bar_x, bar_y, bar_width, bar_height))
    else:
        pygame.draw.rect(screen, bar_colors[1], (bar_x, bar_y, bar_width, bar_height))

    font = pygame.font.SysFont("Calibri", 15)
    img = font.render(ip_address, True, (0, 0, 0))
    screen.blit(img, (bar_x, bar_y))


devices_to_ping = [
    {"ip_address": "192.168.0.106", "reachable": False, "response_time": None},
    {"ip_address": "192.168.189.1", "reachable": False, "response_time": None},
    {"ip_address": "192.168.1.3", "reachable": False, "response_time": None},
]

threads = []

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 400
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
font = pygame.font.SysFont("Arial", 24)

# Set the color of the bars
bar_colors = [(0, 255, 0), (255, 0, 0)]

# Set the width and height of the bars
bar_width = 0
bar_height = 30

# Set the number of bars with the amount of devices to ping
num_bars = len(devices_to_ping)

# Set the initial positions and speeds of the bars
bars = []
bar_identifier = 0
for i in range(num_bars):
    bar_x = 0
    bar_y = (i + 1) * (bar_height + 10)
    bar_speed = 8
    bar_identifier += 1
    bars.append((bar_x, bar_y, bar_speed, bar_identifier))

# Update the Pygame display
pygame.display.flip()

# Set the clock
clock = pygame.time.Clock()
ping_results = [None] * num_bars

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the bars from left to right
   # for i in range(num_bars):

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the bars
    for i in range(num_bars):
        bar_width += 0.8
        if bar_width >= screen_width:
            bar_width = 0

        bar_x, bar_y, bar_speed, bar_identifier = bars[i]
        ip_address = devices_to_ping[i]["ip_address"]

        thread = threading.Thread(target=ping_and_draw, args=(ip_address, bar_x, bar_y, bar_width, bar_height))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


    # Update the screen
    pygame.display.update()



    # Pause the game loop to control the frame rate
    clock.tick(30)
