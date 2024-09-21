import pygame
from settings import *

class Menu:
    def __init__(self, screen, high_score=0, last_score=0):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 40)
        self.title = self.font.render("Змейка", True, (255, 255, 255))

        self.high_score = high_score
        self.last_score = last_score

        # Загрузка фонового изображения для меню
        background_image = pygame.image.load("../assets/images/menu_background.jpg").convert()

        # Масштабируем изображение под размер окна
        self.background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Увеличим размеры кнопок
        self.start_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2, 300, 50)
        self.exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 + 70, 300, 50)

    def draw(self):
        # Отображаем фоновое изображение
        self.screen.blit(self.background_image, (0, 0))

        # Заголовок
        self.screen.blit(self.title, (SCREEN_WIDTH // 2 - self.title.get_width() // 2, 100))

        # Кнопка "Начать игру"
        pygame.draw.rect(self.screen, (0, 255, 0), self.start_button)
        start_text = self.font.render("Начать игру", True, (0, 0, 0))
        self.screen.blit(start_text, (self.start_button.x + (self.start_button.width - start_text.get_width()) // 2, self.start_button.y + 10))

        # Кнопка "Выход"
        pygame.draw.rect(self.screen, (255, 0, 0), self.exit_button)
        exit_text = self.font.render("Выход", True, (0, 0, 0))
        self.screen.blit(exit_text, (self.exit_button.x + (self.exit_button.width - exit_text.get_width()) // 2, self.exit_button.y + 10))

        # Отображаем текущий счет и рекорд
        score_text = self.font.render(f"Ваш счет: {self.last_score}", True, (255, 255, 255))
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200))

        high_score_text = self.font.render(f"Рекорд: {self.high_score}", True, (255, 255, 255))
        self.screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, 250))

        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.start_button.collidepoint(event.pos):
                return 'start'
            elif self.exit_button.collidepoint(event.pos):
                return 'exit'
        return None
