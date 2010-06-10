import pickle
import os.path

class Solutionspace:
    solution = []
    def load(self, filename):
        if os.path.isfile(filename):
            #print "Attempting to load "+filename
            f = open(filename)
            self.initialsolution = pickle.load(f)
            f.close()
            #print "Loaded initialization-file successfully"
        elif filename != "":
            print "Invalid filename given"

	""" Return an initial solution to the problem """
	def initialize(self):
		pass
	
	""" Make a randomized minor change to the solution """
	def tweak(self, solution):
		pass
	
	""" Return a nummeric value for the quality of the solution """
	def value(self):
		pass
		
    def getSolution(self):
        return self.solution
