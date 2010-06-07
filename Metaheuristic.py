#!/usr/bin/python

import pygame
from threading import Event, Thread
from Algorithms import *
from Solutionspaces import *
from optparse import OptionParser

class Metaheuristic:
    def __init__(self, solutionspace, algorithm, stopevent, options):
        algorithm.initialize(solutionspace, options)
        
        def getx(p):
            (a,b) = p
            return a
        def gety(p):
            (a,b) = p
            return b    
        
        (self.max_x, _) = max(solutionspace.solution, key = getx)
        (_, self.max_y) = max(solutionspace.solution, key = gety)
        
        self.size = 400
        self.pointSize = 5
        self.margin = 20
        self.closeDelay = 5


        self.stopEvent = stopevent
        self.gen = algorithm.execute()
        self.algorithm = algorithm
        self.solution = solutionspace
        
        pygame.init()
        self.window = pygame.display.set_mode((self.size + 2 * self.margin, self.size + 2 * self.margin))

        self.i = 0
        self.update()
        
    def update(self):
        """ Update the graphical display. """
        print self.algorithm.solution.assess()
        self.window.fill((255, 255, 255))

        def scale(p):
            (x, y) = p
            return (self.margin + int(x/self.max_x * self.size), self.margin + int(y/self.max_y * self.size))
        def pt(i):
            return scale(self.algorithm.solution.solution[i])

        for p in self.algorithm.solution.solution:
            pygame.draw.circle(self.window, (0, 0, 0), scale(p), self.pointSize)

        for i in range(0, len(self.solution.solution)):
            pygame.draw.line(self.window, (0,0,255), pt(i), pt((i+1)%len(self.solution.solution)))

        pygame.display.flip()
        
    def step(self):
        try:
            self.gen.next()
        except StopIteration:
            self.update()
            self.stopEvent.wait(self.closeDelay)
            self.stopEvent.set()
            
def main():
    solutionspaces = {
        'tsp': TravellingSalesman(),
    }
    algorithms = {
        'hillclimb': Hillclimbing(),
    }
    parser = OptionParser()
    parser.add_option('-a', '--algorithm', type='choice',
                      default='hillclimb', dest='algorithm',
                      choices=algorithms.keys(),
                      help='algorithm to use')
    parser.add_option('-s', '--solutionspace', type='choice',
    				  default='tsp', dest='solutionspace',
    				  choices=solutionspaces.keys(),
    				  help='solutionspace to run on')
    parser.add_option('-f', '--file', default='', dest='filename',
    				  help='Give the solutionspace an input (else random)')
    parser.add_option('-d', '--delay', type='float',
                      default=0.01, dest='delay',
                      help='delay between each step in seconds')
    (options, args) = parser.parse_args()
    
    algorithm = algorithms[options.algorithm];
    solutionspace = solutionspaces[options.solutionspace];
	
    stopEvent = Event()
    
    disp = Metaheuristic(solutionspace, algorithm, stopEvent, options)
    
    def update():
        """ Update loop; updates the screen every few seconds. """
        while True:
            stopEvent.wait(options.delay)
            disp.update()
            if stopEvent.isSet():
                break
            disp.step()

    t = Thread(target=update)
    t.start()

    while not stopEvent.isSet():
        try:
            stopEvent.wait(options.delay)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stopEvent.set()
        except KeyboardInterrupt:
            stopEvent.set()

if __name__ == "__main__":
    main()
