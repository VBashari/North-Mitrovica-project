import pygame
import os.path
import random

pygame.init()

SQUARE_SCALE = (50, 50)
BUTTON_SCALE = (100, 50)
GREEN = (224, 248, 207)
DARK_GREEN = (48, 104, 80)

# ---
# window
# ---
window_size = (700, 700)
window = pygame.display.set_mode(window_size)


class Image():
    def __init__(self,):

# ---
# global assets
# ---
player = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "person1.png")), SQUARE_SCALE)
person_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "person2.png")), SQUARE_SCALE)
person_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "person4.png")), SQUARE_SCALE)
person_3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "person5.png")), SQUARE_SCALE)

road = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "road.png")), SQUARE_SCALE)
grass = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "grass.png")), SQUARE_SCALE)
grass_position = [random.randrange(0, window_size[0], SQUARE_SCALE[0]) for position in range(30)]


def draw_grass():
    for i in range(len(grass_position)):
        window.blit(grass, (grass_position[i], grass_position[i - 1]))


# ---
# Map
# ---

city_map = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "map.png")), (580, 460))
sign1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "sign1.png")), BUTTON_SCALE)
sign2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "sign2.png")), BUTTON_SCALE)
sign3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "sign3.png")), BUTTON_SCALE)
sign4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "sign4.png")), BUTTON_SCALE)


def map_display():
    window.fill(DARK_GREEN)
    pygame.draw.rect(window, GREEN, (50, 50, window_size[0] - 100, window_size[0] - 100))

    window.blit(city_map, (60, 120))
    window.blit(sign1, (sign1.get_width() * 4.5, sign1.get_height() * 7.5))
    window.blit(sign2, (sign1.get_width() * 2.5, sign1.get_height() * 9.5))
    window.blit(sign3, (sign1.get_width(), sign1.get_height() * 10.5))
    window.blit(sign4, (sign1.get_width() * 2.8, sign1.get_height() * 5))

    pygame.display.update()


# ---
# Bridge
# ---
water_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "water 1.png")), SQUARE_SCALE)
water_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "water 2.png")), SQUARE_SCALE)
water_3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "water 3.png")), SQUARE_SCALE)
water_sprites = [water_1, water_2, water_3]

old_man = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "person3.png")), SQUARE_SCALE)
ground = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "ground.png")), SQUARE_SCALE)
shop = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "building1.png")), (144, 144))
back_bridge = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bridge1.png")), (63, 27))
front_bridge = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bridge2.png")), (63, 48))


def bridge_display():
    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(int(window_size[0] / SQUARE_SCALE[0])):
            window.blit(random.choice(water_sprites), (i * SQUARE_SCALE[0], j * SQUARE_SCALE[0]))

    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(5):
            window.blit(ground, (i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 3))

    for i in range(12):
        window.blit(back_bridge, (i * 63 - 30, window_size[0] / 3))
        window.blit(front_bridge, (i * 63 - 30, window_size[0] / 3 * 2))

    window.blit(old_man, (SQUARE_SCALE[0], window_size[0] / 7 * 4))
    window.blit(shop, (SQUARE_SCALE[0] * 3, window_size[0] / 3 - 10))

    pygame.display.update()


# ---
# Shop
# ---

bag = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "bag.png")), (90, 90))
plate = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "plate.png")), (80, 80))
cifteli = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "cifteli.png")), (170, 80))
mini_miners = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "mini_miners.png")), (80, 80))
shop_table = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "shop_table.png")), (700, 200))
inside_wall = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "inside_wall.png")), (400, 300))

pixel_font = pygame.font.Font("Grand9K Pixel.ttf", 20)
price1 = pixel_font.render(" 250 ", True, GREEN, DARK_GREEN)
price2 = pixel_font.render(" 300 ", True, GREEN, DARK_GREEN)
price3 = pixel_font.render(" 250 ", True, GREEN, DARK_GREEN)
price4 = pixel_font.render(" 160 ", True, GREEN, DARK_GREEN)


def shop_display():
    window.fill(DARK_GREEN)
    for i in range(2):
        for j in range(2):
            window.blit(inside_wall, (i * inside_wall.get_width(), j * inside_wall.get_height()))

    window.blit(pygame.transform.scale(person_2, (150, 150)), (person_2.get_width() * 8.5, person_2.get_height() * 6))
    window.blit(shop_table, (0, window_size[0] / 5 * 3))

    # items
    window.blit(plate, (SQUARE_SCALE[0], SQUARE_SCALE[0] * 0.6))
    window.blit(price1, (price1.get_width() * 1.2, SQUARE_SCALE[0] * 2.5))

    window.blit(plate, (SQUARE_SCALE[0] * 4.5, SQUARE_SCALE[0] * 0.7))
    window.blit(price1, (price1.get_width() * 4.3, SQUARE_SCALE[0] * 2.5))

    window.blit(cifteli, (cifteli.get_width() * 0.7, cifteli.get_height() * 2))
    window.blit(price2, (price2.get_width() * 3.2, SQUARE_SCALE[0] * 5))

    window.blit(bag, (bag.get_width() * 0.5, bag.get_height() * 3.1))
    window.blit(price3, (price3.get_width() * 1.2, SQUARE_SCALE[0] * 7.5))

    window.blit(mini_miners, (mini_miners.get_width() * 3, mini_miners.get_width() * 3.6))
    window.blit(price4, (price4.get_width() * 5.4, SQUARE_SCALE[0] * 7.5))

    pygame.display.update()


# ---
# School of Rock
# ---
jukebox = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "jukebox.png")), (50, 60))
guitar = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "guitar.png")), (72, 36))
stage = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "stage.png")), (471, 150))


def rock_school_display():
    window.fill(GREEN)
    draw_grass()

    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(5):
            window.blit(road, (i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 2))

    # stage
    window.blit(stage, (window_size[0] - stage.get_width(), window_size[0] / 3 * 1.1))
    window.blit(jukebox, (jukebox.get_width() * 5, window_size[0] / 3))
    window.blit(jukebox, (jukebox.get_width() * 11, window_size[0] / 3 + 30))
    window.blit(guitar, (guitar.get_width() * 6, window_size[0] / 2.5))
    window.blit(guitar, (guitar.get_width() * 9, window_size[0] / 3 + 70))
    window.blit(person_2, (person_1.get_width() * 7, window_size[0] / 3 + 55))

    # teen group
    window.blit(person_1, (person_1.get_width() * 3, window_size[0] / 2 + 30))
    window.blit(person_2, (person_1.get_width() * 2, window_size[0] / 2 + 55))
    window.blit(person_3, (person_1.get_width() * 3.7, window_size[0] / 2 + 70))

    pygame.display.update()


# ---
# Football stadium
# ---
ticket_booth = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "ticket booth.png")),
                                      (window_size[0], 400))
gate = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "gate.png")), (90, 45))


def stadium_display():
    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(int(window_size[0] / SQUARE_SCALE[0])):
            window.blit(road, (i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 2))

    for i in range(int(window_size[0] / SQUARE_SCALE[0])):
        for j in range(int(window_size[0] / SQUARE_SCALE[0])):
            window.blit(grass, (i * SQUARE_SCALE[0], j * SQUARE_SCALE[0] + window_size[0] / 6 * 5.1))

    window.blit(ticket_booth, (0, 0))
    window.blit(person_2, (person_2.get_width() * 2, window_size[0] / 3 * 2))

    for i in range(int(window_size[0] / gate.get_width()) + 1):
        window.blit(gate, (i * gate.get_width(), window_size[0] / 6 * 4.8))

    pygame.display.update()


# ---
# Miner's monument
# ---
monument = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "monument.png")), (301, 269))
plaque = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "plaque.png")), SQUARE_SCALE)


def miners_display():
    window.fill(GREEN)
    draw_grass()

    for i in range(2):
        for j in range(2):
            window.blit(road, (i * SQUARE_SCALE[0] + SQUARE_SCALE[0] * 8, window_size[0] / 1.9 + j * SQUARE_SCALE[0]))

    for i in range(4):
        for j in range(5):
            window.blit(road, (i * SQUARE_SCALE[0] + SQUARE_SCALE[0] * 7, window_size[0] / 1.5 + j * SQUARE_SCALE[0]))

    window.blit(monument, (window_size[0] - monument.get_width() - 100, 100))

    window.blit(plaque, (plaque.get_width() * 2, plaque.get_height() * 9.6))
    window.blit(person_3, (person_3.get_width() * 3.2, person_3.get_height() * 9.5))

    pygame.display.update()
