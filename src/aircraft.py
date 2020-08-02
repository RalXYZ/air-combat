import random
import pygame
from src import constants


class Aircraft:
    def __init__(self):
        random.seed()
        self.__list = []
        self.__aircraft_img = pygame.image.load('../img/magenta_block.png')

    def spawn(self):
        aircraft_position = [random.randint(0, constants.WINDOW_WIDTH), 0]
        self.__list.append({'position': aircraft_position, 'velocity': (0, 0.05), 'hp': 1})

    def display(self, screen):
        for point in self.__list:
            screen.blit(self.__aircraft_img, (int(point['position'][0] - self.__aircraft_img.get_width() / 2), int(point['position'][1] - self.__aircraft_img.get_height() / 2)))
