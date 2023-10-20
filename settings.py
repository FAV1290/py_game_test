from enums import Difficulty
from config import TARGET_FPS, SCREEN_WIDTH, SCREEN_HEIGHT, DIFFICULTY


class Settings:
    def __init__(
        self,
        target_fps: int = TARGET_FPS,
        screen_width: int = SCREEN_WIDTH,
        screen_height: int = SCREEN_HEIGHT,
        difficulty: Difficulty = DIFFICULTY,
    ):
        self.game_on = True
        self.is_ambient_active = True
        self.target_fps = target_fps
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.difficulty = difficulty
