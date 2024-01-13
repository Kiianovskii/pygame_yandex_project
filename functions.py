# imports
import os
import sys
import pygame


# (
#     bg_image,
#     WINDOW_SIZE,
#     WINDOW_HEIGHT,
#     WINDOW_WIDHT,
#     screen,
#     clock,
#     FPS
# )


# from classes import (
#     Enemy,
#     Hero,
#     Border
# )

# drow bg
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, WINDOW_SIZE)
    bg_coords = (0, 0)
    screen.blit(scaled_bg, bg_coords)


# quit func
def terminate():
    pygame.quit()
    sys.exit()


# show health bar func
def show_health_bar(health, x, y):
    part_of_health = health / 100
    pygame.draw.rect(screen, (0, 0, 255), (x, y, 100, 50))
    pygame.draw.rect(screen, (0, 255, 0),
                     (x, y, 100 * part_of_health, 50))



# image load func
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# show start screen func
def start_screen():
    intro_text = ["ЗАСТАВКА", "",
                  "Правила игры",
                  "Если в правилах несколько строк,",
                  "приходится выводить их построчно"]

    fon = pygame.transform.scale(load_image('fon.jpg'), (WINDOW_WIDHT, WINDOW_HEIGHT))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


# init
pygame.init()

# set size
WINDOW_SIZE = WINDOW_WIDHT, WINDOW_HEIGHT = 1200, 700

# set FPS
FPS = 60

# make sprite group
all_sprites = pygame.sprite.Group()

# set horizontal borders
horizontal_borders = pygame.sprite.Group()

# set vertical borders
vertical_borders = pygame.sprite.Group()

# init clock
clock = pygame.time.Clock()

# create screen
screen = pygame.display.set_mode(WINDOW_SIZE)

# bg image
bg_image = pygame.image.load('bg.jpg').convert_alpha()

#
# background = pygame.Surface(WINDOW_SIZE)
#
# #
# color = 'white'
#
# #
# background.fill(color)
