import pygame
from pygame import Vector2
import random

def same_pos(rect, rects):
    for i in range(len(rects)):
        if rect.center == rects[i].center:
            return False
    return True

#game initialize
pygame.init()


#window
pygame.display.set_caption("Snake")
window_width = 1600
window_height = 900
window = pygame.display.set_mode((window_width, window_height))

#settings
clock = pygame.time.Clock()
timer = 0
box_width = 20
box_height = 20
rows = int(window_width / box_width)
columns = int(window_height / box_height)
font = pygame.font.Font("pixel_font.ttf", 50)

#colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
ORANGE = pygame.Color(255, 68, 0)
RED = pygame.Color(255, 15, 15)
LIGHT_GRAY = pygame.Color(79, 79, 79)
DARK_GRAY = pygame.Color(43, 43, 43)

def new_snake_part(snake_width, snake_height):
    body_pos = Vector2(snake_parts[snake_len - 1].centerx,
                        snake_parts[snake_len - 1].centery)
    body = pygame.rect.Rect(-100, -100, snake_width, snake_height)
    body.center = body_pos
    return body

#snake
snake_width = 16
snake_height = 16
snake_g_colors = [255]

direction = "RIGHT"

snake_parts = []
snake_head_pos = Vector2(int(rows / 2) * box_width, int(columns / 2) * box_height)
snake_head = pygame.rect.Rect(0, 0, snake_width, snake_height)
snake_head.center = snake_head_pos
snake_parts.append(snake_head)

def new_apple(apple_width, apple_height):
    apple_pos = Vector2(random.randint(1, int(window_width / box_width) - 1) * box_width,
                        random.randint(1, int(window_height / box_height) - 1) * box_height)
    apple = pygame.rect.Rect(-100, -100, apple_width, apple_height)
    apple.center = apple_pos
    return apple

#apples
apple_width = 12
apple_height = 12

apples = []
apple = new_apple(apple_width, apple_height)
apples.append(apple)

#score
score = 0

score_text = font.render(f"score: {score}", True, WHITE)

#game loop
run = True
while run:
    clock.tick(50 * 1000)
    timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and direction != "DOWN":
            direction = "UP"
        elif pressed[pygame.K_DOWN] and direction != "UP":
            direction = "DOWN"
        elif pressed[pygame.K_LEFT] and direction != "RIGHT":
            direction = "LEFT"
        elif pressed[pygame.K_RIGHT] and direction != "LEFT":
            direction = "RIGHT"

    if timer >= 40:

        snake_len = len(snake_parts)

        for i in range(snake_len):
            if snake_len - i - 2 >= 0:
                new_pos = snake_parts[snake_len - i - 2].center
                snake_parts[snake_len - i - 1].center = new_pos
        if direction == "UP":
            snake_parts[0].center += Vector2(0, -box_height)
        elif direction == "DOWN":
            snake_parts[0].center += Vector2(0, box_height)
        elif direction == "LEFT":
            snake_parts[0].center += Vector2(-box_width, 0)
        elif direction == "RIGHT":
            snake_parts[0].center += Vector2(box_width, 0)

        snake_head = snake_parts[0]
        for i in range(snake_len):
            if i != 0:
                if snake_head.center == snake_parts[i].center:
                    run = False
                    pygame.quit()
        if snake_head.centerx <= 0 or snake_head.centerx >= window_width or \
            snake_head.centery <= 0 or snake_head.centery >= window_height:
            run = False
            pygame.quit()

        if apples[0].center == snake_parts[0].center:
            apples.pop(0)

            apple = new_apple(apple_width, apple_height)
            while not same_pos(apple, snake_parts):
                apple = new_apple(apple_width, apple_height)
            apples.append(apple)

            snake_part = new_snake_part(snake_width, snake_height)
            snake_parts.append(snake_part)

            score += 1

            last_color = snake_g_colors[len(snake_g_colors) - 1]
            snake_g_colors.append(last_color - 0.5)

        score_text = font.render(f"score: {score}", True, WHITE)

        timer -= 40


    window.fill(BLACK)

    for rect in apples:
        pygame.draw.rect(window, RED, rect)

    for i in range(len(snake_parts)):
        color = pygame.Color(5, int(snake_g_colors[i]), 5)
        pygame.draw.rect(window, color, snake_parts[i])

    window.blit(score_text, (10, 10))

    pygame.display.update()
