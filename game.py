import random
import pygame as pg


from constants import ICON_FILEPATH, GAME_TITLE, AMBIENT_FILEPATH, ENEMIES_SPRITES
from settings import Settings
from enemy import Enemy
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
    pg.time.set_timer(pg.USEREVENT, first_pickup.lifetime_sec * 330)  


def initialize_enemies(settings: Settings) -> None:
    random.shuffle(ENEMIES_SPRITES)
    for enemy_number in range(settings.difficulty.value):
        enemy_y = (enemy_number) * (settings.screen_height // settings.difficulty.value)
        Enemy(settings.screen_width - 100, enemy_y, ENEMIES_SPRITES[enemy_number])   


def check_pickups_collide(player: Player) -> Player:
    player_collide = pg.sprite.spritecollideany(player, Pickup.pickups)
    if player_collide:
        player.score += 1
        player_collide.kill()
    for enemy_sprite in Enemy.enemies:
        pg.sprite.spritecollide(enemy_sprite, Pickup.pickups, dokill=True)    
    return player


def check_enemies_collide(player: Player) -> Player:
    collide = pg.sprite.spritecollideany(player, Enemy.enemies)
    if collide:
        player.hp -= 1
    return player


def main() -> None: 
    game_config = Settings()
    base_surface = initialize_game(game_config)
    current_player = Player(game_config.screen_width // 2, game_config.screen_height // 2)
    initialize_pickups(game_config)
    initialize_enemies(game_config)
    render_intro(base_surface, game_config)
    while game_config.game_on:
        game_config = events_handler(game_config)
        if game_config.game_on:
            current_player = player_controls_handler(current_player)
            render_frame(base_surface, current_player, Pickup.pickups, Enemy.enemies, game_config)
        current_player = check_pickups_collide(current_player)
        current_player = check_enemies_collide(current_player)
        if current_player.hp <= 0:
            game_config.game_on = False
        Enemy.enemies.update(player=current_player)
        pg.time.Clock().tick(game_config.target_fps)


if __name__ == '__main__':
    main()
