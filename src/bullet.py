import pygame
from src import constants


class Bullet:
    def __init__(self):
        self.__list = []
        self.__shootSpeed = 0.2
        self.__relativeSpeed = 0.05
        self.__bulletImg = pygame.image.load("../img/bullet.png")

    def add(self, content: list) -> None:
        self.__list.append(content)

    def removeOutside(self) -> None:
        tempList = []
        for point in self.__list:
            if 0 < point[0][1] < constants.windowHeight:
                tempList.append(point)
        self.__list = tempList

    def fly(self) -> None:
        for point in self.__list:
            point[0][0] += point[1][0] * self.__relativeSpeed
            point[0][1] += point[1][1] * self.__relativeSpeed
            point[0][1] -= self.__shootSpeed

    def display(self, screen) -> None:
        for point in self.__list:
            screen.blit(self.__bulletImg, (int(point[0][0]), int(point[0][1])))
