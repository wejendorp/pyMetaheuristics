from MetaAlgorithm import MetaAlgorithm
import copy

class Hillclimbing(MetaAlgorithm):
    """ The algorithm has been initialized into self.solution """    
    def execute(self):
        i = 0
        self.solutionval = self.solution.assess()
        yield
        while i < 1000:
            r = copy.deepcopy(self.solution)
            r.tweak()
            rval = r.assess()
            if rval < self.solutionval:
                self.solution = r
                self.solutionval = rval
                i = 0
                yield
                continue
            i+=1
