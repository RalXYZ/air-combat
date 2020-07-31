import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Air Combat")

aircraft = pygame.image.load("../img/magenta_block.png")
bullet = pygame.image.load("../img/bullet.png")

bulletList = []

while True:
    screen.fill((255, 255, 255))

    x, y = pygame.mouse.get_pos()
    x -= aircraft.get_width() / 2
    y -= aircraft.get_height() / 2
    screen.blit(aircraft, (int(x), int(y)))

    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            bulletList.append(list(pygame.mouse.get_pos()))
        if event.type == QUIT:
            exit()

    tempList = []
    for point in bulletList:
        screen.blit(bullet, (int(point[0]), int(point[1])))
        point[1] -= 0.2
        if point[1] > 0:
            tempList.append(point)
    bulletList = tempList

    pygame.display.update()
