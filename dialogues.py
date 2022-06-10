import pygame
import time
import textwrap
import graphics_display as graphs

pygame.init()
pixel_font = pygame.font.Font("Grand9K Pixel.ttf", 20)

diag_box = pygame.Rect((0, 0), (500, 150))
diag_box.center = (graphs.window_size[0] / 2, graphs.window_size[1] / 2 * 1.7)


def box_text(surface, font, position, text, text_color, bg_color):
    x = position[0]
    y = position[1]
    lines = textwrap.wrap(text, 40)

    pygame.draw.rect(surface, bg_color, diag_box)
    for line in lines:
        curr_line = font.render(line, True, text_color)
        surface.blit(curr_line, (x, y))
        y += curr_line.get_height() + 4

        pygame.display.update()


def display_dialogue(surface, dialogue_list, text_color, bg_color):
    for line in dialogue_list:
        box_text(surface, pixel_font, (130, 530), line, text_color, bg_color)
        time.sleep(3)


old_man_diag = ['Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 'Excepteur sint occaecat cupidatat non '
                                                                            'proident.', 'Duis aute irure dolor in '
                                                                                         'reprehenderit in voluptate '
                                                                                         'velit esse cillum dolore eu '
                                                                                         'fugiat nulla pariatur.']
