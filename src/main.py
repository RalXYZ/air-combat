import pygame
from src.display import gameDisplay

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Air Combat")

gameDisplay(screen)
