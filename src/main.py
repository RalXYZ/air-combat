import pygame
from src.display import gameDisplay
from src import constants

pygame.init()
screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption("Air Combat")

gameDisplay(screen)
