import pygame
from settings import *

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = pygame.K_RIGHT
        self.grow = False

    def update(self):
        # Передвижение змейки
        head_x, head_y = self.body[0]

        if self.direction == pygame.K_RIGHT:
            new_head = (head_x + SNAKE_SIZE, head_y)
        elif self.direction == pygame.K_LEFT:
            new_head = (head_x - SNAKE_SIZE, head_y)
        elif self.direction == pygame.K_UP:
            new_head = (head_x, head_y - SNAKE_SIZE)
        elif self.direction == pygame.K_DOWN:
            new_head = (head_x, head_y + SNAKE_SIZE)

        # Проверяем выход за границы экрана и телепортируем на другую сторону
        new_head = (
            new_head[0] % SCREEN_WIDTH,
            new_head[1] % SCREEN_HEIGHT
        )

        self.body = [new_head] + self.body[:-1]

        if self.grow:
            self.body.append(self.body[-1])
            self.grow = False

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    def change_direction(self, direction):
        # Предотвращаем возможность двигаться в противоположном направлении
        if direction == pygame.K_RIGHT and self.direction != pygame.K_LEFT:
            self.direction = pygame.K_RIGHT
        elif direction == pygame.K_LEFT and self.direction != pygame.K_RIGHT:
            self.direction = pygame.K_LEFT
        elif direction == pygame.K_UP and self.direction != pygame.K_DOWN:
            self.direction = pygame.K_UP
        elif direction == pygame.K_DOWN and self.direction != pygame.K_UP:
            self.direction = pygame.K_DOWN

    def grow_snake(self):
        self.grow = True
