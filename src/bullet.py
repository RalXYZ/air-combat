import pygame
from src import constants


class Bullet:
    def __init__(self):
        self.__list = []
        self.__shootSpeed = 0.2
        self.__relativeSpeed = 0.05
        self.__bulletImg = pygame.image.load('../img/bullet.png')

    def add(self, position: tuple, baseVelocity: tuple) -> None:
        self.__list.append({'position': list(position), 'velocity': baseVelocity})

    def removeOutside(self) -> None:
        self.__list = list(filter(lambda point: 0 < point['position'][1] < constants.windowHeight, self.__list))

    def fly(self) -> None:
        for point in self.__list:
            point['position'][0] += point['velocity'][0] * self.__relativeSpeed
            point['position'][1] += point['velocity'][1] * self.__relativeSpeed
            point['position'][1] -= self.__shootSpeed

    def display(self, screen) -> None:
        for point in self.__list:
            screen.blit(self.__bulletImg, (int(point['position'][0]), int(point['position'][1])))
