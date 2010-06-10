from MetaAlgorithm import MetaAlgorithm
import copy

class SteepestAscent(MetaAlgorithm):
    """ The algorithm has been initialized into self.solution """    
    def execute(self):
        i = 0
        best = self.solution
        bestval = self.solutionval
        yield
        while i < 1000:
            r = []
            for gfh in range(0,20):
                r.append(self.solution[:])
            for s in r:
                self.solutionspace.tweak(s)
                sval = self.solutionspace.value(s)
                if sval < bestval:
                    best = s
                    bestval = sval
               
            if bestval < self.solutionval:
                self.solution = best
                self.solutionval = bestval
                i = 0
                yield
                continue
            i+=1

