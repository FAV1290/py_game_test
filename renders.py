import pygame

from player import Player
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from constants import TEXT_FONT, TEXT_FONT_SIZE, INTRO_TEXT_LIST, RGB_BLACK, RGB_WHITE


def render_frame(base_surface: pygame.Surface, current_player: Player) -> None:
    base_surface.fill(RGB_BLACK)
    base_surface.blit(current_player.create_surface(), current_player.create_rect())
    pygame.display.update()


def render_intro(base_surface) -> None:
    intro_font = pygame.font.Font(TEXT_FONT, TEXT_FONT_SIZE)
    base_surface.fill(RGB_BLACK)
    line_x = SCREEN_WIDTH // 2
    line_y = SCREEN_HEIGHT // 2 - TEXT_FONT_SIZE
    for text_line in INTRO_TEXT_LIST:
        line_surface = intro_font.render(text_line, True, RGB_WHITE, None)
        line_rect = line_surface.get_rect(center=(line_x, line_y))
        base_surface.blit(line_surface, line_rect)
        line_y += TEXT_FONT_SIZE*2
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait()
    