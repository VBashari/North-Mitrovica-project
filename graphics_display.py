import pygame
import os.path
import random

SQUARE_SCALE = (50, 50)
GREEN = (224, 248, 207)

# ---
# window
# ---
window_size = (700, 700)
window = pygame.display.set_mode(window_size)

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
        window.blit(grass, (grass_position[i], grass_position[i-1]))


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
# Xhafer Deva house
# ---
deva_house = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "building2.png")), (200, 330))
car = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "car.png")), (120, 80))
road_frame = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "road frame.png")), (90, 20))


def deva_house_display():
    window.fill(GREEN)

    for i in range(9):
        for j in range(10):
            window.blit(grass, (i * SQUARE_SCALE[0], j * SQUARE_SCALE[0]))

    for i in range(5):
        window.blit(road_frame, (i * road_frame.get_width(), window_size[0] / 3 * 2.1))

    for i in range(6):
        window.blit(pygame.transform.rotate(road_frame, 90),
                    (window_size[0] / 3 * 1.9, i * road_frame.get_width() - 30))

    window.blit(deva_house, (100, 60))
    window.blit(person_2, (person_1.get_width() * 7, person_1.get_height() * 8.2))

    window.blit(car, (window_size[0] - car.get_width() * 2 - 30, window_size[0] - car.get_height() - 10))
    window.blit(car, (window_size[0] - car.get_width() - 10, window_size[0] - car.get_height() - 10))

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
