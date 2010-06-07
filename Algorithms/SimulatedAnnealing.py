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
        self.solutionval = self.solution.assess()
        yield
        while i < 1000:
            r = copy.deepcopy(self.solution)
            r.tweak()
            rval = r.assess()
            if rval < self.solutionval or t > 0 and random() < exp((rval-self.solutionval)/t):
                self.solution = r
                self.solutionval = rval
                i = 0
                yield
            if bestval == -1 or self.solutionval < bestval:
                best = self.solution
                bestval = self.solutionval
            t-=0.01
            i+=1
        self.solution = best
        self.solutionval = bestval
