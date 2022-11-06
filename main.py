# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 00:52:00 2020

@author: patri
"""
import sys, pygame, Population, Barrier, keyboard
from time import perf_counter
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5 as qt

# Pygame stuff
pygame.init()
myfont = pygame.font.SysFont('Ariel', 30)

display_width = 500
display_height = 500

win = pygame.display.set_mode((display_width, display_height)) 
pygame.display.set_caption("Smart Dots")

clock = pygame.time.Clock()
fps = 60

# Population stuff
x = display_width/2
y = display_height-25
populationSize = 500
pop = Population.Population(x, y, populationSize)

# Barriers and goal
barrier = Barrier.Barrier(100, 200, 400, 10)
barrier2 = Barrier.Barrier(0, 350, 400, 10)
goalx = int(display_width/2)
goaly = 25

# Plot performance with matplotlib
matplotlib.use("Qt5Agg")
plt.ion()
times = []

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

    win.fill((255, 255, 255)) 
    pygame.draw.ellipse(win, (0, 0, 255), (goalx-8, goaly-8, 16, 16))
    textsurface = myfont.render('Gen %d' % pop.gen, False, (0,0,0))
    win.blit(textsurface, (400,470))
    
    if pop.allDead():
        startEvolution = perf_counter()
        
        pop.calcFitness(goalx, goaly)
        pop.setBestDot()
        pop.naturalSelection()
        pop.mutateDemBabies(0.05)
        pop.reInitialize()

        endEvolution = perf_counter()
        elapsedTime = endEvolution - startEvolution

        # Plot performance
        times.append(elapsedTime)
        x = list(range(0, len(times)))
        plt.plot(x, times)
        plt.title('Performance vs Runs')
        plt.xlabel('Run Number')
        plt.ylabel('Time (seconds)')
        plt.draw()

        print(f'Evolution Time: {(elapsedTime):.3f}')
    else:
        pop.move()
        pop.checkDeath(goalx, goaly, barrier, barrier2)
        if pygame.key.get_focused() and keyboard.is_pressed('b'):
            key = False
        else:
            key = True
        pop.show(win, key)
        barrier.show(win)
        barrier2.show(win)
    
    pygame.display.update()
    if pygame.key.get_focused():
        if keyboard.is_pressed('a'):
            fps = 45
        elif keyboard.is_pressed('s'):
            fps = 60
        elif keyboard.is_pressed('d'):
            fps = 120
        elif keyboard.is_pressed('f'):
            fps = 240
    clock.tick(fps)