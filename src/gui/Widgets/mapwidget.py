# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:44:56 2020

@author: The Absolute Tinkerer
"""


from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter

import constants as c
from Map import Map
from painter import Painter


class MapWidget(QWidget):
    def __init__(self, parent=None):
        """
        Constructor
        """
        super(MapWidget, self).__init__(parent)

        # Bind class variables
        self._config = None
        self._map = None

    """
    ###########################################################################
                                Built-In Functions
    ###########################################################################
    """
    def paintEvent(self, event):
        """
        """
        super(MapWidget, self).paintEvent(event)

        # Create the painter object and being the painter
        p = QPainter()
        p.begin(self)

        # Draw the map only if a map instance exists
        if self._map is not None:
            self._map.draw(p)
        else:
            self._drawPreloadScreen(p)

    """
    ###########################################################################
                                Public Functions
    ###########################################################################
    """
    def setConfiguration(self, config):
        """
        Public function used to attach the configuration file instance to this
        class. I really don't want conflicting instances.

        Parameters:
        -----------
        config : Configuration
            The configuration instance

        Returns:
        --------
        """
        self._config = config

    def setOSMFile(self, fname):
        """
        Public function used to assign the OSM file we're plotting

        Parameters:
        -----------
        fname : String
            The OSM file name

        Returns:
        --------
        """
        self._map = Map(self.width(), self.height(), fname, self._config)
        self.update()

    def saveImage(self, max_dim, fname):
        """
        """
        # Compute the scale parameter
        t = self._map.getTransform()
        w, h = t.width - 2*t.xOffset, t.height - 2*t.yOffset
        # Clamp height
        if w >= h:
            scale = max_dim/h
            width = max_dim
            height = max_dim*h/w
        # Clamp width
        else:
            scale = max_dim/w
            height = max_dim
            width = max_dim*w/h

        # Instantiate the independent painter object on which we will draw the
        # image
        p = Painter(width, height)

        # Create a new map object from which we'll draw this image
        _map = Map(width, height, self._map.fname, self._config, scale=scale)

        # Actually draw the map
        _map.draw(p)

        # Save the resulting image
        p.saveImage(fname, fname[-3:], 100)

        # Delete the map object
        del _map

    """
    ###########################################################################
                                Private Functions
    ###########################################################################
    """
    def _drawPreloadScreen(self, p):
        """
        Private function used to draw the text centered on the screen
        instructing the user to load an OSM file to begin

        Parameters:
        -----------
        p : QPainter

        Returns:
        --------
        """
        p.fillRect(0, 0, self.width(), self.height(),
                   self._config.getValue(c.CONFIG_BG_COLOR))

        text = 'Load an OSM file to begin!'
        fm = p.fontMetrics()
        w, h = fm.width(text), fm.height()
        p.drawText(self.width()/2-w/2, self.height()/2+h/2, text)
