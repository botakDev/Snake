import pygame
from pygame import Vector2
import random

def check_same_pos(rect, rects):
    for i in range(len(rects)):
        if rect.center == rects[i].center:
            return True
    return False


#game initialize
pygame.init()
clock = pygame.time.Clock()
timer = 0

#window
pygame.display.set_caption("Snake")
window = pygame.display.set_mode((500, 500))

#colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
ORANGE = pygame.Color(255, 68, 0)
RED = pygame.Color(255, 15, 15)
LIGHT_GRAY = pygame.Color(79, 79, 79)
DARK_GRAY = pygame.Color(43, 43, 43)

#snake
snake_width = 45
snake_height = 45
snake_g_colors = [255]

direction = "RIGHT"
changed_direction = False

snake_parts = []
snake_head = pygame.rect.Rect(252, 252, snake_width, snake_height)
snake_parts.append(snake_head)

#apples
apple_width = 35
apple_height = 35

apples = []
apple = pygame.rect.Rect(random.randint(1, 9) * 50 + 7, random.randint(1, 9) * 50 + 7, apple_width,
                         apple_height)
apples.append(apple)

#game loop
run = True
while run:
    clock.tick(90 * 1000)
    timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if changed_direction == False:
                if pygame.key.get_pressed()[pygame.K_UP] and direction != "DOWN":
                    direction = "UP"
                elif pygame.key.get_pressed()[pygame.K_DOWN] and direction != "UP":
                    direction = "DOWN"
                elif pygame.key.get_pressed()[pygame.K_LEFT] and direction != "RIGHT":
                    direction = "LEFT"
                elif pygame.key.get_pressed()[pygame.K_RIGHT] and direction != "LEFT":
                    direction = "RIGHT"
                changed_direction = True

    if timer >= 800:
        changed_direction = False

        snake_len = len(snake_parts)
        apple_len = len(apples)

        for i in range(snake_len):
            if snake_len - i - 2 >= 0:
                snake_parts[snake_len - i - 1].center = snake_parts[snake_len - i - 2].center

        if direction == "UP":
            snake_parts[0].center += Vector2(0, -50)
        elif direction == "DOWN":
            snake_parts[0].center += Vector2(0, 50)
        elif direction == "LEFT":
            snake_parts[0].center += Vector2(-50, 0)
        elif direction == "RIGHT":
            snake_parts[0].center += Vector2(50, 0)

        for i in range(snake_len):
            if i >= 1:
                if snake_parts[0].center == snake_parts[i].center:
                    run = False
                    pygame.quit()
            if snake_parts[0].centerx < 0 or snake_parts[0].centerx > 500 or \
                        snake_parts[0].centery < 0 or snake_parts[0].centery > 500:
                run = False
                pygame.quit()

        for i in range(apple_len):
            if apples[i].center == snake_parts[0].center:
                apples.pop(i)
                apple = pygame.rect.Rect(random.randint(1, 9) * 50 + 7, random.randint(1, 9) * 50 + 7, apple_width,
                                         apple_height)
                while check_same_pos(apple, snake_parts):
                    apple = pygame.rect.Rect(random.randint(1, 9) * 50 + 7, random.randint(1, 9) * 50 + 7, apple_width,
                                             apple_height)

                apples.append(apple)

                snake_body = pygame.rect.Rect(snake_parts[snake_len - 1].x, snake_parts[snake_len - 1].y, snake_width, snake_height)
                snake_parts.append(snake_body)
                snake_g_colors.append(snake_g_colors[len(snake_g_colors) - 1] - 2.3)

        timer -= 800

    window.fill(BLACK)

    for rect in apples:
        pygame.draw.rect(window, RED, rect)

    for i in range(len(snake_parts)):
        color = pygame.Color(5, int(snake_g_colors[i]), 5)
        pygame.draw.rect(window, color, snake_parts[i])

    pygame.display.update()
