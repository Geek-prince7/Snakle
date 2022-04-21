import pygame
from pygame.locals import *
import time

def draw_block():
    surface.fill((110, 110, 5))
    surface.blit(block, (x_cord, y_cord))
    pygame.display.flip()




if __name__ =="__main__":
    pygame.init()
    surface=pygame.display.set_mode((1000,700))
    #set background color
    surface.fill((110, 110, 5))

    #update the screen for bg color
    pygame.display.flip()
    #loadimage
    block=pygame.image.load("Resouce/block.jpg").convert()
    #add block img on game screen
    y_cord=100
    x_cord=100
    surface.blit(block,(x_cord,y_cord))
    #uodate the screen
    pygame.display.flip()

    #event loop
    running=True
    #to hold game screen
    while running:
        for event in pygame.event.get():
            if event.type==KEYDOWN:
                #using escape key i will quit game window
                if event.key==K_ESCAPE:
                    running=False
                if event.key==K_UP:
                    y_cord-=10
                    draw_block()

                if event.key==K_DOWN:
                    y_cord+=10
                    draw_block()


                if event.key==K_LEFT:
                    x_cord-=10
                    draw_block()

                if event.key==K_RIGHT:
                    x_cord+=10
                    draw_block()


            #byclicking on x button it will close otherwise it wont close
            elif event.type==QUIT:
                running=False

