# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 21:21:28 2020

@author: patri
"""
import pygame

class Barrier():
    
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.sizex = x1
        self.sizey = y1
    
    def show(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.sizex, self.sizey))
    
    def check(self, dot):
        if dot.pos.v[0] <= self.x + self.sizex and dot.pos.v[0] >= self.x and dot.pos.v[1] <= self.y + self.sizey and dot.pos.v[1] >= self.y:
            dot.die()