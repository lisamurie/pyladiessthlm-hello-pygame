import pygame, random
from pygame.locals import *

class Kitten(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self) #call Sprite intializer
    self.image = pygame.image.load('150.jpg')
    self.rect = self.image.get_rect()
    self.rect.center = (250, 250)

  def run_away_from(self, position):
    if self.rect.collidepoint(position):
      self.rect.move_ip(random.uniform(-25, 25), random.uniform(-25, 25))

pygame.init()
screen = pygame.display.set_mode((500, 500))

background = pygame.Surface(screen.get_size())
background.fill((250, 250, 250))

clock = pygame.time.Clock()

kitten = Kitten()
allsprites = pygame.sprite.RenderPlain((kitten))

while 1:
  #Handle Input Events
  for event in pygame.event.get():
    if event.type == MOUSEMOTION:
      kitten.run_away_from(event.dict['pos'])

  screen.blit(background, (0, 0))
  allsprites.draw(screen) 
  pygame.display.flip() 
