import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.position = self.random_position()

    def random_position(self):
        return (random.randint(0, SCREEN_WIDTH - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE,
                random.randint(0, SCREEN_HEIGHT - SNAKE_SIZE) // SNAKE_SIZE * SNAKE_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(self.position[0], self.position[1], SNAKE_SIZE, SNAKE_SIZE))
