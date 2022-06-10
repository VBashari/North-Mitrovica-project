import pygame
from graphics_display import window_size, Image, SQUARE_SCALE

VEL = 5


class Player(Image):
    def __init__(self, x_pos, y_pos):
        super().__init__("person1.png", SQUARE_SCALE)

        self.rect.x = x_pos
        self.rect.y = y_pos

    def update(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_a] and self.rect.x > 0:
            self.rect.move_ip(-VEL, 0)
        if key_pressed[pygame.K_d] and self.rect.x + self.img.get_width() + VEL < window_size[0]:
            self.rect.move_ip(VEL, 0)
        if key_pressed[pygame.K_w] and self.rect.y > 0:
            self.rect.move_ip(0, -VEL)
        if key_pressed[pygame.K_s] and self.rect.y + self.img.get_height() + VEL < window_size[1]:
            self.rect.move_ip(0, VEL)

        self.draw(self.rect)
