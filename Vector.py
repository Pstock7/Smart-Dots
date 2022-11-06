# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 12:15:11 2020

@author: patri
"""
import math
from random import uniform

class Vector():
    
    def __init__(self, px, py):
        self.v = [float(px),float(py)] #Creates a vector with an x and y value
    
    def __add__(self, other):
        return Vector(self.v[0]+other.v[0], self.v[1]+other.v[1]) #Adds the x and y components of each vector
    
    def __mul__(self, other):
        return Vector(self.v[0]*other, self.v[1]*other) #Multiplies the x and y components by a value
    
    def __str__(self):
        return "[%f, %f]" % (self.v[0], self.v[1])
    
    def randomVector(self, xmin, xmax, ymin, ymax):
        return Vector(uniform(xmin,xmax), uniform(ymin,ymax))
    
    def length(self):
        return (self.v[0]**2 + self.v[1]**2)**0.5
    
    def copy(self):
        return Vector(self.v[0], self.v[1])
    
    def limit(self, lim): #Makes a limit for the length of the vector
        if self.length() > lim:
            angle = math.atan2(self.v[1], self.v[0])
            self.v[0] = lim*math.cos(angle)
            self.v[1] = lim*math.sin(angle)
            '''correction = 0.05
            if self.v[0]**2 > self.v[1]**2:
                if self.v[0] < 0:
                    self.v[0] += correction
                elif self.v[0] > 0:
                    self.v[0] -= correction
            else:
                if self.v[1] < 0:
                    self.v[1] += correction
                elif self.v[1] > 0:
                    self.v[1] -= correction
            self.limit(lim)'''
            