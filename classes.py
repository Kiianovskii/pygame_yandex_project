
# imports
import sys

import pygame
import pygame_gui
from functions import *
from time import time
from result import PicAppear


# game class
class Game:
    def __init__(self, win_balls=100, enemy_health=100, hero_health=100):
        manager = pygame_gui.UIManager(WINDOW_SIZE)
        hero = Hero(100, 410, hero_health, win_balls)
        enemy = Enemy(700, 410, enemy_speed, enemy_health)
        pygame.display.set_caption('Game')
        draw_bg()
        hero.draw(screen, enemy)
        enemy.draw(screen, hero)
        show_health_bar(hero.health, 50)
        show_health_bar(enemy.health, 700)

        # Добавьте атрибуты для отслеживания состояния игры
        self.win_condition = False
        self.lose_condition = False
        while not (self.win_condition or self.lose_condition):
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
        if self.win_condition:
            PicAppear() 


# hero class
class Hero(pygame.sprite.Sprite):
    def __init__(self, x, y, hearth, win_balls):
        self.is_dead = False
        self.win = False
        self.health = hearth
        image = None
        self.image = image
        self.win_balls = win_balls

        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y, 70, 80))

        self.speed = 10

        self.vx = 0
        self.vy = 0

        self.gravity = 2

        self.attacking = False

        self.start_attacking = time()

        self.score = 0
        # алинина часть кода с анимацией
        self.animation_frames = [load_image(f"pic/hero/hero_walk/hero_walk_{i}.png") for i in range(8)]
        self.frame_index = 0
        self.image = self.animation_frames[self.frame_index]
        self.rect = self.image.get_rect()

    # update func
    def draw(self, surface, target):
        # get pressed
        key = pygame.key.get_pressed()

        # check the fighter is not attacking
        if not self.attacking and self.health > 0:
            # check move
            if key[pygame.K_a]:
                # draw_bg()
                self.l_move()
            if key[pygame.K_d]:
                # draw_bg()
                self.r_move()
            if key[pygame.K_SPACE]:
                pass

            # check attack
            if key[pygame.K_e]:
                # draw_bg()
                self.r_attack(target)
            if key[pygame.K_q]:
                # draw_bg()
                self.l_attack(target)
        elif not self.win and target.health <= 0:
            self.win = True
            self.score += 1
            print(target.score)

        # print(target.health)

        # check out of screen
        if self.rect.left + self.vx < 0:
            self.vx = 0
        if self.rect.right + self.vx > WINDOW_WIDHT:
            self.vx = 0

        # change coords
        self.x += self.vx
        self.y += self.vy

        # movw rect
        self.rect = pygame.Rect((self.x, self.y, 100, 200))

        # stop move
        self.vx = 0
        self.vy = 0

        # draw
        draw_bg()

        # show hero health bar and score
        show_health_bar(self.health, 50)
        show_text(self.score, font, 30)

        # show enemy health bar and score
        show_health_bar(target.health, 700)
        show_text(target.score, font, 730)


# pygame.draw.rect(surface, (255, 255, 255), self.rect)

        # change attacking parameter
        now = time()
        if now - self.start_attacking >= 2:
            self.attacking = False

        surface.blit(self.image, self.rect.topleft)  # Draw hero image

        # Update animation frame
        self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
        self.image = self.animation_frames[self.frame_index]

        # Проверка на победу
        if target.health <= 0:
            win(self.win_balls)
            self.win_condition = True

    # move left func
    def l_move(self):
        self.vx = -self.speed
        # алинин код
        self.image = pygame.transform.flip(self.animation_frames[self.frame_index], True, False)

    # move right func
    def r_move(self):
        self.vx = self.speed
        # pygame.display.flip()

    # jump func
    def jump(self):
        # draw_bg()
        self.vy += self.gravity
        self.vy = -self.speed * 2
        # for i in range(25):
        #     self.y -= 2
        #     self.draw(screen)
        #     clock.tick(100)
        #     # screen.fill('white')
        # for i in range(25):
        #     self.y += 2
        #     self.draw(screen)
        #     # screen.fill('white')
        #     clock.tick(100)

    # stop move func
    def stop_move(self, target):
        self.vx = 0
        self.vy = 0
        self.draw(screen, target)
        pygame.display.flip()

    # left attack func
    def r_attack(self, target):
        if not self.attacking:
            self.attacking = True
            self.start_attacing = time()
            r_attack_rect = pygame.Rect(self.rect.centerx, self.rect.y,
                                        self.rect.width * 1.5, self.rect.height)
            pygame.draw.rect(screen, (255, 0, 0), r_attack_rect)
            pygame.display.flip()
            if r_attack_rect.colliderect(target.rect):
                target.health -= 1
            if target.health <= 0:
                win(self.win_balls)

    # right attack func
    def l_attack(self, target):
        if not self.attacking:
            self.attacking = True
            self.start_attacking = time()
            l_attack_rect = pygame.Rect(self.rect.centerx - 150,
                                        self.rect.y, self.rect.width * 1.5,
                                        self.rect.height)
            pygame.draw.rect(screen, (255, 0, 0), l_attack_rect)
            pygame.display.flip()

            if l_attack_rect.colliderect(target.rect):
                target.health -= 1

            if target.health <= 0:
                win(self.win_balls)


# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, hearth):
        self.win = False

        # fighter health
        self.health = hearth

        # load image
        image = None

        # Sprite constructor
        # super().init(*group)

        # set image
        self.image = image

        # set coords
        self.x = x
        self.y = y

        # set rect
        self.rect = pygame.Rect((self.x, self.y, 70, 80))

        # move speed
        self.speed = speed

        # speed of coord changing
        self.vx = 0
        self.vy = 0

        # set gravity
        self.gravity = 2

        # set start attacking
        self.start_attacking = time()

        # is fighter attacking now
        self.attacking = False

        # set score counter
        self.score = 0
        # алинина часть кода с анимацией
        self.animation_frames = [load_image(f"pic/enemy/enemy_walk/enemy_walk_{i}.png") for i in range(8)]
        self.frame_index = 0
        self.image = self.animation_frames[self.frame_index]
        self.rect = self.image.get_rect()


    def draw(self, surface, target):
            # draw enemy
            # pygame.draw.rect(surface, (0, 0, 0), self.rect)
            # enemy movement
            if self.health > 0:
                if not self.attacking:
                    if target.rect.centerx > self.rect.centerx:
                        if abs(target.rect.centerx - self.rect.centerx) > 150:
                            self.r_move()
                        else:
                            self.r_attack(target)
                    else:
                        if abs(self.rect.centerx - target.rect.centerx) > 150:
                            self.l_move()
                        else:
                            self.l_attack(target)
                else:
                    if target.rect.centerx > self.rect.centerx:
                        self.l_move()
                    else:
                        self.r_move()
            elif not self.win:
                self.win = True
                self.score += 1
                print(target.score)

            # check out of screen
            if self.rect.left + self.vx < 0:
                self.vx = 0
            if self.rect.right + self.vx > WINDOW_WIDHT:
                self.vx = 0
            # change coords
            self.x += self.vx
            self.y += self.vy
            # movw rect
            self.rect = pygame.Rect((self.x, self.y, 100, 200))
            # stop move
            self.vx = 0
            self.vy = 0
            # draw
            # draw_bg()
            # pygame.draw.rect(surface, (0, 0, 0), self.rect)
            # change attacking parameter
            now = time()
            if now - self.start_attacking >= 1:
                self.attacking = False
            # update(self, target)
            pygame.display.flip()
            surface.blit(self.image, self.rect.topleft)  # Draw enemy image

            # АЛинина часть кода с аниамцией
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.frame_index]

    # move left func
    def l_move(self):
        self.vx = -self.speed
        # Алинина часть кода с аниамцией
        self.image = pygame.transform.flip(self.animation_frames[self.frame_index], True, False)

    # move right func
    def r_move(self):
        self.vx = self.speed
        # pygame.display.flip()

    # jump func
    def jump(self):
        # draw_bg()
        self.vy += self.gravity
        self.vy = -self.speed * 2
        # for i in range(25):
        #     self.y -= 2
        #     self.draw(screen)
        #     clock.tick(100)
        #     # screen.fill('white')
        # for i in range(25):
        #     self.y += 2
        #     self.draw(screen)
        #     # screen.fill('white')
        #     clock.tick(100)

    # stop move func
    def stop_move(self, target):
        self.vx = 0
        self.vy = 0
        self.draw(screen, target)
        pygame.display.flip()

    # left attack func
    def r_attack(self, target):
        self.start_attacking = time()
        self.attacking = True
        r_attack_rect = pygame.Rect(self.rect.centerx, self.rect.y,
                                    self.rect.width * 1.5, self.rect.height)
        pygame.draw.rect(screen, (255, 0, 0), r_attack_rect)
        pygame.display.flip()
        if r_attack_rect.colliderect(target.rect):
            target.health -= 10
        if target.health <= 0:
            lose()

    # right attack func
    def l_attack(self, target):
        self.start_attacking = time()
        self.attacking = True
        l_attack_rect = pygame.Rect(self.rect.centerx - 150,
                                    self.rect.y, self.rect.width * 1.5,
                                    self.rect.height)
        pygame.draw.rect(screen, (255, 0, 0), l_attack_rect)
        pygame.display.flip()
        if l_attack_rect.colliderect(target.rect):
            target.health -= 10
        if target.health <= 0:
            lose()


# border class
class Border(pygame.sprite.Sprite):
    # init func
    def init(self, x1, y1, x2, y2):
        super().__init__(all_sprites)
        # vertical border
        if x1 == x2:
            self.add(vertical_borders)
            self.image = pygame.Surface([1, y2 - y1])
            self.rect = pygame.Rect(x1, y1, 1, y2 - y1)
        # horizontal border
        else:
            self.add(horizontal_borders)
            self.image = pygame.Surface([x2 - x1, 1])
            self.rect = pygame.Rect(x1, y1, x2 - x1, 1)