import pygame

class Kitten(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self) #call Sprite intializer
    self.image = pygame.image.load('150.jpg')
    self.rect = self.image.get_rect()
    self.rect.center = (250, 250)

pygame.init()
screen = pygame.display.set_mode((500, 500))

background = pygame.Surface(screen.get_size())
background.fill((250, 250, 250))

kitten = Kitten()
allsprites = pygame.sprite.RenderPlain((kitten))

# game loop
while True:
  #Handle Input Events
  for event in pygame.event.get():
    pass

  screen.blit(background, (0, 0))
  allsprites.draw(screen) 
  pygame.display.flip() 

# -> Introducing a kitten to the game
# -> The kitten is a sub class to pygame.sprite.Sprite - a 2-dimensional image
# -> cut cat, but it just sits there... not much of a game