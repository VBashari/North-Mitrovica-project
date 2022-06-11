import pygame
from graphics_display import LIGHT_GREEN, GREEN, DARK_GREEN


def sudoku(surface):
    surface.fill(LIGHT_GREEN)

    for i in range(20):
        pygame.draw.line(surface, DARK_GREEN, (50 + 50 * i, 50), (50 + 50*i, 650), 2)
        pygame.draw.line(surface, DARK_GREEN, (50, 50 + 50 * i), (650, 50 + 50 * i), 2)

    pygame.display.update()
