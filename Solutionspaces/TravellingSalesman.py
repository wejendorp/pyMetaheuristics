from Solutionspace import Solutionspace
from random import *
from math import *
import os.path

class TravellingSalesman(Solutionspace):
    def initialize(self, options):
        self.load(options.filename)
        if len(self.solution) == 0:
            self.randomize()
            
    def randomize(self):
        print "This should be a random space"
        pass

    def tweak(self):
        # Only allow disjoint edges
        r1 = 0
        r2 = 0
        while abs(r1-r2)<1:
            r1 = randint(1,len(self.solution)-1)
            r2 = randint(1,len(self.solution)-1)
        #number of elements we wanna swap [r1+i] <=> [r2-i]
        r = int(floor((abs(r1 - r2))/2))
        #Swap two nodes
        if random() < 0.05 or r == 0:
            temp = self.solution[r1]
            self.solution[r1] = self.solution[r2]
            self.solution[r2] = temp
        #swap two edges
        else:
            for i in range(0, r):
                temp = self.solution[(r1+i)%len(self.solution)]
                self.solution[(r1+i)%len(self.solution)] = self.solution[(r2-i)%len(self.solution)]
                self.solution[(r2-i)%len(self.solution)] = temp
                
        return [self.solution[r1], self.solution[r2]]

    def assess(self):
        def distance(a,b):
            (xa,ya) = a
            (xb,yb) = b
            return sqrt(abs(xa-xb)**2+abs(ya-yb)**2)

        sum = 0
        for i in range(0,len(self.solution)-1):
            sum += distance(self.solution[i], self.solution[(i+1) % len(self.solution)])
        return sum
