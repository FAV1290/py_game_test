import pygame as pg


from pickup import Pickup
from player import Player
from settings import Settings


def player_controls_handler(player: Player) -> Player:
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[pg.K_LEFT] or keys_pressed[pg.K_a]:
        player.pos_x -= player.speed
    elif keys_pressed[pg.K_RIGHT] or keys_pressed[pg.K_d]:
        player.pos_x += player.speed
    if keys_pressed[pg.K_UP] or keys_pressed[pg.K_w]:
        player.pos_y -= player.speed 
    elif keys_pressed[pg.K_DOWN] or keys_pressed[pg.K_s]:
        player.pos_y += player.speed
    player.update()
    return player


def events_handler(current_settings: Settings, pickups_group: pg.sprite.Group) -> Settings:
    for event in pg.event.get():
        if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or event.type == pg.QUIT:
            current_settings.game_on = False
        elif event.type == pg.KEYDOWN and event.key == pg.K_m:
            if current_settings.is_ambient_active:
                pg.mixer.music.pause()
            else:
                pg.mixer.music.unpause()
            current_settings.is_ambient_active = not current_settings.is_ambient_active
        elif event.type == pg.USEREVENT:
            Pickup(current_settings.screen_width, current_settings.screen_height, pickups_group)
    return current_settings
