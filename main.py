import pygame
from pygame.locals import *
import time
import random


class Apple:
    def __init__(self, parent_screen):
        self.image = pygame.image.load("Resouce/apple.jpg").convert()
        self.surface = parent_screen
        self.x = 120
        self.y = 160

    def draw(self):
        self.surface.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move(self):
        self.x = random.randint(1,25)*40
        self.y = random.randint(1,17)*40

    def return_apple_pos(self):
        return self.x , self.y


class Snake:
    def __init__(self, parent_screen, length):
        self.surface = parent_screen
        self.block = pygame.image.load("Resouce/block.jpg").convert()
        self.b_height = self.block.get_height()
        self.b_width = self.block.get_width()
        self.len = length
        self.x = [40] * length
        self.y = [40] * length
        self.direction = 'down'

    def draw(self, len1=1):
        self.surface.fill((110, 110, 5))
        newl = int(len1)
        if (self.len < newl):
            self.len = newl
            newl = newl - len(self.x)
            for i in range(newl):
                self.x.append(self.x[0])
                self.y.append(self.y[0])

        for i in range(self.len):
            self.surface.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def return_snake_pos(self):
        return self.x[0] , self.y[0]

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_right(self):
        self.direction = 'right'

    def move_left(self):
        self.direction = 'left'

    def walk(self):

        for i in range(self.len - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'up':
            self.y[0] -= self.b_height
        elif self.direction == 'down':
            self.y[0] += self.b_height
        elif self.direction == 'right':
            self.x[0] += self.b_width
        elif self.direction == 'left':
            self.x[0] -= self.b_width
        self.draw()


class Game:
    # constructor
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1200, 700))
        self.length = 1
        self.snake = Snake(self.surface, self.length)
        self.snake.draw()
        self.apple = Apple(self.surface)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def size_change(self):
        self.length += 1
        self.snake.draw(self.length)

    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_1:
                        self.size_change()


                elif event.type == QUIT:
                    running = False

            self.play()
            if self.apple.return_apple_pos()==self.snake.return_snake_pos():
                self.apple.move()
                self.size_change()
            time.sleep(0.3)


if __name__ == '__main__':
    game = Game()
    game.run()
