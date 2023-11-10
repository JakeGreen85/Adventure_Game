import pygame, sys, random, time
from pygame.locals import*

pygame.init()
mainClock = pygame.time.Clock()
BLACK = (0,0,0)
WHITE = (255,255,255)

windowSurface = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption("Test")

mainmenu = pygame.image.load("Game Images/Pic Fin/Backgrounds/Main Menu.png")
Rect1 = pygame.draw.rect(windowSurface, WHITE, (5, 5, 10, 10))
windowSurface.blit(mainmenu, Rect1)

pygame.display.update()
mainClock.tick(40)
