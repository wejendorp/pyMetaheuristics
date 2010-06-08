from MetaAlgorithm import MetaAlgorithm
import copy

class SteepestAscent(MetaAlgorithm):
    """ The algorithm has been initialized into self.solution """    
    def execute(self):
        i = 0
        self.solutionval = self.solution.assess()
        best = self.solution
        bestval = self.solutionval
        yield
        while i < 1000:
            r = []
            for gfh in range(0,20):
                r.append(copy.deepcopy(self.solution))
            for s in r:
                s.tweak()
                sval = s.assess()
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
