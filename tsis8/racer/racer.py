
import pygame
import random

pygame.init()

FPS = 60
WIDTH, HEIGHT = 400, 600
STEP_g = 5
enemy_step = 10

# color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

clock = pygame.time.Clock()

s_cor_e = 0  # time
s_cor_e_coins = 0  # SCORE

# fonts
font = pygame.font.SysFont("Verdana", 20)
font1 = pygame.font.SysFont("Verdana", 60)
game_over = font1.render("Game Over", True, BLACK)

# display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cars")

# load pictures
background = pygame.image.load('bkg.png')

# переменные для движения заднего фона
bgY = 0
bgY2 = - background.get_height()
BGSPEED = 5


class Player(pygame.sprite.Sprite):  # класс игрока
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):  # движение
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-STEP_g, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(STEP_g, 0)
        if self.rect.top > 0:
            if pressed_keys[pygame.K_UP]:
                self.rect.move_ip(0, -STEP_g)
        if self.rect.bottom < HEIGHT:
            if pressed_keys[pygame.K_DOWN]:
                self.rect.move_ip(0, STEP_g)

    def draw(self, surface):  # отрисовка
        surface.blit(self.image, self.rect)


class Coins(pygame.sprite.Sprite):  # класс монеток

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dollar.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(24, WIDTH - 24), random.randint(24, HEIGHT - 24))

    def update(self):  # рандомное появление монеток
        # self.rect.center = (random.randint(24,WIDTH - 24), random.randint(24,HEIGHT - 24))
        self.rect.center = (random.randint(24, WIDTH - 24), 0)

    def move(self):  # движение вниз
        self.rect.move_ip(0, 7)
        if self.rect.bottom > HEIGHT:
            self.top = 0
            self.rect.center = (random.randint(24, WIDTH - 24), 0)

    def draw(self, surface):  # отрисовка
        surface.blit(self.image, self.rect)


pl = Player()  # объект игрока

c = Coins()  # объект монетки
coins = pygame.sprite.Group()  # группа монеток
coins.add(c)  # добавление монетки в группу
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # проверка на закрытие окна
            finished = True
    pl.update()
    if pygame.sprite.spritecollideany(pl, coins):  # проверка столкновения игрока с монеткой
        s_cor_e_coins += 1
        coins.update()
    screen.blit(background, (0, bgY))
    screen.blit(background, (0, bgY2))
    # движение заднего фона
    if bgY > background.get_height():
        bgY = -background.get_height()
    if bgY2 > background.get_height():
        bgY2 = -background.get_height()
    bgY += BGSPEED
    bgY2 += BGSPEED
    pl.draw(screen)
    c.draw(screen)
    c.move()
    score_coins_img = font.render(f'{s_cor_e_coins}', True, RED)
    screen.blit(score_coins_img, (10, 35))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()