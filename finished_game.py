import pygame, sys, os
from pygame.locals import *


#functions to create our resources
def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

class Kitten(pygame.sprite.Sprite):
    def __init__(self):
    	pygame.sprite.Sprite.__init__(self) #call Sprite intializer
        self.image, self.rect = load_image('150.jpg', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0


pygame.init()
screen = pygame.display.set_mode((450, 450))

#Create The Backgound
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))

#Display The Background
screen.blit(background, (0, 0))
pygame.display.flip()

kitten = Kitten()
allsprites = pygame.sprite.RenderPlain((kitten))

while 1:
  #Draw Everything
  screen.blit(background, (0, 0))
  allsprites.draw(screen)
  pygame.display.flip()