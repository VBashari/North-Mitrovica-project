import pygame
import dialogues as diag
import graphics_display as graphs


def bridge_section(user):
    graphs.bridge_display()
    user.update()

    if user.rect.colliderect(graphs.old_man):
        diag.display_dialogue(graphs.window, diag.old_man_diag, graphs.GREEN, graphs.DARK_GREEN)
        user.rect.x += 50

    if user.rect.colliderect(graphs.shop):
        while True:
            key_pressed = pygame.key.get_pressed()
            shop_section(graphs.window)

            if key_pressed[pygame.K_ESCAPE]:
                user.rect.y += 50
                break

    pygame.display.update(user)


def shop_section(surface):
    graphs.shop_display()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            for item in graphs.shop_items:
                mouse_pos = event.pos

                if item.rect.collidepoint(mouse_pos):
                    diag.display_dialogue(surface, ['Not enough money'], graphs.GREEN, graphs.DARK_GREEN)


def rock_school_section(user):
    graphs.rock_school_display()
    user.update()

    if user.rect.colliderect(graphs.person_group):
        diag.display_dialogue(graphs.window, diag.rock_school_diag, graphs.GREEN, graphs.DARK_GREEN)
        user.rect.x += 50

    pygame.display.update(user)


def stadium_section(user):
    graphs.stadium_display()
    user.update()

    pygame.display.update(user)


def miners_section(user):
    graphs.miners_display()
    user.update()

    pygame.display.update(user)
