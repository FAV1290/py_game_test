import pygame


from constants import ICON_FILEPATH, GAME_TITLE, PLAYER_MODEL_FILEPATH
from config import SCREEN_WIDTH, SCREEN_HEIGHT, TARGET_FPS
from settings import Settings
from player import Player
from controls import player_controls_handler, events_handler
from renders import render_intro, render_frame


def initialize_game(settings: Settings) -> pygame.Surface:
    pygame.init()
    base_suface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(GAME_TITLE)
    pygame.display.set_icon(pygame.image.load(ICON_FILEPATH))
    settings.initialize_ambient()
    return base_suface


def main() -> None:
    current_settings = Settings()
    current_player = Player(model_filepath=PLAYER_MODEL_FILEPATH)
    base_surface = initialize_game(current_settings)
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
