import pygame
import time
import random
import sounds
from pygame.locals import K_ESCAPE
pygame.init()

class player:
    def __init__(self, coins, level, name, health, dmgmulti, shield, critchance, critmulti, accuracy, world, storytasks):
        self.coins = coins
        self.level = level
        self.name = name
        self.health = health
        self.dmgmulti = dmgmulti
        self.shield = shield
        self.critchance = critchance
        self.critmulti = critmulti
        self.accuracy = accuracy
        self.world = world
        self.storytasks = storytasks

class Button:
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        self.buttonText = ''
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False


class enemy:
    def __init__(self, hp, mind, maxd):
        self.hp = hp
        self.min = mind
        self.max = maxd

guy = player(0, 0, 'bob', 50, 1.0, 0, 3, 3, 70, 1, False)
zombie = enemy(30, 2, 4)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
print(pygame.FULLSCREEN)
w, h = screen.get_size()
pygame.display.set_caption('stick vs zombie')

def show_image(image, scale, x, y):
    img_width, img_height = image.get_size()
    image = pygame.transform.scale(image, (img_width * scale, img_height * scale))
    # screen.blit(image, ((width - image.get_width()) * scale, (height - image.get_height()) * scale))
    screen.blit(image, (x, y))
    pygame.display.flip()

show_image(pygame.image.load('R.png'), 0.5, 100, 100)
show_image(pygame.image.load('zombie.jpg'), 0.2, 1200, 400)
running = True
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(f'Health: {guy.health}', True, (255, 255, 255))
text_rect = text.get_rect()
text_rect.center = (300, 800)
screen.blit(text, text_rect)
text2 = font.render(f'Health: {zombie.hp}', True, (255, 255, 255))
text_rect2 = text2.get_rect()
text_rect2.center = (1000, 800)
screen.blit(text2, text_rect2)
text3 = font.render(f'e', True, (255, 255, 255))
text_rect3 = text3.get_rect()
text_rect3.center = (600, 100)
variable = 0
variable2 = 0
text4 = font.render(f'There is a cooldown to attacking.', True, (255, 255, 255))
text_rect4 = text4.get_rect()
text_rect4.center = (1000, 1000)
screen.blit(text4, text_rect4)

button = Button(w//2, h//2, 100, 50, 'attack')
quitting = False
delay = 0
num = 0
sounds.endlessplay('fightmusic.mp3', 0)
atkcd = 0
while running:
    time.sleep(1 / 30)
    num += 1
    if atkcd > 0:
        atkcd -= 1
    if pygame.mouse.get_pressed()[0] and button.buttonRect.collidepoint(pygame.mouse.get_pos()) and atkcd == 0:
        atkcd = 30
        if zombie.hp > 0:
            variable = random.randint(zombie.min, zombie.max)
            variable2 = random.randint(2, 7)
            guy.health -= variable
            zombie.hp -= variable2
            if zombie.hp < 0:
                zombie.hp = 0
            text = font.render(f'Health: {guy.health}', True, (255, 255, 255))
            text2 = font.render(f'Health: {zombie.hp}', True, (255, 255, 255))
            sounds.playsound('explode.mp3', 1)
            text3 = font.render(f'Player took: {variable} damage! '
                                f'Zombie took {variable2} damage!', True, (255, 255, 255))
            screen.fill(pygame.Color("blue"), (200, 600, 1000, 400))
            screen.fill(pygame.Color("blue"), (500, 0, 900, 300))
            pygame.display.update()
            screen.blit(text, text_rect)
            screen.blit(text2, text_rect2)
            screen.blit(text3, text_rect3)
    pygame.display.update()
    # button.process()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitting = True
            pygame.quit()

            # return
            # running = False
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                quitting = True
                running = False
        # if pygame.mouse.get_pressed()[0] and mysprite.rect.collidepoint(pygame.mouse.get_pos()):
        #     print("You have opened a chest!")
