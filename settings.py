import pygame


from config import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import AMBIENT_FILEPATH, ICON_FILEPATH, GAME_TITLE


class Settings:
    game_on = False
    is_ambient_active = False


    def quit_game(self) -> None:
        self.game_on = False
        pygame.quit()

    
    def initialize_ambient(self) -> None:
        pygame.mixer.music.load(AMBIENT_FILEPATH)
        pygame.mixer.music.play(-1)
        self.is_ambient_active = True

    
    def initialize_game(self) -> pygame.Surface:
        pygame.init()
        base_suface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        pygame.display.set_icon(pygame.image.load(ICON_FILEPATH))
        self.initialize_ambient()
        self.game_on = True
        return base_suface
