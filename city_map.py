import pygame
from graphics_display import sign1, sign2, sign3, sign4, map_display, bridge_display, rock_school_display, stadium_display, miners_display


def travel_map():

    while True:
        map_display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if sign1.rect.collidepoint(mouse_pos):
                    rock_school_display()

                if sign2.rect.collidepoint(mouse_pos):
                    bridge_display()

                if sign3.rect.collidepoint(mouse_pos):
                    stadium_display()

                if sign4.rect.collidepoint(mouse_pos):
                    miners_display()
