"""
Created on Sun Oct 11 02:15:02 2020

@author: Patrick Stock
"""
import math
from copy import deepcopy
import pygame
import Brain
import Vector


class Dot:
    # global width, height
    height = 5
    width = 5
    pos = Vector.Vector(0, 0)
    vel = Vector.Vector(0, 0)
    acc = Vector.Vector(0, 0)
    counter = 0

    def __init__(self, x, y):
        self.fitness = 0
        self.startX = x
        self.startY = y
        self.pos = Vector.Vector(x, y)  # Starting position of the dot
        self.brain = Brain.Brain()  # Makes a brain
        self.dead = False
        self.reachedGoal = False
        self.step = 0

    def __deepcopy__(self, memo=None):
        copy = Dot(self.startX, self.startY)
        copy.fitness = self.fitness
        copy.pos = self.pos.copy()
        copy.brain = deepcopy(self.brain)
        copy.dead = self.dead
        copy.reachedGoal = self.reachedGoal
        copy.step = self.step
        return copy

    def reInitialize(self):
        self.counter = 0
        self.step = 0
        self.pos.v[0] = self.startX
        self.pos.v[1] = self.startY
        self.vel.v[0] = 0
        self.vel.v[1] = 0
        self.acc.v[0] = 0
        self.acc.v[1] = 0
        self.reachedGoal = False
        self.dead = False

    def show(self, win, color):
        pygame.draw.ellipse(win, color, (self.pos.v[0] - self.width / 2,
                                         self.pos.v[1] - self.height / 2,
                                         self.width, self.height))
        # Draws the dot in pygame

    def move(self):
        if not self.dead:
            if self.counter > len(self.brain.vectors) - 1:
                self.brain.addRandomVector()
            self.acc = self.brain.vectors[self.counter]
            self.vel += self.acc
            self.vel.limit(7)  # Limits the vector to a length of 7
            self.pos += self.vel
            self.counter += 1
            self.step += 1

    def die(self):
        self.dead = True
        if self.pos.v[0] <= 0:
            self.pos.v[0] = 0.001
        elif self.pos.v[0] > 500:
            self.pos.v[0] = 500
        if self.pos.v[1] <= 0:
            self.pos.v[1] = 0.001
        elif self.pos.v[1] > 500:
            self.pos.v[1] = 500

    def dist(self, x, y):
        return math.sqrt((self.pos.v[0] - x) ** 2 + (self.pos.v[1] - y) ** 2)

    def calcFitness(self, goalX, goalY):
        self.fitness = 1 / (self.dist(goalX, goalY) ** 2)
        '''if self.pos.v[1] < 250:
            self.fitness *= 10
        if self.pos.v[1] < 100 and self.pos.v[0] > 100 and self.pos.v[0] < 400:
            self.fitness *= 10'''

    def gimmeBrainVectors(self):
        return self.brain.cloneVectors()

    def mutate(self, chance):
        self.brain.mutate(chance)
