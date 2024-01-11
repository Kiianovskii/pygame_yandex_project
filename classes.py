# imports
import pygame

from functions import *


# hero class
class Hero(pygame.sprite.Sprite):
    # init func
    def __init__(self, x, y):
        # fighter health
        self.health = 100

        # load image
        image = pygame.image.load("hero.png")

        # Sprite constructor
        # super().__init__(*group)

        # set image
        self.image = image

        # set coords
        self.x = x
        self.y = y

        # set rect
        self.rect = pygame.Rect((self.x, self.y, 100, 200))

        # move speed
        self.speed = 10

        # speed of coord changing
        self.vx = 0
        self.vy = 0

        # set gravity
        self.gravity = 2

        # is fighter attacking now
        self.attacking = False

        # # make sprite
        # hero_sprite = pygame.sprite.Sprite()
        # # sprite view
        # hero_sprite.image = load_image(self.image)
        # # sprite size
        # hero_sprite.rect = hero_sprite.image.get_rect()
        # # add sprite to group
        # all_sprites.add(hero_sprite)

    # update func
    def draw(self, surface, target):
        # get pressed
        key = pygame.key.get_pressed()

        # check the fighter is not attacking
        if not self.attacking:
            # check move
            if key[pygame.K_a]:
                draw_bg()
                self.l_move()
            if key[pygame.K_d]:
                draw_bg()
                self.r_move()
            if key[pygame.K_SPACE]:
                pass
                # draw_bg()
                # self.jump()

            # check attack
            if key[pygame.K_e]:
                draw_bg()
                self.r_attack(target)
            if key[pygame.K_q]:
                draw_bg()
                self.l_attack(target)

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

        #
        self.vx = 0
        self.vy = 0

        # draw
        draw_bg()
        pygame.draw.rect(surface, (255, 255, 255), self.rect)

        # if pygame.sprite.spritecollideany(self, horizontal_borders):
        #     self.vy = -self.vy
        # if pygame.sprite.spritecollideany(self, vertical_borders):
        #     self.vx = 0

        self.attacking = False

        pygame.display.flip()

        # self.rect = self.rect.move(,
        #                            )
        # if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
        #         self.rect.collidepoint(args[0].pos):
        #     self.image = self.image_boom

    # move left func
    def l_move(self):
        self.vx = -self.speed
        # pygame.display.flip()

    # move right func
    def r_move(self):
        self.vx = self.speed
        # pygame.display.flip()

    # jump func
    def jump(self):
        draw_bg()
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
    def stop_move(self):
        self.vx = 0
        self.vy = 0
        self.draw(screen)
        pygame.display.flip()

    # left attack func
    def r_attack(self, target):
        self.attacking = True
        r_attack_rect = pygame.Rect(self.rect.centerx, self.rect.y,
                                         self.rect.width * 1.5, self.rect.height)
        pygame.draw.rect(screen, (255, 0, 0), r_attack_rect)
        pygame.display.flip()
        if r_attack_rect.colliderect(target.rect):
            target.health -= 10

    # right attack func
    def l_attack(self, target):
        self.attacking = True
        l_attack_rect = pygame.Rect(self.rect.centerx - 150,
                                         self.rect.y, self.rect.width * 1.5,
                                         self.rect.height)
        pygame.draw.rect(screen, (255, 0, 0), l_attack_rect)
        pygame.display.flip()
        if l_attack_rect.colliderect(target.rect):
            target.health -= 10


# enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        # fighter health
        self.health = 100

        # load image
        image = pygame.image.load("hero.png")

        # Sprite constructor
        # super().__init__(*group)

        # set image
        self.image = image

        # set coords
        self.x = x
        self.y = y

        # set rect
        self.rect = pygame.Rect((self.x, self.y, 100, 200))

        # move speed
        self.speed = 10

        # speed of coord changing
        self.vx = 0
        self.vy = 0

        # set gravity
        self.gravity = 2

        # is fighter attacking now
        self.attacking = False

    def draw(self, surface, target):
        pygame.draw.rect(surface, (0, 0, 0), self.rect)
    # # init func
    # def __init__(self, *group):
    #     # load image
    #     image = pygame.image.load("enemy.png")
    #     # Sprite constructor
    #     super().__init__(*group)
    #     self.image = image
    #     self.rect = self.image.get_rect()
    #     self.rect.x = 0
    #     self.rect.y = 0
    #     # make sprite
    #     enemy_sprite = pygame.sprite.Sprite()
    #     # sprite view
    #     enemy_sprite.image = load_image(self.image)
    #     # sprite size
    #     enemy_sprite.rect = enemy_sprite.image.get_rect()
    #     # add sprite to group
    #     all_sprites.add(enemy_sprite)


# border class
class Border(pygame.sprite.Sprite):
    # init func
    def __init__(self, x1, y1, x2, y2):
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
