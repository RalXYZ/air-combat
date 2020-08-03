import random, abc
import pygame
from src import constants


class Entity:
    def __init__(self, image_path: str) -> None:
        self.list = []
        self.image = pygame.image.load(image_path)

    def new(self, position: tuple, base_velocity: tuple) -> None:
        self.list.append({'position': list(position), 'velocity': base_velocity})

    def remove_outside(self) -> None:
        self.list = list(filter(lambda point: -100 < point['position'][1] < constants.WINDOW_HEIGHT + 100, self.list))

    def display(self, screen) -> None:
        for element in self.list:
            screen.blit(self.image, (int(element['position'][0] - self.image.get_width() / 2),
                                     int(element['position'][1] - self.image.get_height() / 2)))

    @abc.abstractmethod
    def fly(self) -> None:
        pass


class Bullet(Entity):
    def __init__(self) -> None:
        super(Bullet, self).__init__('../img/bullet.png')
        self.__shoot_speed = 0.2
        self.__relative_speed = 0.05

    def fly(self) -> None:
        for element in self.list:
            element['position'][0] += element['velocity'][0] * self.__relative_speed
            element['position'][1] += element['velocity'][1] * self.__relative_speed
            element['position'][1] -= self.__shoot_speed


class Aircraft(Entity):
    def __init__(self) -> None:
        super(Aircraft, self).__init__('../img/magenta_block.png')
        random.seed()

    def new(self, position: tuple = None, base_velocity: tuple = None) -> None:
        if position is None:
            position = [random.randint(0, constants.WINDOW_WIDTH), - self.image.get_height() / 2]
        if base_velocity is None:
            base_velocity = (0, 0.05)
        self.list.append({'position': position, 'velocity': base_velocity, 'hp': 1})

    def fly(self) -> None:
        for element in self.list:
            element['position'][0] += element['velocity'][0]
            element['position'][1] += element['velocity'][1]

    def hit_bullet(self, bullet_list: list) -> None:
        for i in range(len(self.list) - 1, -1, -1):
            for bullet in bullet_list:
                if (bullet['position'][0] - self.image.get_width() / 2) < self.list[i]['position'][0] < (bullet['position'][0] + self.image.get_width() / 2) and \
                        (bullet['position'][1] - self.image.get_height() / 2) < self.list[i]['position'][1] < (bullet['position'][1] + self.image.get_height() / 2):
                    del self.list[i]
                    return


