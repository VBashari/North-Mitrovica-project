import sys
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
old_man_diag_intro = ['Umm, excuse me, sir?', 'Old man:\nWhat do you want, kid, couldn\'t you see I was resting these old bones?', 'I\'m sorry to '
                                                                                                                                   'wake you up '
                                                                                                                                   'from your '
                                                                                                                                   'sleep, sir, '
                                                                                                                                   'but I seem to '
                                                                                                                                   'be lost.',
                      'I\'m currently on a mission to travel the world, and the city of North Mitrovica is my next stop.',
                      'I was hoping you could help me.', 'Old man:\nWe don\'t see many people like you every day.', 'Old man:\nWell you are one '
                                                                                                                    'lucky traveller. This is a map '
                                                                                                                    'of the city,', 'Old man:\nand '
                                                                                                                                    'those marks in '
                                                                                                                                    'it are the '
                                                                                                                                    'places you need '
                                                                                                                                    'to go to find '
                                                                                                                                    'the knowledge '
                                                                                                                                    'you seek.',
                      'Old man:\nHowever it\'s not that simple. In every place you go,', 'Old man:\nyou will be met with challenges you must '
                                                                                         'overcome.', 'What do you mean by challenges, sir?',
                      'Old man:\nYour desire to move forward will be questioned.', 'Thank you very much, sir, I will keep that in mind.',
                      'Old man:\nGood luck traveller. Now let me sleep in peace.']

old_man_diag = ['Huh? Oh it\'s you again.', 'Just don\'t forget the map I gave ya, and you\'ll be fine.', 'Go now, let me rest in peace.']

rock_school_diag_intro = ['Kid:\nOh, hey there, stranger!', 'Kid:\nAre you here to listen to our concert later tonight?',
                          'Kid:\nThey\'ve gotten quite popular recently.', 'Kid:\nI\'m glad our school is growing! It kind of reminds me of the '
                                                                           'city\'s jazz age.', 'Kid:\nMaybe music will unite us again, '
                                                                                                'just like back then...']

rock_school_diag = ['Kid:\nOh, hi!', 'Kid:\nDon\'t forget to attend our concert later.']


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        time_now = pygame.time.get_ticks()
        finish_time = time_now + 3000

        wrap_text(surface, pixel_font, line, (130, 530), text_color, bg_color)

        while time_now < finish_time:
            pass
            time_now = pygame.time.get_ticks()
