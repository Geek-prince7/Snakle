import pygame
from pygame.locals import *
import time


class Snake:
    def __int__(self, parent_screen):
        self.surface = parent_screen
        # load image
        self.block = pygame.image.load("Resouce/block.jpg").convert()
        # add block img on game screen
        self.y_cord = 100
        self.x_cord = 100

    def draw(self):
        self.surface.fill((110, 110, 5))
        self.surface.blit(self.block, (self.x_cord, self.y_cord))
        pygame.display.flip()

    def move_up(self):
        self.y_cord -= 10
        self.draw()

    def move_down(self):
        self.y_cord += 10
        self.draw()

    def move_right(self):
        self.x_cord += 10
        self.draw()

    def move_left(self):
        self.x_cord -= 10
        self.draw()


class Game:
    # constructor
    def __int__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 700))
        # set background color
        self.surface.fill((110, 110, 5))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        # event loop
        running = True
        # to hold game screen
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    # using escape key i will quit game window
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()
                # byclicking on x button it will close otherwise it wont close
                elif event.type == QUIT:
                    running = False

if __name__ =="__main__":
    game=Game()
    game.run()



