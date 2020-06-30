# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:39:56 2020

@author: The Absolute Tinkerer
"""

import math


class Transform:
    def __init__(self, minLat, maxLat, minLong, maxLong, width, height):
        """
        Constructor

        Parameters:
        -----------
        minLat : float
            The minimum latitude documented in the bounds of the OSM file
        maxLat : float
            The maximum latitude documented in the bounds of the OSM file
        minLong : float
            The minimum longitude documented in the bounds of the OSM file
        maxLong : float
            The maximum longitude documented in the bounds of the OSM file
        width : int
            The width of the canvas being drawn on
        height : int
            The height of the canvas being drawn on
        """
        # Bind to class variables
        self._minLat = minLat
        self._maxLat = maxLat
        self._minLong = minLong
        self._maxLong = maxLong
        self._width = width
        self._height = height
        self._xOffset = 0
        self._yOffset = 0

        # Compute the offset values used to center mismatched dimensions that
        # may be experienced
        _maxLat, _minLat = self._lat2y(maxLat), self._lat2y(minLat)
        if (maxLong-minLong)/(_maxLat-_minLat) >= width/height:
            h = width*(_maxLat - _minLat)/(maxLong - minLong)
            self._yOffset = (height - h)/2
        else:
            w = height*(maxLong - minLong)/(_maxLat - _minLat)
            self._xOffset = (width - w)/2

    """
    ###########################################################################
                                Properties
    ###########################################################################
    """
    @property
    def minLat(self):
        return self._minLat

    @property
    def maxLat(self):
        return self._maxLat

    @property
    def minLong(self):
        return self._minLong

    @property
    def maxLong(self):
        return self._maxLong

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def xOffset(self):
        return self._xOffset

    @property
    def yOffset(self):
        return self._yOffset

    """
    ###########################################################################
                                Public Functions
    ###########################################################################
    """
    def convertLat(self, lat):
        """
        Used to convert a latitude to pixels
        """
        _lat = self._lat2y(lat)
        _maxLat, _minLat = self._lat2y(self._maxLat), self._lat2y(self._minLat)
        frac = (_lat - _minLat) / (_maxLat - _minLat)
        h = self._height - 2*self._yOffset
        return h - self._yOffset - frac*h

    def convertLong(self, long):
        """
        Used to convert a longitude to pixels
        """
        frac = (long - self._minLong) / (self._maxLong - self._minLong)
        w = self._width - 2*self._xOffset
        return self._xOffset+frac*w

    """
    ###########################################################################
                                Private Functions
    ###########################################################################
    """
    # See (https://wiki.openstreetmap.org/wiki/Mercator#Python) for info on
    # these functions
    def _y2lat(self, a):
        return 180/math.pi*(2*math.atan(math.exp(a*math.pi/180))-math.pi/2)

    def _lat2y(self, a):
        return 180/math.pi*math.log(math.tan(math.pi/4+a*math.pi/180/2))
