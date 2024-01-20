# imports
import pygame
from functions import *
from open_menu import MainMenu


if __name__ == '__main__':
    main_w = MainMenu()
    main_w.run()
    pygame.quit()
    sys.exit()
