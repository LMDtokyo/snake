import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT  # Импортируем размеры экрана

# Уровни и их конфигурации
class Level:
    def __init__(self, number, next_level_score, obstacles=None):
        self.number = number
        self.next_level_score = next_level_score  # Количество очков для перехода на следующий уровень
        self.obstacles = obstacles or []  # Препятствия для текущего уровня

        # Загрузка фонового изображения для уровня
        background_image = pygame.image.load(f"../assets/images/level_{self.number}.jpg").convert()

        # Масштабируем изображение под размер окна
        self.background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def create_obstacles(self):
        if self.number == 1:
            # Нет препятствий на первом уровне
            self.obstacles = []
        elif self.number == 2:
            # Препятствия для второго уровня
            self.obstacles = [
                pygame.Rect(200, 150, 100, 20),
                pygame.Rect(400, 300, 100, 20),
                pygame.Rect(600, 450, 100, 20)
            ]
        elif self.number == 3:
            # Препятствия для третьего уровня
            self.obstacles = [
                pygame.Rect(150, 150, 100, 20),
                pygame.Rect(450, 250, 20, 150),
                pygame.Rect(300, 450, 150, 20),
                pygame.Rect(600, 350, 20, 150)
            ]
        elif self.number == 4:
            # Препятствия для четвертого уровня
            self.obstacles = [
                pygame.Rect(100, 100, 100, 20),
                pygame.Rect(300, 200, 20, 150),
                pygame.Rect(500, 400, 150, 20),
                pygame.Rect(700, 300, 20, 150),
                pygame.Rect(400, 100, 100, 20)
            ]
        elif self.number == 5:
            # Препятствия для пятого уровня
            self.obstacles = [
                pygame.Rect(100, 100, 100, 20),
                pygame.Rect(300, 200, 20, 150),
                pygame.Rect(500, 400, 150, 20),
                pygame.Rect(700, 300, 20, 150),
                pygame.Rect(400, 100, 100, 20),
                pygame.Rect(200, 500, 150, 20)
            ]

    def draw_background(self, screen):
        screen.blit(self.background_image, (0, 0))

    def draw_obstacles(self, screen):
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (139, 69, 19), obstacle)  # Коричневый цвет для препятствий
