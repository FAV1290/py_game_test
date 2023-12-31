import time
import random
import pygame as pg


from constants import PICKUP_SPRITE_FILEPATH, PICKUP_LIFETIME_SEC


class Pickup(pg.sprite.Sprite):
    def __init__(
        self,
        screen_width: int,
        screen_height: int,
        pickups_group: pg.sprite.Group,
        sprite_filepath: str = PICKUP_SPRITE_FILEPATH,
        lifetime_sec: int = PICKUP_LIFETIME_SEC,
    ):
        pg.sprite.Sprite.__init__(self)
        self.pos_x = random.randint(20, screen_width - 20)
        self.pos_y = random.randint(20, screen_height - 20)
        self.image = pg.image.load(sprite_filepath).convert_alpha()
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.created_at = time.time()
        self.lifetime_sec = lifetime_sec
        self.add(pickups_group)

    def update(self) -> None:
        if time.time() - self.created_at >= self.lifetime_sec:
            self.kill()
