import pygame
import textwrap
import graphics_display as graphs

pygame.init()
pixel_font = pygame.font.Font("Grand9K Pixel.ttf", 20)

dialogue_box = pygame.Rect((0, 0), (500, 150))
dialogue_box.center = (graphs.window_size[0] / 2, graphs.window_size[1] / 2 * 1.7)

# ---
# Dialogue scripts
# ---
old_man_diag = ['Huh? Oh it\'s you again.', 'Just don\'t forget the map I gave ya, and you\'ll be fine.', 'Go now, lemme rest in peace.']

rock_school_diag = ['Oh, hey there, stranger!', 'Are you here to listen to our concert later tonight?', 'They\'ve gotten quite popular recently.',
                    'I\'m glad our school is growing! It kind of reminds me of the city\'s jazz age.', 'Maybe music will unite us again, just like '
                                                                                                       'back then...']


# ---
# Dialogue functions
# ---
def wrap_text(surface, font, text, position, text_color, bg_color):
    x = position[0]
    y = position[1]
    lines = textwrap.wrap(text, 40)

    pygame.draw.rect(surface, bg_color, dialogue_box)
    for line in lines:
        curr_line = font.render(line, True, text_color)
        surface.blit(curr_line, (x, y))
        y += curr_line.get_height() + 4

        pygame.display.update()


def display_dialogue(surface, dialogue_list, text_color, bg_color):
    for line in dialogue_list:
        time_now = pygame.time.get_ticks()
        finish_time = time_now + 3000

        wrap_text(surface, pixel_font, line, (130, 530), text_color, bg_color)

        while time_now < finish_time:
            pass
            time_now = pygame.time.get_ticks()
