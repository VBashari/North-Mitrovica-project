import os
import random
import sys
import pygame
from graphics_display import window_size, LIGHT_GREEN, DARK_GREEN

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
gray = (128, 128, 128)

bg = pygame.transform.scale(pygame.image.load(os.path.join("Assets/Graphics", "word_search bg.png")).convert_alpha(), window_size)
turn = 0
board = [[" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " "]]

fps = 60
timer = pygame.time.Clock()
huge_font = pygame.font.Font("Assets/Grand9K Pixel.ttf", 40)

Word = ["cradle"]
secret_word = Word[random.randint(0, len(Word) - 1)]


def draw_board(screen):
    global turn
    global board
    for col in range(0, 6):
        for fam in range(0, 6):
            pygame.draw.rect(screen, DARK_GREEN, [col * 100 + 12, fam * 100 + 12, 75, 75], 3, 5)
            piece_text = huge_font.render(board[fam][col], True, LIGHT_GREEN)
            screen.blit(piece_text, (col * 100 + 30, fam * 100 + 25))
    pygame.draw.rect(screen, green, [5, turn * 100 + 5, window_size[0] - 10, 90], 3, 5)


def check_words(screen):
    global turn
    global board
    global secret_word
    for col in range(0, 6):
        for fam in range(0, 6):
            if secret_word[col] == board[fam][col] and turn > fam:
                pygame.draw.rect(screen, green, [col * 100 + 12, fam * 100 + 12, 75, 75], 0, 5)
            elif board[fam][col] in secret_word and turn > fam:
                pygame.draw.rect(screen, yellow, [col * 100 + 12, fam * 100 + 12, 75, 75], 0, 5)


def word_search_puzzle(screen):
    global board, turn, secret_word
    game_over = False
    letters = 0
    turn_active = True

    running = True

    while running:
        timer.tick(fps)
        screen.blit(bg, (0, 0))
        check_words(screen)
        draw_board(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # add player controls for letter entry, backspacing, checking guesses and restarting
            if event.type == pygame.TEXTINPUT and turn_active and not game_over:
                entry = event.__getattribute__('text')
                if entry != " " and turn_active:
                    entry = entry.lower()
                    board[turn][letters] = entry
                    letters += 1

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE and letters > 0:
                    board[turn][letters - 1] = ' '
                    letters -= 1
                if event.key == pygame.K_SPACE:
                    guess = board[turn][0] + board[turn][1] + board[turn][2] + board[turn][3] + board[turn][4] + board[turn][5]
                    if guess == secret_word:
                        game_over = True
                        running = False
                        break

                    turn += 1
                    letters = 0

            # control turn active based on letters
            if letters < 6:
                turn_active = True
            else:
                turn_active = False

            if turn == 6:
                turn = 0
                letters = 0
                board = [[" ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " "],
                         [" ", " ", " ", " ", " ", " "]]

        pygame.display.update()
