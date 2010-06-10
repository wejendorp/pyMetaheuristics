from Solutionspace import Solutionspace
from random import *
from math import *
from copy import copy
import os.path

class TravellingCouple(Solutionspace):
    dist = 0.2
    
    def initialize(self, options):
        self.load(options.filename)
        if len(self.initialsolution) == 0:
            self.randomize()
            
        #Figure out which nodes rule out other nodes
        self.groups = []
        sol = self.initialsolution
        for i in range(0,len(sol)):
            self.groups.append([sol[i]])
            for j in range(i,len(sol)):
                if (self.distance(sol[i], sol[j])) < self.dist:
                    self.groups[i].append(sol[j])
                    
        self.solution = self.initialsolution[:]
#        shuffle(self.solution,random)
#	for i in range(0,len(self.solution)):
#		self.dTweak()        

    def randomize(self):
        print "This should be a random space"
        pass

    def tweak(self, solution):
        #perform a D-tweak in 5% of the cases:
        if randint(0,100) <= 4:
            #Distance-tweaks
            return self.dTweak(solution)
        elif randint(0,100) <= 15:
            #Swap edges, and pairs.
            return self.swapTweak(solution)
        else:
            #Move entire sections around
            return self.popTweak(solution)

    def dTweak(self, s):
        #Find an element to remove in the current solution
        i = randint(0,len(self.groups)-1)
        while True:
            if len(self.groups[i]) > 1 and self.groups[i][0] in s:
                break;
            else:
               # print 'dTweakLoop'+str(i)
                i = (i + 1) % len(self.groups)
        # i now points to an element that overlaps another, which is in the graph
        elmindex = s.index(self.groups[i][0])
        elm = s.pop(elmindex)
        def f(x): return elm in x
        grp = filter(f, self.groups)
        # grp is now all clusters including x
        # find a list that has no members of sol and inserts
        i = randint(0,len(grp)-1)
        t = i

        manipulated = [elm]
        while 1:
            g = grp[i]
            memb = False
            #for node in group
            for node in g:
                memb = memb or node in s
            
            if memb == False: # sublist has no members of solution
                ins = g[randint(0,len(g)-1)]
                s.insert(elmindex, ins) # Insert one at random
                manipulated.insert(0,ins)
                
            i = (i + 1) % len(grp)
            if i == t: break
            
        return manipulated                
            
            
                
    def swapTweak(self, s):
            # Only allow disjoint edges
            r1 = 0
            r2 = 0
            while abs(r1-r2)<1:
                r1 = randint(1,len(s)-1)
                r2 = randint(1,len(s)-1)
            #number of elements we wanna swap [r1+i] <=> [r2-i]
            r = int(floor((abs(r1 - r2))/2))
            #Swap two nodes
            if r == 0 or random() < 0.2:
                temp = s[r1]
                s[r1] = s[r2]
                s[r2] = temp
            #swap two edges
            else:
                for i in range(0, r):
                    temp = s[(r1+i)%len(s)]
                    s[(r1+i)%len(s)] = s[(r2-i)%len(s)]
                    s[(r2-i)%len(s)] = temp
                    
            return [s[r1], s[r2]]

    def popTweak(self, s):
        popi = randint(0,len(s)-1)
        count = randint(1,floor(len(s)/2))
        insi = randint(0,(len(s)-1-count)%len(s))
        manipulated = []
        while count > 0:
            pop = s.pop(popi)
            s.insert(insi,pop)
            manipulated.insert(0,pop)
            count-=1
        # Return the manipulated nodes
        return manipulated

    def value(self, s):
        sum = 0
        for i in range(0,len(s)):
            sum += self.distance(s[i], s[(i+1) % len(s)])
        return sum
        
    def distance(self, a, b):
        (xa,ya) = a
        (xb,yb) = b
        return sqrt(abs(xa-xb)**2+abs(ya-yb)**2)        
