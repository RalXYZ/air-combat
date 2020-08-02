import pygame
from src import constants


class Bullet:
    def __init__(self):
        self.__list = []
        self.__shoot_speed = 0.2
        self.__relative_speed = 0.05
        self.__bullet_img = pygame.image.load('../img/bullet.png')

    def add(self, position: tuple, baseVelocity: tuple) -> None:
        self.__list.append({'position': list(position), 'velocity': baseVelocity})

    def remove_outside(self) -> None:
        self.__list = list(filter(lambda point: 0 < point['position'][1] < constants.WINDOW_HEIGHT, self.__list))

    def fly(self) -> None:
        for point in self.__list:
            point['position'][0] += point['velocity'][0] * self.__relative_speed
            point['position'][1] += point['velocity'][1] * self.__relative_speed
            point['position'][1] -= self.__shoot_speed

    def display(self, screen) -> None:
        for point in self.__list:
            screen.blit(self.__bullet_img, (int(point['position'][0]), int(point['position'][1])))
