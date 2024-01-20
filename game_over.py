import pygame
import os
import sys


class PicAppear(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PicAppear.load_image('pic/bg_end.png')
        self.rect = self.image.get_rect(center=(100, 390))  # Измененные координаты центра
        self.speed = 200  # Скорость в пикселях в секунду

    def update(self, dt):
        pixels_to_move = self.speed * dt / 1000  # Переводим скорость в пикселях за кадр
        if self.rect.right < 1200:  # Проверка, чтобы не выйти за правый край
            self.rect.x += pixels_to_move

    @staticmethod
    def load_image(name, size=None, colorkey=-1):
        fullname = os.path.join(name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)

        if size is not None:
            image = pygame.transform.scale(image, size)
        return image


class ResultButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pic/btn.PNG')
        self.rect = self.image.get_rect(center=(600, 550))
        self.font = pygame.font.Font(None, 36)
        self.text = '0-0'
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        # self.text_rect = self.rendered_text.get_rect(self.rect.center)

    def update_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.rendered_text.get_rect(center=1500)


def end():
    pygame.init()
    all_sprites = pygame.sprite.Group()
    car = PicAppear()
    result_button = ResultButton()
    all_sprites.add(car, result_button)

    pygame.init()
    screen = pygame.display.set_mode((1200, 700))
    pygame.display.set_caption("Game over")

    clock = pygame.time.Clock()
    dt = 0  # Инициализация прошедшего времени

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        dt = clock.tick(60)  # Получаем прошедшее время с момента последнего вызова
        all_sprites.update(dt)

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
