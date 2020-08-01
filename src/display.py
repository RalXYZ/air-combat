import pygame
from pygame.locals import *
from sys import exit
from src.bullet import Bullet


def gameDisplay(screen):
    from src import bullet
    aircraftImg = pygame.image.load("../img/magenta_block.png")
    bulletImg = pygame.image.load("../img/bullet.png")

    baseVelocity = (0, 0)
    velocityFLag = 0

    while True:
        screen.fill((0, 0, 0))

        x, y = pygame.mouse.get_pos()
        x -= aircraftImg.get_width() / 2
        y -= aircraftImg.get_height() / 2
        screen.blit(aircraftImg, (int(x), int(y)))

        event = pygame.event.poll()
        if event.type == MOUSEMOTION:
            baseVelocity = event.rel
            velocityFLag = 50
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:  # LB
                bullet.bulletList.append([list(pygame.mouse.get_pos()), baseVelocity])
        if event.type == KEYDOWN:
            if event.key == K_k:
                bullet.bulletList.append([list(pygame.mouse.get_pos()), baseVelocity])
        elif event.type == QUIT:
            exit()

        if velocityFLag > 0:
            velocityFLag -= 1
        elif velocityFLag == 0:
            baseVelocity = (0, 0)

        Bullet.fly()
        Bullet.display(screen, bulletImg)
        Bullet.removeOutside()

        pygame.display.update()
