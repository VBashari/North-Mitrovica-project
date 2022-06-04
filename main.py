import pygame
import graphics_display
import city_map

pygame.display.set_caption("North Mitrovica")
clock = pygame.time.Clock()


def main():
    while True:
        clock.tick(40)
        #graphics_display.miners_display()
        city_map.travel_map()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()


if __name__ == "__main__":
    main()
