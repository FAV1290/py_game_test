import pygame


from constants import AMBIENT_FILEPATH


class Settings:
    def __init__(self):
        self.game_on = True
        self.is_ambient_active = False

    def quit_game(self) -> None:
        self.game_on = False
        pygame.quit()
    
    def initialize_ambient(self) -> None:
        pygame.mixer.music.load(AMBIENT_FILEPATH)
        pygame.mixer.music.play(-1)
        self.is_ambient_active = True
