import pygame
from src.display import gameDisplay
from src import constants

pygame.init()
screen = pygame.display.set_mode((constants.windowWidth, constants.windowHeight), 0, 32)
pygame.display.set_caption("Air Combat")

gameDisplay(screen)
