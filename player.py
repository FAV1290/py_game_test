import pygame


from config import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import DEFAULT_MODEL_FILEPATH


class Player:
    default_pos_x = SCREEN_WIDTH // 2
    default_pos_y = SCREEN_HEIGHT // 2
    default_model_filepath = DEFAULT_MODEL_FILEPATH

    def __init__(
        self, 
        model_filepath: str = default_model_filepath,
        pos_x: int = default_pos_x,
        pos_y: int = default_pos_y
    ) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.model_filepath = model_filepath

    def create_surface(self) -> pygame.Surface:
        return pygame.image.load(self.model_filepath)
    
    def create_rect(self) -> pygame.Rect:
        return self.create_surface().get_rect(center=(self.pos_x, self.pos_y))
    