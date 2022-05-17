import pygame
from pygame import Vector2

class SnakeHead(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.surface.Surface((45, 45))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(250, 250)

        self.direction = "RIGHT"

    def move(self):
        if self.direction == "UP":
            self.rect.center += Vector2(0, -50)
        elif self.direction == "DOWN":
            self.rect.center += Vector2(0, 50)
        elif self.direction == "LEFT":
            self.rect.center += Vector2(-50, 0)
        elif self.direction == "RIGHT":
            self.rect.center += Vector2(50, 0)

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.direction = "UP"
                elif event.key == pygame.K_DOWN:
                    self.direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    self.direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    self.direction = "RIGHT"

    def get_pos(self):
        return self.rect.center

class SnakeBody(pygame.sprite.Sprite):
    def __init__(self, color):
        super().__init__()
        self.image = pygame.surface.Surface((45, 45))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = Vector2(250, 250)

    def set_pos(self, pos):
        self.rect.center = pos

    def get_pos(self):
        return self.rect.center

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
LIGHT_GRAY = pygame.Color(79, 79, 79)
DARK_GRAY = pygame.Color(43, 43, 43)

#snake
snake_group = pygame.sprite.Group()
snake_head = SnakeHead(ORANGE)
snake_group.add(snake_head)
snake_body = SnakeBody(DARK_GRAY)
snake_group.add(snake_body)



#game loop
run = True
while run:
    timer += 1

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    if timer >= 800:
        for i in range(len(snake_group.sprites())):
            if i != 0:
                pos = snake_group.sprites()[i - 1].get_pos()
                snake_group.sprites()[i].set_pos(pos)

        snake_body = SnakeBody(DARK_GRAY)
        snake_group.add(snake_body)

        snake_group.sprites()[0].move()
        timer -= 800

    snake_group.update(events)

    window.fill(LIGHT_GRAY)
    snake_group.draw(window)

    pygame.display.update()
