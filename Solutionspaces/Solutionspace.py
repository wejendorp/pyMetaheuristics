import pickle
import os.path

class Solutionspace:
    solution = []
    def load(self, filename):
        if os.path.isfile(filename):
            print "Attempting to load "+filename
            f = open(filename)
            self.solution = pickle.load(f)
            print "Loaded initialization-file successfully"
        elif filename != "":
            print "Invalid filename given"

	""" Return an initial solution to the problem """
	def initialize(self):
		pass
	
	""" Make a randomized minor change to the solution """
	def tweak(self):
		pass
	
	""" Return a nummeric value for the quality of the solution """
	def assess(self):
		pass
