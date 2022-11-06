# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 17:00:50 2020

@author: patri
"""
import Dot as d
from random import uniform

class Population():
    
    def __init__(self, x, y, size):
        self.pop = []
        self.gen = 1
        for i in range(size):
            self.pop.append(d.Dot(x,y))
    
    def reInitialize(self):
        self.pop = self.newPop
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
    
    def checkDeath(self, goalx, goaly, barrier, barrier2):
        for i in self.pop:
            if i.pos.v[0] <= 0 or i.pos.v[0] >= 500 or i.pos.v[1] <= 0 or i.pos.v[1] >= 500:
                i.die()
            if i.dist(goalx, goaly) <= 10:
                i.reachedGoal = True
                for j in self.pop:
                    j.die()
            barrier.check(i)
            barrier2.check(i)
    
    def kill(self):
        for i in self.pop:
            i.die()
                
    def calcFitness(self, goalx, goaly):
        for i in self.pop:
            i.calcFitness(goalx, goaly)
    
    def setBestDot(self):
        self.bestDot = self.getBestDot()
    
    def naturalSelection(self):
        self.newPop = self.pop
        self.calculateFitnessSum()
        self.noBestDot = 1
        
        try: self.newPop[0].brain.vectors = self.bestDot.gimmeBrainVectors()
        except: self.noBestDot = 0
        
        for i in range(self.noBestDot, len(self.pop)):
            parent = self.selectParent() #Select parent based on fitness
            self.newPop[i].brain.vectors = parent.gimmeBrainVectors()
        
        self.gen+=1
    
    def calculateFitnessSum(self):
        self.fitnessSum = 0
        for i in self.pop:
            self.fitnessSum += i.fitness
    
    def selectParent(self):
        rand = uniform(0, self.fitnessSum)
        runningSum = 0
        
        for i in self.pop:
            runningSum += i.fitness
            if (runningSum > rand):
                return i
    
    def mutateDemBabies(self, chance):
        for i in range(self.noBestDot, len(self.newPop)):
            if self.bestDot.reachedGoal:
                self.newPop[i].mutate(chance, self.bestDot.step, True)
            else:
                self.newPop[i].mutate(chance, self.bestDot.brain.size, False)
    
    def getBestDot(self):
        bestFitness = 0
        bestIndex = 0
        index = 0
        for i in self.pop:
            if i.fitness > bestFitness:
                bestFitness = i.fitness
                bestDot = i
                bestIndex = index
            index+=1
        #print(str(bestDot.step) + " " + str(bestIndex))
        return bestDot
                