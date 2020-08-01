import pygame
from pygame.locals import *
from sys import exit
from src.bullet import Bullet


def gameDisplay(screen):
    from src import bullet
    aircraftImg = pygame.image.load("../img/magenta_block.png")
    bulletImg = pygame.image.load("../img/bullet.png")

    while True:
        screen.fill((0, 0, 0))

        x, y = pygame.mouse.get_pos()
        x -= aircraftImg.get_width() / 2
        y -= aircraftImg.get_height() / 2
        screen.blit(aircraftImg, (int(x), int(y)))

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                bullet.bulletList.append(list(pygame.mouse.get_pos()))
            if event.type == QUIT:
                exit()

        for point in bullet.bulletList:
            screen.blit(bulletImg, (int(point[0]), int(point[1])))
            point[1] -= 0.2
        Bullet.rmOutOfScreen()

        pygame.display.update()
