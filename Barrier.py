"""
Created on Thu Nov 12 21:21:28 2020

@author: Patrick Stock
"""
import pygame


class Barrier:

    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.sizeX = x1
        self.sizeY = y1

    def show(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.sizeX, self.sizeY))

    def check(self, dot):
        if self.x + self.sizeX >= dot.pos.v[0] >= self.x and self.y + self.sizeY >= dot.pos.v[1] >= self.y:
            dot.die()
