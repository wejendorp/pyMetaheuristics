class MetaAlgorithm:
    """
    An algorithm must be initialized with initialize before use.

	The field solution is used to contain the current state of the solutionspace.
    """

    def initialize(self, solutionspace, options):
        """ Basic initialization of algorithm before use. """
        self.solution = solutionspace
        self.solution.initialize(options)

    def execute(self):
        """
		Executes the algorithm, which can be anything, e.g.
			Hill-climbing
			Steepest-ascent hill-climbing
		..anything that iteratively tweaks the solutionspace
		
		Yield after each improvement (iteration).
        """
        pass
        
    def value(self):
    	return self.solution.assess()
    	
    def solution(self):
        return self.solution.getsolution()
