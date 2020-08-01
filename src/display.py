import pygame
from pygame.locals import *
from sys import exit
from src.bullet import Bullet


def gameDisplay(screen):
    myBullet = Bullet()

    aircraftImg = pygame.image.load("../img/magenta_block.png")

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
                myBullet.add([list(pygame.mouse.get_pos()), baseVelocity])
        if event.type == KEYDOWN:
            if event.key == K_k:
                myBullet.add([list(pygame.mouse.get_pos()), baseVelocity])
        elif event.type == QUIT:
            exit()

        if velocityFLag > 0:
            velocityFLag -= 1
        elif velocityFLag == 0:
            baseVelocity = (0, 0)

        myBullet.fly()
        myBullet.display(screen)
        myBullet.removeOutside()

        pygame.display.update()
