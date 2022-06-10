import sys
import pygame
import graphics_display as graphs
import dialogues as diag
import sections
from player_class import Player

pygame.display.set_caption("North Mitrovica")
clock = pygame.time.Clock()
FPS = 60

user = Player(600, 350)


def main():
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        graphs.bridge_display()

        user.update()

        if user.rect.colliderect(graphs.old_man):
            diag.display_dialogue(graphs.window, diag.old_man_diag, graphs.GREEN, graphs.DARK_GREEN)
            user.rect.x += 50

        if user.rect.colliderect(graphs.shop):
            while True:
                key_pressed = pygame.key.get_pressed()
                sections.shop_section(graphs.window)

                if key_pressed[pygame.K_ESCAPE]:
                    user.rect.y += 50
                    break

        pygame.display.update()


if __name__ == "__main__":
    main()
