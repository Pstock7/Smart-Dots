"""
Created on Sun Oct 18 18:24:08 2020

@author: Patrick Stock
"""
import random

from Vector import randomVector


class Brain:

    def __init__(self):
        self.vectors = []

    def __deepcopy__(self, memo=None):
        copy = Brain()
        copy.vectors = self.vectors.copy()
        return copy

    def addRandomVector(self):
        self.vectors.append(randomVector(-2, 2, -2, 2))

    def cloneVectors(self):
        return self.vectors.copy()

    def mutate(self, chance):
        for i in range(0, len(self.vectors)):
            rand = random.random()
            if rand < chance:
                self.vectors[i] = randomVector(-2, 2, -2, 2)
