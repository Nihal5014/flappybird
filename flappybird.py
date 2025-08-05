import pygame


HEIGHT = 800
WIDTH = 1000
TITLE = 'flappybird'
run =True
score = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)

flappybird = pygame.image.load("images\\flappybird.png")
flappybird2 = pygame.image.load("images\\flappybird2.png")
flappybird3 = pygame.image.load("images\\flappybird3.png")
floor= pygame.image.load("images\\floor.png")
pole= pygame.image.load("images\\pole.png")
flappybirdbg = pygame.image.load("images\\flappybirdbg.png")

class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.index = 0
        self.birds = [flappybird, flappybird2, flappybird3]
        self.image = self.birds[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

flappy = Bird(200,400)

