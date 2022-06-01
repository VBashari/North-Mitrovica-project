import pygame
import graphics_display as graph_d

loco1 = graph_d.sign1.get_rect()
print(loco1.left)


def travel_map():

    while True:
        graph_d.map_display()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if graph_d.sign1.rect.width + graph_d.sign1 > mouse_pos[0] && ().collidepoint(mouse_pos):
                    print("but1")

                if graph_d.sign2.get_rect().collidepoint(mouse_pos):
                    print("but2")

                if graph_d.sign3.get_rect().collidepoint(mouse_pos):
                    print("but3")

                if graph_d.sign4.get_rect().collidepoint(mouse_pos):
                    print("but4")
