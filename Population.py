"""
Created on Sun Oct 11 17:00:50 2020

@author: Patrick Stock
"""
from copy import deepcopy
from random import uniform
import Dot


class Population:

    def __init__(self, x, y, size):
        self.fitnessSum = 0
        self.bestDot = None
        self.noBestDot = None
        self.pop = []
        self.gen = 1
        for i in range(size):
            self.pop.append(Dot.Dot(x, y))

    def reInitialize(self):
        for i in self.pop:
            i.reInitialize()

    def allDead(self):
        for i in self.pop:
            if not i.dead:
                return False
        return True

    def show(self, win, key):
        for i in range(0, len(self.pop)):
            if i > 0 and key:
                self.pop[i].show(win, (0, 0, 0))
            if self.gen > 1:
                self.pop[0].show(win, (255, 0, 0))
            else:
                self.pop[0].show(win, (0, 0, 0))

    def move(self):
        for i in self.pop:
            i.move()

    def checkDeath(self, goalX, goalY, barrier, barrier2):
        for i in self.pop:
            if i.pos.v[0] <= 0 or i.pos.v[0] >= 500 or i.pos.v[1] <= 0 or i.pos.v[1] >= 500:
                i.die()
            if i.dist(goalX, goalY) <= 10:
                i.reachedGoal = True
                for j in self.pop:
                    j.die()
            barrier.check(i)
            barrier2.check(i)

    def kill(self):
        for i in self.pop:
            i.die()

    def calcFitness(self, goalX, goalY):
        for i in self.pop:
            i.calcFitness(goalX, goalY)

    def setBestDot(self):
        self.bestDot = self.getBestDot()

    def naturalSelection(self):
        newPop = deepcopy(self.pop)
        self.calculateFitnessSum()
        self.noBestDot = 1

        if self.bestDot is not None:
            newPop[0].brain.vectors = self.bestDot.gimmeBrainVectors()
        else:
            self.noBestDot = 0

        for i in range(self.noBestDot, len(self.pop)):
            parent = self.selectParent()  # Select parent based on fitness
            newPop[i].brain.vectors = parent.gimmeBrainVectors()

        self.gen += 1
        self.pop = deepcopy(newPop)

    def calculateFitnessSum(self):
        self.fitnessSum = 0
        for i in self.pop:
            self.fitnessSum += i.fitness

    def selectParent(self):
        rand = uniform(0, self.fitnessSum)
        runningSum = 0

        for i in self.pop:
            runningSum += i.fitness
            if runningSum > rand:
                return i

    def mutateDemBabies(self, chance):
        for i in range(self.noBestDot, len(self.pop)):
            self.pop[i].mutate(chance)

    def getBestDot(self):
        bestFitness = 0
        foundDot = None
        for i in self.pop:
            if i.fitness > bestFitness:
                bestFitness = i.fitness
                foundDot = i
        # print(str(bestDot.step) + " " + str(bestIndex))
        return foundDot
