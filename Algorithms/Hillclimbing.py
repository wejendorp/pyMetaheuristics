from MetaAlgorithm import MetaAlgorithm

class Hillclimbing(MetaAlgorithm):
    """ The algorithm has been initialized into self.solution """    
    def execute(self):
        i = 0
        yield
        while i < 1000:
            r = self.solution[:]
            self.solutionspace.tweak(r)
            rval = self.solutionspace.value(r)
            if rval < self.solutionval:
                self.solution = r
                self.solutionval = rval
                i = 0
                yield
                continue
            i+=1
