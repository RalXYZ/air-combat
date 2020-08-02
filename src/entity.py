import random
import pygame
from src import constants


class Entity:
    def __init__(self, image_path: str):
        self._list = []
        self.__image = pygame.image.load(image_path)

    def new(self, position: tuple, base_velocity: tuple) -> None:
        self._list.append({'position': list(position), 'velocity': base_velocity})

    def remove_outside(self) -> None:
        self._list = list(filter(lambda point: 0 < point['position'][1] < constants.WINDOW_HEIGHT, self._list))

    def display(self, screen):
        for element in self._list:
            screen.blit(self.__image, (int(element['position'][0] - self.__image.get_width() / 2),
                                       int(element['position'][1] - self.__image.get_height() / 2)))


class Bullet(Entity):
    def __init__(self):
        super(Bullet, self).__init__('../img/bullet.png')
        self.__shoot_speed = 0.2
        self.__relative_speed = 0.05

    def fly(self) -> None:
        for point in self._list:
            point['position'][0] += point['velocity'][0] * self.__relative_speed
            point['position'][1] += point['velocity'][1] * self.__relative_speed
            point['position'][1] -= self.__shoot_speed


class Aircraft(Entity):
    def __init__(self):
        super(Aircraft, self).__init__('../img/magenta_block.png')
        random.seed()

    def new(self, position: tuple = None, base_velocity: tuple = None):
        if position is None:
            position = [random.randint(0, constants.WINDOW_WIDTH), 0]
        if base_velocity is None:
            base_velocity = (0, 0.05)
        self._list.append({'position': position, 'velocity': base_velocity, 'hp': 1})
