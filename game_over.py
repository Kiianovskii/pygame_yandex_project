import pygame
import os
import sys


class PicAppear(pygame.sprite.Sprite):
    # Здесь выдвигается окно, то есть класс представляет спрайт (графический объект), который будет двигаться по экрану.
    def __init__(self):
        super().__init__()
        self.image = PicAppear.load_image('pic/bg_end.png')
        self.rect = self.image.get_rect(center=(100, 390))  # Измененные координаты центра
        self.speed = 200  # Скорость в пикселях в секунду

    # update обновляет положение спрайта на каждом кадре в зависимости от прошедшего времени (dt)
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
    # создает кнопку,чтоб перейти в следующее окно
    # Класс ResultButton создает объект кнопки с изображением и текстом.
    # изображение кнопки, его положение (rect), шрифт и текст.
    # Также создаются текст и прямоугольник для отображения
    # Метод update_text позволяет обновить текст на кнопке.
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('pic/btn.PNG')
        self.rect = self.image.get_rect(center=(600, 550))
        self.font = pygame.font.Font(None, 36)
        self.text = 'Закончить'
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def update_text(self, new_text):
        self.text = new_text
        self.rendered_text = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.rendered_text.get_rect(center=self.rect.center)

    def is_clicked(self):
        return end()


def end():
    pygame.init()
    all_sprites = pygame.sprite.Group()
    car = PicAppear()
    result_button = ResultButton()
    all_sprites.add(car, result_button)

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
        all_sprites.update(dt)  # Вызываем метод update для всех спрайтов

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
