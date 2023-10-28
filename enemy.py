import random
import typing
import pygame as pg


from player import Player
from constants import ENEMIES_SPEED


class Enemy(pg.sprite.Sprite):
    last_id = 0

    def __init__(
        self,
        pos_x: int,
        pos_y: int,
        sprite_filepath: str,
    ):
        pg.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.image = pg.image.load(sprite_filepath).convert_alpha()
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
        self.speed = random.choice(ENEMIES_SPEED)
        Enemy.last_id += 1
        self.id = Enemy.last_id

    def __repr__(self) -> str:
        return f'Enemy sprite #{self.id}'

    def __define_sprite_quadrant(self, other_sprite: typing.Self | Player) -> tuple[int, int]:
        sign: typing.Callable[[int], int] = lambda x: (x > 0) - (x < 0)
        enemy_center_x, enemy_center_y = self.rect.center
        other_sprite_center_x, other_sprite_center_y = other_sprite.rect.center
        sign_x = sign(other_sprite_center_x - enemy_center_x)
        sign_y = sign(other_sprite_center_y - enemy_center_y)
        return sign_x, sign_y

    def update(self, player: Player, enemies_group: pg.sprite.Group) -> None:
        collide_list = pg.sprite.spritecollide(self, enemies_group, False)
        if len(collide_list) > 1:
            for ally_sprite in collide_list:
                if ally_sprite.id != self.id:
                    sign_x, sign_y = self.__define_sprite_quadrant(ally_sprite)
                    self.pos_x -= random.choice([sign_x * self.speed, 0])
                    self.pos_y -= random.choice([sign_y * self.speed, 0])
        else:
            sign_x, sign_y = self.__define_sprite_quadrant(player)
            self.pos_x += sign_x * self.speed
            self.pos_y += sign_y * self.speed
        self.rect = self.image.get_rect(topleft=(self.pos_x, self.pos_y))
