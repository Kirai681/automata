import pygame
import config as c
from pygame.sprite import Sprite


class Item(Sprite):
    def __init__(self, x, y, direction, item_type, image=None):
        super().__init__()
        self.x = x
        self.y = y
        self.direction = direction
        self.item_type = item_type

        if image is None:
            self.image = pygame.Surface((c.CELL_SIZE // 2, c.CELL_SIZE // 2))
            self.image.fill((255, 100, 100))
        else:
            self.image = pygame.transform.scale(
                image,
                (c.CELL_SIZE, c.CELL_SIZE),
            )

        self.rect = self.image.get_rect()
        self.rect.center = (
            x * c.CELL_SIZE + c.CELL_SIZE // 2,
            y * c.CELL_SIZE + c.CELL_SIZE // 2,
        )

    def move(self): ...

    def update(self): ...
