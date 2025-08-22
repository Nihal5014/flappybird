import pygame


HEIGHT = 900
WIDTH = 864
TITLE = 'flappybird'
run =True
score = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption(TITLE)
flying = False
gameover = False
flappybird = pygame.image.load("images\\flappybird.png")
flappybird2 = pygame.image.load("images\\flappybird2.png")
flappybird3 = pygame.image.load("images\\flappybird3.png")
floorimg= pygame.image.load("images\\floor.png")
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
        self.velocity = 0
        self.counter = 0
        self.click = False  
    def update(self):

        if flying == True:
            if self.velocity< 8:      
                self.velocity = self.velocity + 0.2
            if pygame.mouse.get_pressed()[0]==1 and self.click == False:
                self.click = True 
                self.velocity = -10
            if pygame.mouse.get_pressed()[0]==0:
                self.click = False

            self.rect.y = self.rect.y + self.velocity
        if gameover == False:
            self.counter = self.counter + 1
            if self.counter > 5:
                self.counter = 0
                self.index = self.index + 1
                if self.index >= 3:
                    self.index = 0
                self.image = self.birds[self.index] 
class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = floorimg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        if flying == True:
            self.rect.x = self.rect.x - 1
            if self.rect.x < -36:
                self.rect.x = 0


class Pole(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pole
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Background(pygame.sprite.Sprite):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.image = flappybirdbg
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


flappy = Bird(200,400)
flappy_group = pygame.sprite.Group()
flappy_group.add(flappy)

floor=Floor(0,768)
floor_group = pygame.sprite.Group()
floor_group.add(floor)

while run ==True:
    screen.blit(flappybirdbg,(0,0))
    flappy_group.draw(screen)
    floor_group.draw(screen)
    floor_group.update()
    flappy_group.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and gameover ==False and flying ==False:
            flying = True




    pygame.display.update()

    
    
