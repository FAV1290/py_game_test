import pygame


from constants import PLAYER_SPEED
from player import Player
from settings import Settings


def player_controls_handler(player: Player) -> Player:
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_LEFT]:
        player.pos_x -= PLAYER_SPEED
    elif keys_pressed[pygame.K_RIGHT]:
        player.pos_x += PLAYER_SPEED
    if keys_pressed[pygame.K_UP]:
        player.pos_y -= PLAYER_SPEED
    elif keys_pressed[pygame.K_DOWN]:
        player.pos_y += PLAYER_SPEED
    return player


def events_handler(current_settings: Settings) -> Settings:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_settings.quit_game()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_m:
            current_settings.is_ambient_active = not current_settings.is_ambient_active
            if current_settings.is_ambient_active:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()
    return current_settings
