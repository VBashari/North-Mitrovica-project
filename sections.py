import pygame
import dialogues as diag
import graphics_display as graphs


def shop_section(surface):
    graphs.shop_display()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in graphs.shop_items:
                mouse_pos = event.pos

                if item.rect.collidepoint(mouse_pos):
                    diag.display_dialogue(surface, ['Not enough money'], graphs.GREEN, graphs.DARK_GREEN)

    pygame.display.update()
