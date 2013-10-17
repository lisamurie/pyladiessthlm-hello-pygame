import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

background = pygame.Surface(screen.get_size())
background.fill((250, 250, 250))

# -> we get a white canvas, but it immediately disappears!