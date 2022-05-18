import pygame
from pygame import Vector2
import random

#game initialize
pygame.init()
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

direction = "RIGHT"

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
    timer += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_UP]:
                direction = "UP"
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                direction = "DOWN"
            elif pygame.key.get_pressed()[pygame.K_LEFT]:
                direction = "LEFT"
            elif pygame.key.get_pressed()[pygame.K_RIGHT]:
                direction = "RIGHT"

    if timer >= 900:
        for i in range(len(snake_parts)):
            if i != 0:
                snake_parts[len(snake_parts) - i].center = snake_parts[i - 1].center

        if direction == "UP":
            snake_parts[0].center += Vector2(0, -50)
        elif direction == "DOWN":
            snake_parts[0].center += Vector2(0, 50)
        elif direction == "LEFT":
            snake_parts[0].center += Vector2(-50, 0)
        elif direction == "RIGHT":
            snake_parts[0].center += Vector2(50, 0)

        for i in range(len(apples)):
            if apples[i].center == snake_parts[0].center:
                apples.pop(i)
                apple = pygame.rect.Rect(random.randint(1, 9) * 50 + 7, random.randint(1, 9) * 50 + 7, apple_width,
                                         apple_height)
                apples.append(apple)

                snake_body = pygame.rect.Rect(snake_parts[0].centerx, snake_parts[0].centery, snake_width, snake_height)
                snake_parts.append(snake_body)
                print(snake_parts)

        timer -= 900

    window.fill(LIGHT_GRAY)

    for i in range(len(snake_parts) + 1):
        print(i)
        if i == 0:
            color = ORANGE
        else:
            color = DARK_GRAY
        pygame.draw.rect(window, color, snake_parts[i - 1])

    for rect in apples:
        pygame.draw.rect(window, RED, rect)

    pygame.display.update()
