import random
import pygame as pg


from constants import (
    GAME_TITLE, ICON_FILEPATH,
    AMBIENT_FILEPATH, GET_HURT_SOUND_FILEPATH,
    ENEMIES_SPRITES,
    PLAYER_IFRAMES,
)
from settings import Settings
from enemy import Enemy
from pickup import Pickup
from player import Player
from controls import player_controls_handler, events_handler
from renders import render_intro, render_frame, render_outro


def initialize_game(settings: Settings) -> pg.Surface:
    pg.init()
    pg.mixer.music.load(AMBIENT_FILEPATH)
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.1)
    base_suface = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption(GAME_TITLE)
    pg.display.set_icon(pg.image.load(ICON_FILEPATH))
    return base_suface


def initialize_pickups(settings: Settings, pickups_group: pg.sprite.Group) -> None:
    first_pickup = Pickup(settings.screen_width, settings.screen_height, pickups_group)
    pg.time.set_timer(pg.USEREVENT, first_pickup.lifetime_sec * 330)  


def initialize_enemies(settings: Settings, enemies_group: pg.sprite.Group) -> None:
    random.shuffle(ENEMIES_SPRITES)
    for enemy_number in range(settings.difficulty.value):
        enemy_y = (enemy_number) * (settings.screen_height // settings.difficulty.value)
        Enemy(settings.screen_width - 100, enemy_y, ENEMIES_SPRITES[enemy_number], enemies_group)


def respond_to_pickups_collide(
    player: Player,
    enemies_group: pg.sprite.Group,
    pickups_group: pg.sprite.Group
) -> Player:
    player_collide = pg.sprite.spritecollideany(player, pickups_group)
    if player_collide:
        player.score += 1
        player_collide.kill()
    for enemy_sprite in enemies_group:
        pg.sprite.spritecollide(enemy_sprite, pickups_group, dokill=True)    
    return player


def respond_to_enemies_collide(player: Player, enemies_group) -> Player:
    collide = pg.sprite.spritecollideany(player, enemies_group)
    if collide and not player.invinsibility_frames:
        if player.hp > 1:
            pg.mixer.Sound(GET_HURT_SOUND_FILEPATH).play()
        player.hp -= 1
        player.invinsibility_frames = PLAYER_IFRAMES
    return player


def respond_to_player_death(
    base_surface: pg.Surface,
    player: Player,
    settings: Settings,
) -> Settings:
    if player.hp <= 0:
        settings.game_on = False
        render_outro(base_surface, settings)
    return settings


def main() -> None: 
    game_config = Settings()
    base_surface = initialize_game(game_config)
    current_player = Player(game_config.screen_width // 2, game_config.screen_height // 2)
    pickups: pg.sprite.Group = pg.sprite.Group()
    enemies: pg.sprite.Group = pg.sprite.Group()
    initialize_pickups(game_config, pickups)
    initialize_enemies(game_config, enemies)
    render_intro(base_surface, game_config)
    while game_config.game_on:
        render_frame(base_surface, current_player, pickups, enemies, game_config)
        game_config = events_handler(game_config, pickups)
        current_player = player_controls_handler(current_player)
        enemies.update(current_player, enemies)
        pickups.update()
        current_player = respond_to_enemies_collide(current_player, enemies)
        current_player = respond_to_pickups_collide(current_player, enemies, pickups)
        game_config = respond_to_player_death(base_surface, current_player, game_config)
        if current_player.invinsibility_frames: current_player.invinsibility_frames -= 1
        pg.time.Clock().tick(game_config.target_fps)
    pg.quit()

if __name__ == '__main__':
    main()
