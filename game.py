import pygame as pg


from constants import ICON_FILEPATH, GAME_TITLE, AMBIENT_FILEPATH
from settings import Settings
from pickup import Pickup
from player import Player
from controls import player_controls_handler, events_handler
from renders import render_intro, render_frame


def initialize_game(settings: Settings) -> pg.Surface:
    pg.init()
    pg.mixer.music.load(AMBIENT_FILEPATH)
    pg.mixer.music.play(-1)
    base_suface = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption(GAME_TITLE)
    pg.display.set_icon(pg.image.load(ICON_FILEPATH))
    return base_suface


def initialize_pickups(settings: Settings) -> None:
    first_pickup = Pickup(settings.screen_width, settings.screen_height)
    pg.time.set_timer(pg.USEREVENT, first_pickup.lifetime_sec * 250)  


def check_pickups_collide(player: Player) -> Player:
    collide = pg.sprite.spritecollideany(player, Pickup.pickups)
    if collide:
        player.score += 1
        collide.kill()
    return player


def main() -> None: 
    game_config = Settings()
    base_surface = initialize_game(game_config)
    current_player = Player(game_config.screen_width // 2, game_config.screen_height // 2)
    initialize_pickups(game_config)
    render_intro(base_surface, game_config)
    while game_config.game_on:
        game_config = events_handler(game_config)
        if game_config.game_on:
            current_player = player_controls_handler(current_player)
            render_frame(base_surface, current_player, Pickup.pickups, game_config)
        current_player = check_pickups_collide(current_player)
        pg.time.Clock().tick(game_config.target_fps)


if __name__ == '__main__':
    main()
