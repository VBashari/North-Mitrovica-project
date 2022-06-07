import sys
import pygame
import graphics_display as graphs
from player_class import Player

pygame.display.set_caption("North Mitrovica")
clock = pygame.time.Clock()
FPS = 30

user = Player(600, 350)

# class Scene_Manager():


def main():
    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        graphs.bridge_display()

        user.update(graphs.bridge_collision)

        user.draw(user.rect)
        pygame.display.update()


if __name__ == "__main__":
    main()
