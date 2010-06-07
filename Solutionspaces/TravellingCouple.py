from Solutionspace import Solutionspace
from random import randint
from math import *
from copy import copy
import os.path

class TravellingCouple(Solutionspace):
    dist = 0.2
    
    def initialize(self, options):
        self.load(options.filename)
        if len(self.solution) == 0:
            self.randomize()
            
        #Figure out which nodes rule out other nodes
        self.groups = []
        for i in range(0,len(self.solution)-1):
            self.groups.append([self.solution[i]])
            for j in range(i,len(self.solution)-1):
                if (self.distance(self.solution[i], self.solution[j])) < self.dist:
                    self.groups[i].append(self.solution[j])
        
    def randomize(self):
        print "This should be a random space"
        pass

    def tweak(self):
        #perform a D-tweak in 5% of the cases:
        if randint(0,100) <= 5:
            self.dTweak()
        else:
            self.swapTweak()

    def dTweak(self):
        # Check that there are overlaps
        if max(self.groups, key = len) > 1:
            #Find an element to remove in the current solution
            i = randint(0,len(self.groups)-1)
            while True:
                if len(self.groups[i]) > 1 and self.groups[i][0] in self.solution:
                    break;
                else:
                   # print 'dTweakLoop'+str(i)
                    i = (i + 1) % len(self.groups)
            # i now points to an element that overlaps another, which is in the graph
            elmindex = self.solution.index(self.groups[i][0])
            elm = self.solution.pop(elmindex)
            def f(x): return elm in x
            grp = filter(f, copy(self.groups))
            # grp is now all clusters including x
            # find a list that has no members of sol and inserts
            i = randint(0,len(grp)-1)
            t = i
            while 1:
                g = grp[i]
                memb = False
                for m in g:
                    memb = memb or m in self.solution
                
                if memb == False: # sublist has no members of solution
                    self.solution.insert(elmindex, g[randint(0,len(g)-1)]) # Insert one at random
                i = (i + 1) % len(grp)
                if i == t: break
                
            
            
                
    def swapTweak(self):
            # Only allow disjoint edges
            r1 = 0
            r2 = 0
            while abs(r1-r2)<1:
                r1 = randint(1,len(self.solution))
                r2 = randint(1,len(self.solution))
            #number of elements we wanna swap [r1+i] <=> [r2-i]
            r = int(floor((abs(r1 - r2)-1)/2))
            #swap the elements
            for i in range(1, r):
                temp = self.solution[(r1+i)%len(self.solution)]
                self.solution[(r1+i)%len(self.solution)] = self.solution[(r2-i)%len(self.solution)]
                self.solution[(r2-i)%len(self.solution)] = temp

    def assess(self):
        sum = 0
        for i in range(0,len(self.solution)-1):
            sum += self.distance(self.solution[i], self.solution[(i+1) % len(self.solution)])
        return sum
        
    def distance(self, a, b):
        (xa,ya) = a
        (xb,yb) = b
        return sqrt(abs(xa-xb)**2+abs(ya-yb)**2)        
