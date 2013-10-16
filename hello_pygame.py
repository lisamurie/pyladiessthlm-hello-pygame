

# what is pygame?
# what can it be used for?
# what have other people made?
# (sudo) pip install pygame

# based on pygame/examples/chimp.py

import pygame, sys, os
from pygame.locals import *

# make the cat move away from the mouse?
# LOL a cat that is afraid of the mouse... :S
# you win if you manage to catch the cat?

# am I going to type all this? no...
# uncomment line by line?
# maybe put all steps in separate files and run after displaying the new code?
# maybe make macros?

# 1.
pygame.init()
# -> something happens? but almost nothing

# 2. 
screen = pygame.display.set_mode((450, 450))
# -> there was something there, but it went right away...

# 3.
while 1:
  pass
# -> yay, window stays - and we've got a game loop
# -> a game loop is where we figure out what should happen next in our game
  # * both based on what the user has done and one what is happening in the game
# -> the game loop runs until the user quits the game
# -> when we click anywhere the game has no idea what to do...

# 5. 
  for event in pygame.event.get():
    if event.type == MOUSEBUTTONDOWN:
      break


'''
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


class Kitten:
  def __init__(self):
    self.sprite = Sprite()
    #self.sprite.image, self.sprite.rect = 
'''