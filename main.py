# imports
# import pygame
import pygame_gui
from functions import *
from classes import Hero, Enemy

# init manager
manager = pygame_gui.UIManager(WINDOW_SIZE)

# create hero object
hero = Hero(100, 410)

# create enemy object
enemy = Enemy(300, 410)

if __name__ == '__main__':
    # set window name
    pygame.display.set_caption('Game')

    # set screen color
    # screen.fill('white')

    # hero.draw(screen)
    # create enemy object
    # enemy = Enemy

    # drow bg
    draw_bg()

    # show health bars
    print('ppp')
    show_health_bar(hero.health, 50, 50)
    show_health_bar(enemy.health, 500, 50)

    # draw hero
    hero.draw(screen, enemy)

    # draw enemy
    enemy.draw(screen, hero)

    # main loop
    running = True
    while running:
        # move fighters
        hero.draw(screen, enemy)
        enemy.draw(screen, hero)

        time_delta = clock.tick(FPS) / 1000.0
        all_sprites.draw(screen)
        for event in pygame.event.get():
            # screen.fill('white')
            # all_sprites.draw(screen)
            # all_sprites.update(event)
            # при закрытии окна
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.KEYDOWN:
                # if event.key == pygame.K_SPACE:
                #     hero.jump()
                # if event.key == pygame.K_a:
                #     print('a')
                #     # screen.fill('white')
                #     hero.l_move()
                # if event.key == pygame.K_d:
                #     print('d')
                #     # screen.fill('white')
                #     hero.r_move()

            manager.process_events(event)
            # hero.draw(screen)
            pygame.display.flip()

        manager.update(time_delta)
        manager.draw_ui(screen)
        all_sprites.draw(screen)

        # обновление экрана
        pygame.display.flip()
        clock.tick(FPS)
        # pygame.display.update()
    pygame.quit()

