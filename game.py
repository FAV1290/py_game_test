import pygame


from constants import PLAYER_MODEL_FILEPATH
from config import TARGET_FPS
from settings import Settings
from player import Player
from controls import player_controls_handler, events_handler
from renders import render_intro, render_frame


def main() -> None:
    current_settings = Settings()
    current_player = Player(model_filepath = PLAYER_MODEL_FILEPATH)
    base_surface = current_settings.initialize_game()
    render_intro(base_surface)
    while current_settings.game_on:
        current_settings = events_handler(current_settings)
        if not current_settings.game_on:
            continue
        current_player = player_controls_handler(current_player)
        render_frame(base_surface, current_player)
        pygame.time.Clock().tick(TARGET_FPS)


if __name__ == '__main__':
    main()
