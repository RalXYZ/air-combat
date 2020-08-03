import pygame
from src.entity import Bullet, Aircraft

enemy_emerge_time = 1000
enemy_emerge_event_id = pygame.USEREVENT + 1


def gameDisplay(screen):
    my_bullet = Bullet()
    enemy_aircraft = Aircraft()
    pygame.time.set_timer(enemy_emerge_event_id, enemy_emerge_time)

    aircraft_img = pygame.image.load('../img/magenta_block.png')

    base_velocity = (0, 0)
    velocity_flag = 0

    while True:
        screen.fill((0, 0, 0))

        x, y = pygame.mouse.get_pos()
        x -= aircraft_img.get_width() / 2
        y -= aircraft_img.get_height() / 2
        screen.blit(aircraft_img, (int(x), int(y)))

        event = pygame.event.poll()
        if event.type == pygame.MOUSEMOTION:
            base_velocity = event.rel
            velocity_flag = 50
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # LB
                my_bullet.new(pygame.mouse.get_pos(), base_velocity)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                my_bullet.new(pygame.mouse.get_pos(), base_velocity)
        elif event.type == enemy_emerge_event_id:
            enemy_aircraft.new()
        elif event.type == pygame.QUIT:
            exit()

        if velocity_flag > 0:
            velocity_flag -= 1
        elif velocity_flag == 0:
            base_velocity = (0, 0)

        my_bullet.fly()
        my_bullet.display(screen)
        my_bullet.remove_outside()

        enemy_aircraft.display(screen)
        enemy_aircraft.hit_bullet(my_bullet.list)
        enemy_aircraft.fly()
        enemy_aircraft.remove_outside()

        pygame.display.update()
