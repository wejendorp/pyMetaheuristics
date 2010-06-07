class Markers:
    """
    Keeps track of markers (colored lines) we want to display to make the
    visualizations more appealing.
    """
    def __init__(self):
        self.linemarkers = {}
        self.pointmarkers = {}
        self.verticalmarkers = {}
        self.id = 0

    def addPointMarker(self, index, color):
        """
        Adds a marker for the given point to our collection.
        
        Parameters:
        - index (int): Index of the point that should be recolored.
        - color (color): The color the marker is to have on the display.
                         Should be passed as a RGB-tuple; e.g. (255, 0, 0) = red.

        Returns an the id of the marker created, to be used for modifying/removing the marker at a later point in time.
        """
        self.id += 1

        marker = { 'id': self.id,
                   'index': index,
                   'color': color }

        self.pointmarkers[self.id] = marker

        return self.id

    def addLineMarker(self, start, end, color):
        """
        Adds a marker for a line to our collection.
        
        Parameters:
        - start (int): Index of the start point of the line.
        - end (int): Index of the end point of the line.
        - color (color): The color the marker is to have on the display.
                         Should be passed as a RGB-tuple; e.g. (255, 0, 0) = red.

        Returns an the id of the marker created, to be used for modifying/removing the marker at a later point in time.
        """
        self.id += 1

        marker = { 'id': self.id,
                   'type': 'line',
                   'start': start,
                   'end': end,
                   'color': color }

        self.linemarkers[self.id] = marker

        return self.id

    def addVerticalMarker(self, x, color):
        """
        Draws a vertical line of the form x = t, for some t.
        
        Parameters:
        - x (float): x-coordinate to draw the line in.
        - color (color): The color the marker is to have on the display.
                         Should be passed as a RGB-tuple; e.g. (255, 0, 0) = red.

        Returns an the id of the marker created, to be used for modifying/removing the marker at a later point in time.
        """
        self.id += 1

        marker = { 'id': self.id,
                   'type': 'vertical',
                   'x': x,
                   'color': color }

        self.verticalmarkers[self.id] = marker

        return self.id

    def movePointMarker(self, id, index):
        """ Moves the point marker with the given id to the given index. """
        self.pointmarkers[id]['index'] = index

    def moveLineMarker(self, id, start, end):
        """ Moves the line marker with the given id to the given position. """
        self.linemarkers[id]['start'] = start
        self.linemarkers[id]['end'] = end

    def moveVerticalMarker(self, id, x):
        """ Moves the vertical line marker with the given id to the given x-coordinate. """
        self.verticalmarkers[id]['x'] = x

    def changePointMarkerColor(self, id, color):
        """ Changes the color of the given marker. """
        self.pointmarkers[id]['color'] = color

    def changeLineMarkerColor(self, id, color):
        """ Changes the color of the given marker. """
        self.linemarkers[id]['color'] = color

    def changeVerticalMarkerColor(self, id, color):
        """ Changes the color of the given marker. """
        self.verticalmarkers[id]['color'] = color

    def removePointMarker(self, id):
        """ Removes the point marker with the given id. """
        del self.pointmarkers[id]

    def removeLineMarker(self, id):
        """ Removes the line marker with the given id. """
        del self.linemarkers[id]

    def removeVerticalMarker(self, id):
        """ Removes the vertical marker with the given id. """
        del self.verticalmarkers[id]


