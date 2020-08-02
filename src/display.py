import pygame
from src.bullet import Bullet

enemyEmergeTime = 1000
enemyEmergeEventID = pygame.USEREVENT + 1


def gameDisplay(screen):
    myBullet = Bullet()
    pygame.time.set_timer(enemyEmergeEventID, enemyEmergeTime)

    aircraftImg = pygame.image.load('../img/magenta_block.png')

    baseVelocity = (0, 0)
    velocityFLag = 0

    while True:
        screen.fill((0, 0, 0))

        x, y = pygame.mouse.get_pos()
        x -= aircraftImg.get_width() / 2
        y -= aircraftImg.get_height() / 2
        screen.blit(aircraftImg, (int(x), int(y)))

        event = pygame.event.poll()
        if event.type == pygame.MOUSEMOTION:
            baseVelocity = event.rel
            velocityFLag = 50
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # LB
                myBullet.add(pygame.mouse.get_pos(), baseVelocity)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                myBullet.add(pygame.mouse.get_pos(), baseVelocity)
        elif event.type == enemyEmergeEventID:
            pass  # TODO: enemy aircraft emerge
        elif event.type == pygame.QUIT:
            exit()

        if velocityFLag > 0:
            velocityFLag -= 1
        elif velocityFLag == 0:
            baseVelocity = (0, 0)

        myBullet.fly()
        myBullet.display(screen)
        myBullet.removeOutside()

        pygame.display.update()
