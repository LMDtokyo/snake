import pygame
import sys
from settings import *
from snake import Snake
from food import Food
from menu import Menu
from levels import Level
import os

# Функция для корректной работы путей при использовании PyInstaller
def resource_path(relative_path):
    """ Получает путь к ресурсам при сборке в исполняемый файл """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# Инициализация Pygame
pygame.init()

# Окно игры
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Функция для отображения счета и уровня
def draw_score_and_level(screen, score, level):
    font = pygame.font.SysFont("Arial", 30)
    score_text = font.render(f"Счет: {score}", True, (255, 255, 255))
    level_text = font.render(f"Уровень: {level.number}", True, (255, 255, 255))
    screen.blit(score_text, (SCREEN_WIDTH - score_text.get_width() - 10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 50))

# Основной цикл игры
def main():
    clock = pygame.time.Clock()

    # Инициализация меню
    high_score = 0  # Рекорд
    menu = Menu(screen, high_score)

    # Состояния игры
    game_state = 'menu'  # 'menu', 'play', 'gameover'

    snake = None
    food = None
    score = 0  # Переменная для хранения счета
    level = Level(1, 45)  # Текущий уровень: первый уровень, 45 очков для перехода на следующий
    speed = FPS  # Начальная скорость

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if game_state == 'menu':
                action = menu.handle_event(event)
                if action == 'start':
                    # Начало новой игры
                    snake = Snake()
                    food = Food()
                    score = 0  # Обнуление счета
                    level = Level(1, 45)  # Начальный уровень
                    level.create_obstacles()  # Препятствий нет на первом уровне
                    speed = FPS  # Начальная скорость
                    game_state = 'play'
                elif action == 'exit':
                    running = False

            elif game_state == 'play':
                if event.type == pygame.KEYDOWN:
                    snake.change_direction(event.key)

            elif game_state == 'gameover':
                action = menu.handle_event(event)
                if action == 'start':
                    # Перезапуск игры после смерти
                    snake = Snake()  # Создаем новую змейку
                    food = Food()  # Создаем новую еду
                    score = 0  # Обнуление счета при новой игре
                    level = Level(1, 45)  # Начальный уровень
                    level.create_obstacles()  # Препятствий нет на первом уровне
                    speed = FPS  # Начальная скорость
                    game_state = 'play'  # Переключение в режим игры
                elif action == 'exit':
                    running = False

        if game_state == 'menu':
            menu.draw()

        elif game_state == 'play':
            # Логика игры
            snake.update()

            # Проверка на съедение еды
            if snake.body[0] == food.position:
                snake.grow_snake()
                food = Food()
                score += 1  # Увеличение счета на 1

                # Переход на следующий уровень при достижении нужного количества очков
                if score >= level.next_level_score:
                    level, snake = next_level(level, score, snake)
                    score = 0  # Сброс счета при переходе на новый уровень
                    speed += 5  # Увеличение скорости игры с каждым уровнем

            # Проверка на столкновение с телом змейки
            if snake.body[0] in snake.body[1:]:
                # Обновление рекорда, если текущий счет больше рекорда
                if score > high_score:
                    high_score = score
                game_state = 'gameover'
                menu.last_score = score  # Обновляем последний счет
                menu.high_score = high_score  # Обновляем рекорд

            # Проверка на столкновение с препятствиями (если есть)
            for obstacle in level.obstacles:
                if pygame.Rect(snake.body[0][0], snake.body[0][1], SNAKE_SIZE, SNAKE_SIZE).colliderect(obstacle):
                    game_state = 'gameover'
                    menu.last_score = score  # Обновляем последний счет
                    menu.high_score = high_score  # Обновляем рекорд

            # Отрисовка
            level.draw_background(screen)  # Отрисовка фона уровня
            snake.draw(screen)
            food.draw(screen)
            draw_score_and_level(screen, score, level)  # Отрисовка счета и уровня
            level.draw_obstacles(screen)  # Отрисовка препятствий для текущего уровня
            pygame.display.flip()

        elif game_state == 'gameover':
            # Показываем меню с результатами
            screen.fill(BG_COLOR)
            font = pygame.font.SysFont("Arial", 40)
            game_over_text = font.render(f"Ваш счет: {score}   Рекорд: {high_score}", True, (255, 255, 255))
            screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))
            pygame.display.flip()

            pygame.time.wait(2000)  # Небольшая пауза перед возвратом в меню
            game_state = 'menu'  # Переход в состояние меню

        clock.tick(speed)  # Учитываем текущую скорость игры

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
