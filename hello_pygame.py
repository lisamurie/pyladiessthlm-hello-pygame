# (sudo) pip install pygame
import pygame, sys, os
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((450, 450))
pygame.display.set_caption('PyLadies!')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

clock = pygame.time.Clock()

while 1:
  clock.tick(60)

  exit = False

  #Handle Input Events
  for event in pygame.event.get():
    if event.type == QUIT:
      exit = True
    elif event.type == KEYDOWN and event.key == K_ESCAPE:
      exit = True
    elif event.type == MOUSEBUTTONDOWN:
      exit = True

  if exit:
    break

