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


class Bomb(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('bomb.png')
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = randint(0, 450), randint(0, 450)

    def update(self):
        self.image = load_image('boom.png')


if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    running = True
    all_sprites = pygame.sprite.Group()
    for i in range(20):
        all_sprites.add(Bomb())
    while running:
        screen.fill('white')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for bomb in all_sprites:
                    if (event.pos[0] in range(bomb.rect.x, bomb.rect.x + 51)) and \
                        (event.pos[1] in range(bomb.rect.y, bomb.rect.y + 51)):
                        bomb.update()

        all_sprites.draw(screen)
        pygame.display.flip()
