#!/usr/bin/python

import pygame
from threading import Event, Thread
from Algorithms import *
from Solutionspaces import *
from optparse import OptionParser
import pickle
import os.path

class Metaheuristic:
    def __init__(self, solutionspace, algorithm, stopevent, options):
        algorithm.initialize(solutionspace, options, stopevent)
        
        def getx(p):
            (a,b) = p
            return a
        def gety(p):
            (a,b) = p
            return b    
        
        (max_x, _) = max(solutionspace.solution, key = getx)
        (_, max_y) = max(solutionspace.solution, key = gety)
        self.range = max(max_x, max_y)
        self.size = 400
        self.pointSize = 3
        self.margin = 20
        self.closeDelay = 3
        self.visual = options.visual

        self.stopEvent = stopevent
        self.gen = algorithm.execute()
        self.algorithm = algorithm
        self.solution = solutionspace
        
        pygame.init()
        if options.visual:
            self.window = pygame.display.set_mode((self.size + 2 * self.margin, self.size + 2 * self.margin))
            self.update()
        
    def update(self):
        """ Update the graphical display. """
        #print self.algorithm.solutionval
        self.window.fill((255, 255, 255))

        def scale(p):
            (x, y) = p
            return (self.margin + int(x/self.range * self.size), self.size + self.margin - int(y/self.range * self.size))
        def pt(i):
            return scale(self.algorithm.solution[i])

        for p in self.algorithm.solution:
            pygame.draw.circle(self.window, (200, 200, 200), scale(p), int(0.2/self.range * self.size))
        for p in self.algorithm.solutionspace.initialsolution:
            pygame.draw.circle(self.window, (0, 0, 0), scale(p), self.pointSize)
        for i in range(0, len(self.algorithm.solution)):
            pygame.draw.line(self.window, (0,0,255), pt(i%len(self.algorithm.solution)), pt((i+1)%len(self.algorithm.solution)))

        pygame.display.flip()
        
    def step(self):
        try:
            self.gen.next()
        except StopIteration:
            if self.visual:
                self.update()
            self.stopEvent.wait(self.closeDelay)
            self.stopEvent.set()
            
def main():
    solutionspaces = {
        'tsp': TravellingSalesman(),
        'tcp': TravellingCouple(),
    }
    algorithms = {
        'hillclimb': Hillclimbing(),
        'annealing': SimulatedAnnealing(),
        'ascent': SteepestAscent(),
        'tabu': TabuSearch(),
    }
    parser = OptionParser()
    parser.add_option('-a', '--algorithm', type='choice',
                      default='hillclimb', dest='algorithm',
                      choices=algorithms.keys(),
                      help='algorithm to use')
    parser.add_option('-s', '--solutionspace', type='choice',
    				  default='tcp', dest='solutionspace',
    				  choices=solutionspaces.keys(),
    				  help='solutionspace to run on')
    parser.add_option('-f', '--file', default='', dest='filename',
    				  help='Give the solutionspace an input (else random)')
    parser.add_option('-d', '--delay', type='float',
                      default=0, dest='delay',
                      help='delay between each step in seconds')
    parser.add_option('-n', action="store_true", dest="displaysolution", default=False)
    parser.add_option("-v", action="store_false", dest="visual", default=True)
    
    (options, args) = parser.parse_args()
    
    algorithm = algorithms[options.algorithm];
    solutionspace = solutionspaces[options.solutionspace];
	
    stopEvent = Event()
    
    disp = Metaheuristic(solutionspace, algorithm, stopEvent, options)
    
    def update():
        """ Update loop; updates the screen every few seconds. """
        while True:
            if options.visual:
                stopEvent.wait(options.delay)
                disp.update()
                
            if stopEvent.isSet():
                break
            disp.step()

    if options.displaysolution:
        disp.update()
        print "The imported file has value: "+str(solutionspace.assess())
    else:
        #print "Starting "+str(algorithm)+" on "+str(options.solutionspace)+"..."            
        t = Thread(target=update)
        t.start()

    while not stopEvent.isSet():
        try:
            stopEvent.wait(options.delay)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stopEvent.set()
                elif event.type == pygame.KEYDOWN and event.unicode == 'p':
                    print algorithm.solutionval
                    print algorithm.solution.solution
        except KeyboardInterrupt:
            stopEvent.set()
    # logging of results:
    #log = open('results.log', 'a')
    #log.write('#############\nResult ('+options.algorithm+'): '+str(algorithm.solution.assess())+'\nSolution='+str(algorithm.solution.solution)+'\n;')
    #log.close()
    
    # log best solution
    if os.path.isfile('bestval.log'):
        h = open('bestval.log', 'r')
        bestval = pickle.load(h)
        h.close()
    else:
        bestval = 4294967295

    if algorithm.solutionval < bestval:
        bestval = algorithm.solutionval
        h = open('best.log', 'w')
        pickle.dump(algorithm.solution.solution, h)
        h.close()
        h = open('bestval.log', 'w')
        pickle.dump(bestval, h)
        h.close()
    print str(algorithm.solutionval)
#    print "Best: "+str(bestval)
    

if __name__ == "__main__":
    main()
