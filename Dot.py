# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 02:15:02 2020

@author: patri
"""
import Vector as v, pygame, Brain as b, math

class Dot():
   
    global width, height
    height = 5
    width = 5
    pos = v.Vector(0,0)
    vel = v.Vector(0,0)
    acc = v.Vector(0,0)
    counter = 0
    
    def __init__(self, x, y):
        self.startx = x
        self.starty = y
        self.pos = v.Vector(x, y) #Starting position of the dot
        self.brain = b.Brain(500) #Makes a brain
        self.dead = False
        self.reachedGoal = False
        self.step = 0
        self.previousStep = self.brain.size
        self.ceiling = self.brain.size
    
    def reInitialize(self):
        self.counter = 0
        self.step = 0
        self.pos.v[0] = self.startx
        self.pos.v[1] = self.starty
        self.vel.v[0] = 0
        self.vel.v[1] = 0
        self.acc.v[0] = 0
        self.acc.v[1] = 0
        self.reachedGoal = False
        self.dead = False
    
    def show(self, win, color):
        pygame.draw.ellipse(win, color, (self.pos.v[0]-width/2, self.pos.v[1]-height/2, width, height))
        #Draws the dot in pygame
    
    def move(self):
        if not self.dead:
            self.acc = self.brain.vectors[self.counter]
            self.vel += self.acc
            self.vel.limit(7) #Limits the vector to a length of 7
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
        return math.sqrt((self.pos.v[0] - x)**2 + (self.pos.v[1] - y)**2)
    
    def calcFitness(self, goalx, goaly):
        self.fitness = 1/(self.dist(goalx, goaly)**2)
        '''if self.pos.v[1] < 250:
            self.fitness *= 10
        if self.pos.v[1] < 100 and self.pos.v[0] > 100 and self.pos.v[0] < 400:
            self.fitness *= 10'''
    
    def gimmeBrainVectors(self):
        return self.brain.cloneVectors()
    
    def mutate(self, chance, step, goalReached):
        if goalReached:
            if step > self.previousStep:
                step = self.previousStep
            else:
                self.ceiling = step+20
            self.previousStep = step
        self.brain.mutate(chance, self.ceiling)