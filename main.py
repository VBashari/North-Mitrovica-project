import pygame
import graphics_display

pygame.display.set_caption("North Mitrovica")
clock = pygame.time.Clock()


def main():
    while True:
        clock.tick(40)
        graphics_display.bridge_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":
    main()
