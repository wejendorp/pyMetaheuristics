from MetaAlgorithm import MetaAlgorithm
import copy
from random import randint

class TabuSearch(MetaAlgorithm):
    """ The algorithm has been initialized into self.solution """
    n = 20
    l = 30
     
    def execute(self):
        self.c = 0
        i = 0
        self.solutionval = self.solution.assess()
        best = self.solution
        bestval = self.solutionval
        self.TabuList = []
#        yield
        while i < 1000:
            self.c += 1
            #Remove old Tabu Entries
            self.TabuList = self.removeOld()
            # Preprocess
            R = copy.deepcopy(self.solution)
            Rtw = R.tweak()
            r = []
            for gfh in range(0,self.n-1):
                r.append(copy.deepcopy(self.solution))
                
            # Algorithm:
            for W in r:
                tw = W.tweak()
                if not self.isTabu(tw) and (W.assess() < R.assess() or self.isTabu(Rtw)):
                    R = W
                    Rtw = tw
                    
            if not self.isTabu(Rtw) and R.assess() < self.solutionval:
                self.solution = R
                self.solutionval = R.assess()
                self.makeTabu(Rtw)
                yield
                
            if bestval > self.solutionval:
                best = self.solution
                bestval = self.solutionval
                i = 0
                continue
            i+=1
        self.solution = best
        self.solutionval = bestval
        yield
        
    def isTabu(self, s):
        for i in s:
            for (x,_) in self.TabuList:
                if i == x:
                    return True
        return False
        
    def makeTabu(self, s):
        self.TabuList.extend([(a, self.c) for a in s])
        #print str(len(self.TabuList)),'elements are Tabu'
        
    def removeOld(self):
        def live((_,age)): return self.c-age < self.l
        return filter(live, self.TabuList)
