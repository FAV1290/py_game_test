import pygame as pg


from player import Player
from settings import Settings
from constants import (
    INTRO_TEXT_FONT, INTRO_TEXT_FONT_SIZE, INTRO_TEXT_LIST,
    INTERFACE_FONT, INTERFACE_FONT_SIZE,
    RGB_BLACK, RGB_WHITE,
    BACKGROUND_FILEPATH, DEATH_SCREEN_FILEPATH,
    DEATH_SOUND_FILEPATH,
    HP_UNIT_FILEPATH,
)


def draw_score(base_surface: pg.Surface, player: Player) -> None:
    score_font = pg.font.Font(INTERFACE_FONT, INTERFACE_FONT_SIZE)
    score_surface = score_font.render(f'{str(player.score * 100000)}$', True, RGB_WHITE, None)
    base_surface.blit(score_surface, score_surface.get_rect(topleft=(20, 80)))


def draw_hp_bar(base_surface: pg.Surface, player: Player) -> None:
    for hp_unit in range(player.hp):
        hp_surface = pg.image.load(HP_UNIT_FILEPATH).convert_alpha()
        hp_unit_x = 20 + hp_unit*40
        base_surface.blit(hp_surface, hp_surface.get_rect(topleft=(hp_unit_x, 20)))


def render_frame(
    base_surface: pg.Surface,
    player: Player,
    pickups_group: pg.sprite.Group,
    enemies_group: pg.sprite.Group,
    settings: Settings,
) -> None:
    background = pg.image.load(BACKGROUND_FILEPATH).convert()
    background = pg.transform.scale(background, (settings.screen_width, settings.screen_height))
    base_surface.blit(background, (0, 0))
    pickups_group.draw(base_surface)
    enemies_group.draw(base_surface)
    base_surface.blit(player.image, player.rect)
    draw_score(base_surface, player)
    draw_hp_bar(base_surface, player)
    pg.display.update()


def render_intro(base_surface: pg.Surface, settings: Settings) -> None:
    intro_font = pg.font.Font(INTRO_TEXT_FONT, INTRO_TEXT_FONT_SIZE)
    base_surface.fill(RGB_BLACK)
    line_x = settings.screen_width // 2
    line_y = settings.screen_height // 2 - INTRO_TEXT_FONT_SIZE
    for text_line in INTRO_TEXT_LIST:
        line_surface = intro_font.render(text_line, True, RGB_WHITE, None)
        line_rect = line_surface.get_rect(center=(line_x, line_y))
        base_surface.blit(line_surface, line_rect)
        line_y += INTRO_TEXT_FONT_SIZE * 2
    pg.display.update()
    pg.event.clear()
    pg.event.wait()


def render_outro(base_surface: pg.Surface, settings: Settings) -> None:
    pg.mixer.music.pause()
    pg.mixer.Sound(DEATH_SOUND_FILEPATH).play()
    death_screen_x = settings.screen_width // 2
    death_screen_y = settings.screen_height // 2
    death_screen_image = pg.image.load(DEATH_SCREEN_FILEPATH).convert()
    death_screen_rect = death_screen_image.get_rect(center=(death_screen_x, death_screen_y))
    base_surface.fill(RGB_BLACK)
    base_surface.blit(death_screen_image, death_screen_rect)
    pg.display.update()
    pg.time.delay(5000)
