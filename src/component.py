import pygame
import config as c
from pygame.sprite import Sprite


class Component(Sprite):
    def __init__(self, x, y, direction="down", image=None):
        super().__init__()
        self.x = x
        self.y = y
        self.direction = direction

        if image is None:
            self.image = pygame.Surface((c.CELL_SIZE, c.CELL_SIZE))
            self.image.fill((200, 200, 200))
        else:
            self.image = pygame.transform.scale(
                image,
                (c.CELL_SIZE, c.CELL_SIZE),
            )

        self.rect = self.image.get_rect()
        self.rect.topleft = (x * c.CELL_SIZE, y * c.CELL_SIZE)

    def update(self): ...
