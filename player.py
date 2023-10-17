import pygame as pg


from constants import PLAYER_SPRITE_FILEPATH


class Player(pg.sprite.Sprite):
    def __init__(
        self, 
        pos_x: int,
        pos_y: int,
        sprite_filepath: str = PLAYER_SPRITE_FILEPATH,
    ) -> None:
        pg.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pg.image.load(sprite_filepath).convert_alpha()
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.score = 0
    
    def update(self):
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
