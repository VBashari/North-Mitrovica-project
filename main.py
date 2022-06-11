import sys
import pygame
import sections as sect
from player_class import Player

pygame.display.set_caption("Traveller's Journey")

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

        sect.miners_section(user)


if __name__ == "__main__":
    main()
