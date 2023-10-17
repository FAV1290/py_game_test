import pygame as pg


from constants import PLAYER_SPEED
from pickup import Pickup
from player import Player
from settings import Settings


def player_controls_handler(player: Player) -> Player:
    keys_pressed = pg.key.get_pressed()
    if keys_pressed[pg.K_LEFT]:
        player.pos_x -= PLAYER_SPEED
    elif keys_pressed[pg.K_RIGHT]:
        player.pos_x += PLAYER_SPEED
    if keys_pressed[pg.K_UP]:
        player.pos_y -= PLAYER_SPEED
    elif keys_pressed[pg.K_DOWN]:
        player.pos_y += PLAYER_SPEED
    player.update()
    return player


def events_handler(current_settings: Settings) -> Settings:
    for event in pg.event.get():
        if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE) or event.type == pg.QUIT:
            current_settings.game_on = False
            pg.quit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_m:
            if current_settings.is_ambient_active:
                pg.mixer.music.pause()
            else:
                pg.mixer.music.unpause()
            current_settings.is_ambient_active = not current_settings.is_ambient_active
        elif event.type == pg.USEREVENT:
            Pickup(current_settings.screen_width, current_settings.screen_height)
    return current_settings
