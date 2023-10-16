import pygame as pg


from pickup import Pickup
from player import Player
from settings import Settings
from constants import (
    TEXT_FONT, TEXT_FONT_SIZE, INTRO_TEXT_LIST,
    INTERFACE_FONT, INTERFACE_FONT_SIZE,
    RGB_BLACK, RGB_WHITE,
    BACKGROUND_FILEPATH,
)


def draw_score(base_surface: pg.Surface, player: Player) -> None:
    score_font = pg.font.Font(INTERFACE_FONT, INTERFACE_FONT_SIZE)
    score_surface = score_font.render(str(player.score), True, RGB_WHITE, None)
    base_surface.blit(score_surface, score_surface.get_rect(center=(50, 50)))    


def render_frame(base_surface: pg.Surface, player: Player, pickups_group: pg.sprite.Group, settings: Settings) -> None:
    background = pg.image.load(BACKGROUND_FILEPATH).convert()
    background = pg.transform.scale(background, (settings.screen_width, settings.screen_height))
    base_surface.blit(background, (0, 0))
    pickups_group.draw(base_surface)
    base_surface.blit(player.image, player.rect)
    draw_score(base_surface, player)
    pg.display.update()
    Pickup.pickups.update()


def render_intro(base_surface: pg.Surface, settings: Settings) -> None:
    intro_font = pg.font.Font(TEXT_FONT, TEXT_FONT_SIZE)
    base_surface.fill(RGB_BLACK)
    line_x = settings.screen_width // 2
    line_y = settings.screen_height // 2 - TEXT_FONT_SIZE
    for text_line in INTRO_TEXT_LIST:
        line_surface = intro_font.render(text_line, True, RGB_WHITE, None)
        line_rect = line_surface.get_rect(center=(line_x, line_y))
        base_surface.blit(line_surface, line_rect)
        line_y += TEXT_FONT_SIZE*2
    pg.display.update()
    pg.event.clear()
    pg.event.wait()
