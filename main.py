import pygame
import sys
from pygame import *
pygame.init()



class GameSprite(sprite.Sprite):
    # конструктор класса
    def __init__(self,player_image, player_x, player_y, size_x, size_y):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y


    # метод, отрисовывающий героя на окне
    def reset(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))






class Player(GameSprite):
    # метод, в котором реализовано управление спрайтом по кнопкам стрелочкам клавиатуры
    def __init__(self,player_image, player_x, player_y, size_x ,size_y, player_x_speed, player_y_speed):
        # Вызываем конструктор класса (Sprite):
        GameSprite.__init__(self,player_image, player_x, player_y, size_x, size_y)
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed


class Wals():
    def __init__(self, barrier_x, barrier_y, size_y, size_x):
        self.x = barrier_x
        self.y = barrier_y
        self.size_x = size_x
        self.size_y = size_y
    def touch(self):
        if Alan.rect.x > self.x and Alan.rect.left < self.x + self.size_x:
            if Alan.rect.bottom > self.y + self.size_y:
                if Alan.rect.top < self.y + self.size_y:
                    Alan.rect.top = self.y + self.size_y - 1
                    Alan.y_speed = 0
            if Alan.rect.bottom > self.y and Alan.rect.top < self.y:
                Alan.rect.bottom = self.y + 1
                Alan.y_speed = 0
        if Alan.rect.y > self.y and Alan.rect.y < self.y + self.size_y:
            if Alan.rect.right > self.x:
                Alan.rect.right == self.x - 1
                Alan.x_speed = 0
            elif Alan.rect.x > self.x + self.size_x:
                if Alan.rect.right < self.x + self.size_x:
                    Alan.rect.x = self.x + self.size_x + 1
                    Alan.x_speed = 0






class animation():
    def __init__(self,anim_images, anim_count):
        self.images = anim_images
        self.counter = 0
        self.anim_count = anim_count
    def anim_print(self):
        Alan.image = transform.scale(image.load(self.images[self.counter]), (100, 170))
        self.rect = Alan.image.get_rect()
        self.rect.x = Alan.rect.x
        self.rect.y = Alan.rect.y
        if self.counter == self.anim_count:
            self.counter = 0
        else:
            self.counter += 1






            


#экран
width = 800
height = 950
fps = 45
timer = pygame.time.Clock()
white = (255, 255, 255)

#бэкраунд
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Похождение Алана')
bg = GameSprite('SPRITE BG 1.2.png',0, 0, 800, 950)
bg2 = GameSprite('bg2.png', -1 ,0 , 800, 950)

#старт
title_text = GameSprite('lobby text.png',100, 300, 600, 300)
text_start = GameSprite('text for start.png', 170, 340, 450, 150)
#главный герой
Alan = Player('empty.png' ,180, 150, 100, 170, 0, 0)
inventory = pygame.sprite.Group()


closet_counter = 0
closet = GameSprite('Sprite closet1.png', 25 ,800 , 300, 150)
barriers = sprite.Group(closet)
door_1 = GameSprite('Sprite door1.png',740, 700, 60, 180)
bed_1 = GameSprite('Sprite bed (3).png', 30, 100, 150, 250)
key_1 = GameSprite('key 1.png', 100, 700, 30, 45)
door1_key = GameSprite('door key.png', 745, 740, 40, 40)
room1 = pygame.sprite.Group(bg,closet, door_1, bed_1, door1_key, title_text, text_start)

bath = GameSprite('bath all/ванна1.png', 490, 770, 260 , 110)
toylet = GameSprite('toylet all/туалет1.png', 30 , 730 , 120, 100)
room2 = pygame.sprite.Group(bg2, bath,toylet)
wall_2_1 = Wals(0 , 680, 10, 300)
wall_2_2 = Wals(400, 680 , 10 , 300)

ALan_room = 0
Alan_anim_Up = animation(
[
    'up alan/ALan behind 1.png',
    'up alan/ALan behind 1.png',
    'up alan/ALan behind 2.png',
    'up alan/ALan behind 2.png',
    'up alan/ALan behind 5.png',
    'up alan/ALan behind 5.png',
    'up alan/ALan behind 1.png',
    'up alan/ALan behind 1.png',
    'up alan/ALan behind 4.png',
    'up alan/ALan behind 4.png',
    'up alan/ALan behind 3.png',
    'up alan/ALan behind 3.png',
    ],
    10,
)

Alan_anim_Down = animation(
    [
        'down alan/ALan up 1.png',
        'down alan/ALan up 1.png',
        'down alan/ALan up 4.png',
        'down alan/ALan up 4.png',
        'down alan/ALan up 2.png',
        'down alan/ALan up 2.png',
        'down alan/ALan up 1.png',
        'down alan/ALan up 1.png',
        'down alan/ALan up 3.png',
        'down alan/ALan up 3.png',
        'down alan/ALan up 5.png',
        'down alan/ALan up 5.png',

    ],10
)
Alan_anim_Left = animation(
    [
        'left/Sprite-0006 (3).png',
        'left/Sprite-0006 (3).png',
        'left/Sprite-0006 (4).png',
        'left/Sprite-0006 (4).png',
        'left/Sprite-0006 (5).png',
        'left/Sprite-0006 (5).png',
        'left/Sprite-0006 (6).png',
        'left/Sprite-0006 (6).png',

    ],6
)

Alan_anim_Right = animation(
    [
        'right/Sprite-0008.png',
        'right/Sprite-0009.png',
        'right/Sprite-0010.png',
        'right/Sprite-0011.png',

    ],3
)




blink_frequency = 400  # Частота мигания в миллисекундах
last_blink_time = 0
is_visible = True
space_pressed = False
start = False
run = True
while run:
    timer.tick(fps)

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    if ALan_room == 0:
        room1.draw(screen)
        Alan.reset()
        pygame.display.update()
        if Alan.rect.collidepoint(740, 700) and key_1 in inventory:
            room1.remove(door1_key)
            ALan_room = 1
            Alan.rect.y = 400
            Alan.rect.x = 50
        if Alan.rect.colliderect(closet.rect):
            closet_barrier = Wals(closet.rect.x, closet.rect.y, 150, 300)
            closet_barrier.touch()
            closet.image = transform.scale(image.load('Sprite closet3.png'), (300, 150))

            if len(inventory) == 0:
                room1.add(key_1)
        elif Alan.rect.colliderect(key_1):
            room1.remove(key_1)
            key_1.rect.y = 830
            key_1.rect.x = 55
            key_1.image = transform.scale(image.load('key 1.png'), (85, 115))
            inventory.add(key_1)
        else:
            closet.image = transform.scale(image.load('Sprite closet1.png'), (300, 150))



    if ALan_room == 1 :

        room2.draw(screen)
        Alan.reset()
        wall_2_1.touch()
        wall_2_2.touch()
        if Alan.rect.collidepoint(5, 500):
            ALan_room = 0
            Alan.rect.y = 700
            Alan.rect.x = 640
        pygame.display.update()

    current_time = pygame.time.get_ticks()
    if current_time - last_blink_time > blink_frequency:
        last_blink_time = current_time
        is_visible = not is_visible
    if is_visible and space_pressed is False:
        room1.add(text_start)
    else:
        room1.remove(text_start)
    if e.type == KEYDOWN:
        if e.key == K_SPACE:
            start = True

        if start is True:
            if e.key == K_LEFT and Alan.rect.x > 5:
                Alan.rect.x -=7
            elif e.key == K_RIGHT and Alan.rect.x + 110 < width- 5:
                Alan.rect.x += 7
            elif e.key == K_UP and Alan.rect.y > 0 :
                Alan.rect.y -= 7
            elif e.key == K_DOWN and Alan.rect.y + 180 < height - 5:
                Alan.rect.y += 7
            elif e.key == K_TAB:
                room1.add(inventory)
                room2.add(inventory)

        #Анимация открытия шкафа


    elif e.type == KEYUP:
        if e.key == K_SPACE:
            start = True
            Alan.image = transform.scale(image.load('down alan/ALan up 1.png'), (100, 170))
            bed_1.image = transform.scale(image.load('Sprite bed (2).png'), (150, 250))
            space_pressed = True
            room1.remove(title_text)
        if start is True:
            if e.key == K_LEFT:
                Alan.x_speed = 0
            elif e.key == K_RIGHT:
                Alan.x_speed = 0
            elif e.key == K_UP:
                Alan.y_speed = 0
            elif e.key == K_DOWN:
                Alan.y_speed = 0
            elif e.key == K_TAB:
                room1.remove(inventory)
                room2.remove(inventory)

    if start is True:
        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            Alan_anim_Up.anim_print()
        elif keys[K_DOWN]:
            Alan_anim_Down.anim_print()
        elif keys[K_RIGHT]:
            Alan_anim_Right.anim_print()
        elif keys[K_LEFT]:
            Alan_anim_Left.anim_print()











pygame.quit()