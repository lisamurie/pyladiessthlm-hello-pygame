import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))

background = pygame.Surface(screen.get_size())
background.fill((250, 250, 250))

# game loop
while True:
  #Handle Input Events
  for event in pygame.event.get():
    pass

  screen.blit(background, (0, 0))
  pygame.display.flip() 

# -> yay, window stays - and we've got a game loop
# -> a game loop is where we figure out what should happen next in our game
  # * both based on what the user has done and one what is happening in the game
# -> the game loop runs until the user quits the game
# -> we are also prepared to look at what the user is doing, with the pygame.event.get() for-loop