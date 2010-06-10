class MetaAlgorithm:
    """
    An algorithm must be initialized with initialize before use.

    The field solution is used to contain the current state of the solutionspace.
    """

    def initialize(self, solutionspace, options, stopevent):
        """ Basic initialization of algorithm before use. """
        self.solutionspace = solutionspace
        self.solutionspace.initialize(options)

        # Set the values
        self.solution = self.solutionspace.getSolution()
        self.solutionval = self.solutionspace.value(self.solution)

        self.stopevent = stopevent

    def execute(self):
        """
        Executes the algorithm, which can be anything, e.g.
            Hill-climbing
            Steepest-ascent hill-climbing
        ..anything that iteratively tweaks the solutionspace
        
        Yield after each improvement (iteration).
        """
        pass
