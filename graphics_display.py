import pygame
import os
import random

pygame.init()

SQUARE_SCALE = (50, 50)
BUTTON_SCALE = (100, 50)

GREEN = (224, 248, 207)
DARK_GREEN = (48, 104, 80)
LIGHT_GREEN = (224, 248, 207)

# ---
# Window
# ---
window_size = (700, 700)
window = pygame.display.set_mode(window_size)


# ---
# Global assets
# ---

class Image(pygame.sprite.Sprite):
    def __init__(self, file, dimensions):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("Assets", file)).convert_alpha(), dimensions)
        self.rect = self.img.get_rect()

    def draw(self, position):
        self.rect.x = position[0]
        self.rect.y = position[1]
        window.blit(self.img, self.rect)


person_1 = Image("person2.png", SQUARE_SCALE)
person_2 = Image("person4.png", SQUARE_SCALE)
person_3 = Image("person5.png", SQUARE_SCALE)

road = Image("road.png", SQUARE_SCALE)
grass = Image("grass.png", SQUARE_SCALE)
grass_position = [random.randrange(0, window_size[0], SQUARE_SCALE[0]) for position in range(30)]


def draw_grass():
    for i in range(len(grass_position)):
        grass.draw((grass_position[i], grass_position[i - 1]))


# ---
# Map
# ---

city_map = Image("map.png", (580, 460))
sign1 = Image("sign1.png", BUTTON_SCALE)
sign2 = Image("sign2.png", BUTTON_SCALE)
sign3 = Image("sign3.png", BUTTON_SCALE)
sign4 = Image("sign4.png", BUTTON_SCALE)


def map_display():
    window.fill(DARK_GREEN)
    pygame.draw.rect(window, GREEN, (50, 50, window_size[0] - 100, window_size[0] - 100))

    city_map.draw((60, 120))
    sign1.draw((sign1.img.get_width() * 4.5, sign1.img.get_width() * 4))
    sign2.draw((sign2.img.get_width() * 2.7, sign2.img.get_width() * 4.5))
    sign3.draw((sign3.img.get_width() * 1.1, sign3.img.get_width() * 5.2))
    sign4.draw((sign4.img.get_width() * 2.8, sign4.img.get_width() * 2.8))

    pygame.display.update()


# ---
# Bridge
# ---
water = Image("water.png", SQUARE_SCALE)

old_man = Image("person3.png", SQUARE_SCALE)
ground = Image("ground.png", SQUARE_SCALE)
shop = Image("building1.png", (144, 144))
back_bridge = Image("bridge1.png", (63, 27))
front_bridge = Image("bridge2.png", (63, 48))

bridge_collision = [old_man, shop, back_bridge, front_bridge]


def bridge_display():
    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(int(window_size[0] / SQUARE_SCALE[0])):
            water.draw((i * SQUARE_SCALE[0], j * SQUARE_SCALE[0]))

    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(5):
            ground.draw((i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 3))

    for i in range(12):
        back_bridge.draw((i * 63 - 30, window_size[0] / 3))
        front_bridge.draw((i * 63 - 30, window_size[0] / 3 * 2))

    old_man.draw((SQUARE_SCALE[0], window_size[0] / 7 * 4))
    shop.draw((SQUARE_SCALE[0] * 3, window_size[0] / 3 - 10))

    pygame.display.update()


# ---
# Shop
# ---

clerk = Image("person2.png", (150, 180))
bag = Image("bag.png", (90, 90))
plate = Image("plate.png", (80, 80))
cifteli = Image("cifteli.png", (170, 80))
mini_miners = Image("mini_miners.png", (80, 80))
shop_table = Image("shop_table.png", (700, 200))
inside_wall = Image("inside_wall.png", (550, 440))

shop_items = [plate, bag, cifteli, mini_miners]

pygame.init()
pixel_font = pygame.font.Font("Grand9K Pixel.ttf", 20)
price1 = pixel_font.render(" 250 ", True, GREEN, DARK_GREEN)
price2 = pixel_font.render(" 300 ", True, GREEN, DARK_GREEN)
price3 = pixel_font.render(" 250 ", True, GREEN, DARK_GREEN)
price4 = pixel_font.render(" 160 ", True, GREEN, DARK_GREEN)


def shop_display():
    window.fill(DARK_GREEN)
    for i in range(2):
        inside_wall.draw((inside_wall.img.get_width() * i - 100, 0))

    clerk.draw((person_2.img.get_width() * 8.5, person_2.img.get_width() * 5.5))
    shop_table.draw((0, window_size[0] / 5 * 3))

    # items
    plate.draw((SQUARE_SCALE[0], SQUARE_SCALE[0] * 0.6))
    window.blit(price1, (price1.get_width() * 1.2, SQUARE_SCALE[0] * 2.5))

    plate.draw((SQUARE_SCALE[0] * 4.5, SQUARE_SCALE[0] * 0.7))
    window.blit(price1, (price1.get_width() * 4.3, SQUARE_SCALE[0] * 2.5))

    cifteli.draw((cifteli.img.get_width() * 0.7, cifteli.img.get_width()))
    window.blit(price2, (price2.get_width() * 3.2, SQUARE_SCALE[0] * 5))

    bag.draw((bag.img.get_width() * 0.5, bag.img.get_width() * 3.1))
    window.blit(price3, (price3.get_width() * 1.2, SQUARE_SCALE[0] * 7.5))

    mini_miners.draw((mini_miners.img.get_width() * 3, mini_miners.img.get_width() * 3.6))
    window.blit(price4, (price4.get_width() * 5.4, SQUARE_SCALE[0] * 7.5))

    pygame.display.update()


# ---
# School of Rock
# ---
jukebox = Image("jukebox.png", (50, 60))
guitar = Image("guitar.png", (72, 36))
stage = Image("stage.png", (471, 150))
person_group = Image("person_group.png", (124, 100))


def rock_school_display():
    window.fill(GREEN)
    draw_grass()

    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(5):
            road.draw((i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 2))

    # stage
    stage.draw((window_size[0] - stage.img.get_width(), window_size[0] / 3 * 1.1))
    jukebox.draw((jukebox.img.get_width() * 5, window_size[0] / 3))
    jukebox.draw((jukebox.img.get_width() * 11, window_size[0] / 3 + 30))
    guitar.draw((guitar.img.get_width() * 6, window_size[0] / 2.5))
    guitar.draw((guitar.img.get_width() * 9, window_size[0] / 3 + 70))
    person_2.draw((person_2.img.get_width() * 7, window_size[0] / 3 + 55))

    person_group.draw((window_size[0] / 5, window_size[1] / 4 * 2.3))

    pygame.display.update()


# ---
# Football stadium
# ---
ticket_booth = Image("ticket booth.png", (window_size[0], 400))
gate = Image("gate.png", (90, 45))


def stadium_display():
    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(int(window_size[0] / SQUARE_SCALE[0])):
            road.draw((i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 2))

    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(int(window_size[0] / SQUARE_SCALE[0])):
            grass.draw((i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 6 * 5.1))

    ticket_booth.draw((0, 0))
    person_2.draw((person_2.img.get_width() * 2, window_size[0] / 3 * 2))

    for i in range(int(window_size[0] / gate.img.get_width()) + 1):
        gate.draw((i * gate.img.get_width(), window_size[0] / 6 * 4.8))

    pygame.display.update()


# ---
# Miner's monument
# ---
monument = Image("monument.png", (301, 269))
plaque = Image("plaque.png", SQUARE_SCALE)


def miners_display():
    window.fill(GREEN)
    draw_grass()

    for i in range(2):
        for j in range(2):
            road.draw((i * SQUARE_SCALE[0] + SQUARE_SCALE[0] * 8, window_size[0] / 1.9 + j * SQUARE_SCALE[0]))

    for i in range(4):
        for j in range(5):
            road.draw((i * SQUARE_SCALE[0] + SQUARE_SCALE[0] * 7, window_size[0] / 1.5 + j * SQUARE_SCALE[0]))

    monument.draw((window_size[0] - monument.img.get_width() - 100, 100))

    plaque.draw((plaque.img.get_width() * 2, plaque.img.get_width() * 9.6))
    person_3.draw((person_3.img.get_width() * 3.2, person_3.img.get_width() * 9.5))

    pygame.display.update()
