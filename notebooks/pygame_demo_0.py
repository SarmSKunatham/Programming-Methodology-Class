# 1 - import packages
import pygame
import sys

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH =  1080
WINDOW_HEIGHT = 720
FRAME_RATE = 30

# 3 - Initialize pygame
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: images/ sounds / etc.

# 5 - Initialize vairables

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # 8 - Do any per frame actions
    # 9 - Clear the window
    window.fill(BLACK)
    # 10 - Draw all window elements
    pygame.draw.circle(window, (0, 0, 255), (250, 250), 75)
    # 11 - Update the window
    pygame.display.update()
    # 12 - Ensure frame rate 
    clock.tick(FRAME_RATE)
