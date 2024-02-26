import pygame
import sys
from pygame.locals import *
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = os.path.join(BASE_DIR, 'assets')

pygame.init()

FPS = 30
fpsClock = pygame.time.Clock()

window = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Animation')

WHITE = (255, 255, 255)
catImg = pygame.image.load(os.path.join(ASSET_DIR, 'cat.png'))
catX = 10
catY = 10
direction = 'right'

while True:
    window.fill(WHITE)
    
    if direction == 'right':
        catX += 5
        if catX == 280:
            direction = 'down'
    elif direction == 'down':
        catY += 5
        if catY == 220:
            direction = 'left'
    elif direction == 'left':
        catX -= 5
        if catX == 10:
            direction = 'up'
    elif direction == 'up':
        catY -= 5
        if catY == 10:
            direction = 'right'
    
    window.blit(catImg, (catX, catY))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    fpsClock.tick(FPS)
