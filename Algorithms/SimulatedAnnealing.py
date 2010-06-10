from MetaAlgorithm import MetaAlgorithm
from random import random
from math import exp
import copy

class SimulatedAnnealing(MetaAlgorithm):
    """ The algorithm has been initialized into self.solution """    
    def execute(self):
        t = 10
        i = 0
        best = []
        bestval = -1
        yield
        while i < 2000:
            r = self.solution[:]
            self.solutionspace.tweak(r)
            rval = self.solutionspace.value(r)
            if rval < self.solutionval or t > 0 and random() < 2**(rval-self.solutionval)/t:
                self.solution = r
                self.solutionval = rval
                i = 0
                t=t*0.45
                yield
            if bestval == -1 or self.solutionval < bestval:
                best = self.solution
                bestval = self.solutionval
       	    
            i+=1
        self.solution = best
        self.solutionval = bestval
