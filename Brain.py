# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 18:24:08 2020

@author: patri
"""
import Vector as v, random

class Brain():
    
    def __init__(self, size):
        self.vectors = []
        self.size = size
        for i in range(size):
            self.vectors.append(v.Vector(0,0).randomVector(-2,2,-2,2))
            # Makes a bunch of random vectors at first
    
    def cloneVectors(self):
        '''clone = []
        for i in range(self.size):
            clone.append(self.vectors[i])
        return clone'''
        return self.vectors.copy()
    
    def mutate(self, chance, step):
        '''self.newVectors = []
        for i in range(0, self.size): # Change size to step param when fixed
            rand = random.random()
            if (rand < chance):
                self.newVectors.append(v.Vector(0,0).randomVector(-2,2,-2,2))
            else:
                self.newVectors.append(self.vectors[i].copy())'''
        
        #self.newVectors.append(v.Vector(0,0).randomVector(-2,2,-2,2))
        #self.vectors = self.newVectors
        for i in range(0, self.size):
            rand = random.random()
            if (rand < chance):
                self.vectors[i] = v.Vector(0,0).randomVector(-2,2,-2,2)
        