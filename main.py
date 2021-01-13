import os
import sys
from random import randint
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
width, height = 500, 500
size = width, height
screen = pygame.display.set_mode(size)
bombs = pygame.sprite.Group()


class Bomb(pygame.sprite.Sprite):
    image = load_image('bomb.png')
    image_of_boom = load_image('boom.png')

    def __init__(self):
        super().__init__(all_sprites)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = randint(0, 450), randint(0, 450)
        while pygame.sprite.spritecollideany(self, bombs):
            self.rect.x, self.rect.y = randint(0, 450), randint(0, 450)
        self.add(bombs)

    def update(self, *args):
        if self.rect.collidepoint(event.pos):
            self.image = Bomb.image_of_boom


all_sprites = pygame.sprite.Group()
for i in range(20):
    Bomb()

running = True
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for bomb in all_sprites:
                bomb.update()
    all_sprites.draw(screen)
    pygame.display.flip()
