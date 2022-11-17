"""
Created on Sun Oct 11 00:52:00 2020

@author: Patrick Stock
"""
import sys
from time import perf_counter
import keyboard
import pygame
import Barrier
import Population

if __name__ == "__main__":
    # Pygame stuff
    pygame.init()
    myFont = pygame.font.SysFont('Ariel', 30)

    # Display size
    display_width = 500
    display_height = 500

    win = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Smart Dots")

    clock = pygame.time.Clock()
    fps = 60

    # Population stuff
    x = display_width / 2
    y = display_height - 25
    populationSize = 500
    pop = Population.Population(x, y, populationSize)

    # Barriers and goal
    barrier = Barrier.Barrier(100, 200, 400, 10)
    barrier2 = Barrier.Barrier(0, 350, 400, 10)
    goalX = int(display_width / 2)
    goalY = 25

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Checks if the window has been closed
                pygame.quit()
                sys.exit()

        win.fill((255, 255, 255))  # White background
        pygame.draw.ellipse(win, (0, 0, 255), (goalX - 8, goalY - 8, 16, 16))  # Draw the goal
        textSurface = myFont.render(f'Gen {pop.gen}', False, (0, 0, 0))  # Generation counter
        win.blit(textSurface, (400, 470))  # Draw generation counter in window

        if pop.allDead():
            startEvolution = perf_counter()

            pop.calcFitness(goalX, goalY)  # Calculates the fitness of all dots
            pop.setBestDot()               # Sets the best dot to be immortal (no mutations)
            pop.naturalSelection()         # Only the best dots reproduce
            pop.mutateDemBabies(0.05)      # Make each new dot slightly different
            pop.reInitialize()             # Gets ready for the next generation

            endEvolution = perf_counter()
            elapsedTime = endEvolution - startEvolution

            print(f'Gen {pop.gen} Evolution Time: {elapsedTime:.3f}')
        else:
            pop.move()  # Moves each dot one step
            pop.checkDeath(goalX, goalY, barrier, barrier2)  # Checks whether the dot has run into something
            if pygame.key.get_focused() and keyboard.is_pressed('b'):
                key = False  # Press 'b' on keyboard to only show best dot
            else:
                key = True
            pop.show(win, key)  # Draw dots in window
            barrier.show(win)   # Draw the first barrier
            barrier2.show(win)  # Draw the second barrier

        pygame.display.update()  # Update the display
        if pygame.key.get_focused():  # Control speed with asdf keys
            if keyboard.is_pressed('a'):
                fps = 45
            elif keyboard.is_pressed('s'):
                fps = 60
            elif keyboard.is_pressed('d'):
                fps = 120
            elif keyboard.is_pressed('f'):
                fps = 240
        clock.tick(fps)
