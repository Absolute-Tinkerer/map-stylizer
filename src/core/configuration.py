# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:40:26 2020

@author: The Absolute Tinkerer

If the user wishes to add additional layers, they must include the CONFIG_STYLE
connected with the appropriate QPen or QColor in the _initConfig function
"""

import os
import json

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QPen

import constants as c


class Configuration:
    def __init__(self, fname=c.FILE_CONFIG):
        """
        Constructor for the user configuration file initialization
        """
        self._fname = fname

        if os.path.exists(fname):
            # When reading the config, we read the objects into the init fields
            # and if the file doesn't have all the fields the init has, those
            # new values will be added. This assures backward compatibility
            # AS LONG AS existing keys and values aren't altered. This only
            # addresses new items.
            self._read()
        else:
            self._initConfig()

    """
    ###########################################################################
                                Public Functions
    ###########################################################################
    """
    def getValue(self, item):
        """
        Function used to get the value of a particular item

        Parameters:
        -----------
        item : String
            String used in the _config dict for a value

        Returns:
        --------
        <value> : Object
            The value of the dict's item
        """
        item = self._config[item]
        if item[0] == c.CONFIG_TYPE_QCOLOR:
            return QColor(*item[2:])
        elif item[0] == c.CONFIG_TYPE_QPEN:
            color = QColor(*item[2:6])
            return QPen(color, *item[6:])
        return self._config[item]

    def setValue(self, item, value):
        """
        Function used to set the value of a particular item

        Parameters:
        -----------
        item : String
            String used in the _config dict for a value
        value : Object
            The new value of the dict's item

        Returns:
        --------
        """
        if type(value) == QColor:
            r, g, b = value.red(), value.green(), value.blue()
            a = value.alpha()

            state = self._config[item][1]
            self._config[item] = [c.CONFIG_TYPE_QCOLOR, state, r, g, b, a]
            self._write()
        elif type(value) == QPen:
            color = value.brush().color()
            r, g, b = color.red(), color.green(), color.blue()
            a = color.alpha()
            state = self._config[item][1]

            self._config[item] = [c.CONFIG_TYPE_QPEN, state, r, g, b, a,
                                  value.widthF(), value.style(),
                                  value.capStyle(), value.joinStyle()]
            self._write()
        else:
            raise Exception('setValue value type not correct!\nRequired: %s,' +
                            ' Received: %s' % (type(self._config[item]),
                                               type(value)))

    def getItemState(self, item):
        """
        Function used to get the state of a particular item

        Parameters:
        -----------
        item : String
            String used in the _config dict for a value

        Returns:
        --------
        <value> : boolean
            The state of the dict's item
        """
        return self._config[item][1]

    def setItemState(self, item, state):
        """
        Function used to set the state of a particular item

        Parameters:
        -----------
        item : String
            String used in the _config dict for a value
        state : boolean
            The new state of the dict's item

        Returns:
        --------
        """
        self._config[item][1] = state
        self._write()

    def getConfig(self):
        """
        Function used to get the configuration dict object

        Parameters:
        -----------

        Returns:
        --------
        <value> : dict
            The configuration dict object
        """
        return self._config

    def setConfig(self, newConfig):
        """
        Function used to set the configuration dict object and write the new
        configuration to file

        Parameters:
        -----------
        newConfig : dict
            The new configuration dict object

        Returns:
        --------
        """
        self._config = newConfig
        self._write()

    """
    ###########################################################################
                                Private Functions
    ###########################################################################
    """
    def _initConfig(self):
        """
        Private function used to initialize the configuration

        Parameters:
        -----------
        Returns:
        --------
        """
        self._config = {
            c.CONFIG_BG_COLOR: [c.CONFIG_TYPE_QCOLOR, True, 20, 20, 20, 255],

            c.CONFIG_STYLE_MOTORWAY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 50, 255,
                                10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TRUNK: [
                                c.CONFIG_TYPE_QPEN, True, 255, 100, 50, 255,
                                10, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PRIMARY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 150, 50, 255,
                                5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_SECONDARY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 100, 255,
                                5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TERTIARY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_UNCLASSIFIED: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_RESIDENTIAL: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_LINK_MOTORWAY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 50, 50, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_LINK_TRUNK: [
                                c.CONFIG_TYPE_QPEN, True, 255, 100, 50, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_LINK_PRIMARY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 150, 50, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_LINK_SECONDARY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 100, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_LINK_TERTIARY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_STREET: [
                                c.CONFIG_TYPE_QPEN, True, 200, 200, 200, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_SERVICE: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PEDESTRIAN: [
                                c.CONFIG_TYPE_QPEN, True, 150, 150, 150, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TRACK: [
                                c.CONFIG_TYPE_QPEN, True, 155, 113, 30, 255,
                                1, Qt.DashDotLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_BUS_GUIDEWAY: [
                                c.CONFIG_TYPE_QPEN, True, 100, 100, 255, 255,
                                1, Qt.DashLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_ESCAPE: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_RACEWAY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 192, 202, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_ROAD: [
                                c.CONFIG_TYPE_QPEN, True, 125, 125, 125, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_FOOTWAY: [
                                c.CONFIG_TYPE_QPEN, True, 247, 218, 218, 255,
                                1, Qt.DotLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_BRIDLEWAY: [
                                c.CONFIG_TYPE_QPEN, True, 13, 134, 13, 255,
                                1, Qt.DashLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_STEPS: [
                                c.CONFIG_TYPE_QPEN, True, 249, 104, 92, 255,
                                1, Qt.DashLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_CORRIDOR: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PATH: [
                                c.CONFIG_TYPE_QPEN, True, 247, 218, 218, 255,
                                1, Qt.DotLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_CYCLEWAY: [
                                c.CONFIG_TYPE_QPEN, True, 49, 49, 253, 255,
                                1, Qt.DotLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PROPOSED: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_CONSTRUCTION: [
                                c.CONFIG_TYPE_QPEN, True, 100, 100, 200, 255,
                                1, Qt.DashLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_BUS_STOP: [
                                c.CONFIG_TYPE_QPEN, True, 255, 0, 0, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_CROSSING: [
                                c.CONFIG_TYPE_QPEN, True, 55, 184, 33, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_ELEVATOR: [
                                c.CONFIG_TYPE_QPEN, True, 31, 170, 186, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_EMERG_POINT: [
                                c.CONFIG_TYPE_QPEN, True, 255, 0, 0, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_GIVE_WAY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_MILESTONE: [
                                c.CONFIG_TYPE_QPEN, True, 0, 185, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_MINI_ROUNDABOUT: [
                                c.CONFIG_TYPE_QPEN, True, 205, 128, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_MOTORWAY_JUNC: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PASSING_PLACE: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PLATFORM: [
                                c.CONFIG_TYPE_QPEN, True, 205, 128, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_REST_AREA: [
                                c.CONFIG_TYPE_QPEN, True, 80, 80, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_SPEED_CAMERA: [
                                c.CONFIG_TYPE_QPEN, True, 255, 0, 0, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_STREET_LAMP: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_SERVICES: [
                                c.CONFIG_TYPE_QPEN, True, 80, 80, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_STOP: [
                                c.CONFIG_TYPE_QPEN, True, 255, 0, 0, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TRAFFIC_MIRROR: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TRAFFIC_SIGNAL: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TRAILHEAD: [
                                c.CONFIG_TYPE_QPEN, True, 205, 128, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TURNING_CIRCLE: [
                                c.CONFIG_TYPE_QPEN, True, 205, 128, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TURNING_LOOP: [
                                c.CONFIG_TYPE_QPEN, True, 205, 128, 50, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TOLL_GANTRY: [
                                c.CONFIG_TYPE_QPEN, True, 80, 80, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],

            c.CONFIG_STYLE_RIVER: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_RIVERBANK: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 211, 223, 255],
            c.CONFIG_STYLE_STREAM: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                5, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TIDAL_CHANNEL: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_CANAL: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PRESSURIZED: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_DRAIN: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_DITCH: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_FAIRWAY: [
                                c.CONFIG_TYPE_QPEN, True, 255, 255, 255, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_ARTIFICIAL: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_DERELICT: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_DOCK: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 211, 223, 255],
            c.CONFIG_STYLE_BOATYARD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 211, 223, 255],
            c.CONFIG_STYLE_DAM: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_WEIR: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_FUEL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 211, 223, 255],
            c.CONFIG_STYLE_LOCK_GATE: [
                                c.CONFIG_TYPE_QPEN, True, 170, 211, 223, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],

            c.CONFIG_STYLE_WOOD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                157, 202, 138, 255],
            c.CONFIG_STYLE_TREE_ROW: [
                                c.CONFIG_TYPE_QPEN, True, 157, 202, 138, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_TREE: [
                                c.CONFIG_TYPE_QPEN, True, 157, 202, 138, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_SCRUB: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                200, 215, 171, 255],
            c.CONFIG_STYLE_HEATH: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                214, 217, 159, 255],
            c.CONFIG_STYLE_MOOR: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                211, 210, 165, 255],
            c.CONFIG_STYLE_GRASS: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                205, 235, 176, 255],
            c.CONFIG_STYLE_GRASSLAND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                205, 235, 176, 255],
            c.CONFIG_STYLE_FELL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                174, 222, 126, 255],
            c.CONFIG_STYLE_BARE_ROCK: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                213, 209, 204, 255],
            c.CONFIG_STYLE_SCREE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                237, 228, 220, 255],
            c.CONFIG_STYLE_SHINGLE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                231, 223, 216, 255],
            c.CONFIG_STYLE_SAND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                238, 226, 192, 255],
            c.CONFIG_STYLE_MUD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                227, 219, 211, 255],
            c.CONFIG_STYLE_WATER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                166, 198, 198, 255],
            c.CONFIG_STYLE_WETLAND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                27, 139, 97, 255],
            c.CONFIG_STYLE_GLACIER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                221, 236, 236, 255],
            c.CONFIG_STYLE_BAY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                166, 198, 198, 255],
            c.CONFIG_STYLE_CAPE: [
                                c.CONFIG_TYPE_QPEN, True, 166, 198, 198, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_STRAIT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                166, 198, 198, 255],
            c.CONFIG_STYLE_BEACH: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                255, 241, 186, 255],
            c.CONFIG_STYLE_COASTLINE: [
                                c.CONFIG_TYPE_QPEN, True, 237, 234, 226, 255,
                                1, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_REEF: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                202, 193, 170, 255],
            c.CONFIG_STYLE_SPRING: [
                                c.CONFIG_TYPE_QPEN, True, 166, 198, 198, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_HOT_SPRING: [
                                c.CONFIG_TYPE_QPEN, True, 203, 172, 169, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_GEYSER: [
                                c.CONFIG_TYPE_QPEN, True, 166, 198, 198, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_MTN_RANGE: [
                                c.CONFIG_TYPE_QPEN, True, 208, 143, 85, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_PEAK: [
                                c.CONFIG_TYPE_QPEN, True, 208, 143, 85, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_DUNE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                255, 241, 186, 255],
            c.CONFIG_STYLE_HILL: [
                                c.CONFIG_TYPE_QPEN, True, 205, 235, 176, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_VOLCANO: [
                                c.CONFIG_TYPE_QPEN, True, 212, 0, 0, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_VALLEY: [
                                c.CONFIG_TYPE_QPEN, True, 63, 150, 100, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_RIDGE: [
                                c.CONFIG_TYPE_QPEN, True, 208, 143, 85, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_ARETE: [
                                c.CONFIG_TYPE_QPEN, True, 208, 143, 85, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_CLIFF: [
                                c.CONFIG_TYPE_QPEN, True, 208, 143, 85, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_SADDLE: [
                                c.CONFIG_TYPE_QPEN, True, 208, 143, 85, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_ISTHMUS: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                255, 241, 186, 255],
            c.CONFIG_STYLE_PENINSULA: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                37, 175, 106, 255],
            c.CONFIG_STYLE_ROCK: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                208, 143, 85, 255],
            c.CONFIG_STYLE_STONE: [
                                c.CONFIG_TYPE_QPEN, True, 223, 208, 191, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],
            c.CONFIG_STYLE_SINKHOLE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                255, 241, 186, 255],
            c.CONFIG_STYLE_CAVE_ENTRANCE: [
                                c.CONFIG_TYPE_QPEN, True, 30, 30, 30, 255,
                                2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin],

            c.CONFIG_STYLE_COMMERCIAL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                238, 207, 207, 255],
            c.CONFIG_STYLE_CONSTRUCTION_LU: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                199, 199, 180, 255],
            c.CONFIG_STYLE_INDUSTRIAL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                230, 209, 227, 255],
            c.CONFIG_STYLE_RESIDENTIAL_LU: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                218, 218, 218, 255],
            c.CONFIG_STYLE_RETAIL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                254, 202, 197, 255],
            c.CONFIG_STYLE_ALLOTMENTS: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                201, 225, 191, 255],
            c.CONFIG_STYLE_FARMLAND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                238, 240, 213, 255],
            c.CONFIG_STYLE_FARM: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                238, 240, 213, 255],
            c.CONFIG_STYLE_FARMYARD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                234, 204, 164, 255],
            c.CONFIG_STYLE_FOREST: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                157, 202, 138, 255],
            c.CONFIG_STYLE_MEADOW: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                205, 235, 176, 255],
            c.CONFIG_STYLE_ORCHARD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                158, 220, 144, 255],
            c.CONFIG_STYLE_VINEYARD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                158, 220, 144, 255],
            c.CONFIG_STYLE_GARDEN: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                158, 220, 144, 255],
            c.CONFIG_STYLE_BASIN: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 211, 223, 255],
            c.CONFIG_STYLE_BROWNFIELD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                167, 168, 126, 255],
            c.CONFIG_STYLE_CEMETERY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 203, 175, 255],
            c.CONFIG_STYLE_CONSERVATION: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                197, 236, 148, 255],
            c.CONFIG_STYLE_DEPOT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                214, 214, 193, 255],
            c.CONFIG_STYLE_GARAGE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                214, 214, 193, 255],
            c.CONFIG_STYLE_GARAGES: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                214, 214, 193, 255],
            c.CONFIG_STYLE_TRAF_ISLAND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                230, 209, 227, 255],
            c.CONFIG_STYLE_GRASS_LU: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                197, 236, 148, 255],
            c.CONFIG_STYLE_GREENFIELD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                241, 238, 232, 255],
            c.CONFIG_STYLE_GH_HORT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                238, 240, 213, 255],
            c.CONFIG_STYLE_LANDFILL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                167, 168, 126, 255],
            c.CONFIG_STYLE_MILITARY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                243, 228, 222, 255],
            c.CONFIG_STYLE_PEAT_CUTTING: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                181, 229, 170, 255],
            c.CONFIG_STYLE_PLANT_NURSERY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                181, 229, 170, 255],
            c.CONFIG_STYLE_PORT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                166, 198, 198, 255],
            c.CONFIG_STYLE_QUARRY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                183, 181, 181, 255],
            c.CONFIG_STYLE_RAILWAY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                230, 209, 227, 255],
            c.CONFIG_STYLE_REC_GROUND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                223, 252, 226, 255],
            c.CONFIG_STYLE_RELIGIOUS: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                205, 204, 201, 255],
            c.CONFIG_STYLE_CHURCHYARD: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                205, 204, 201, 255],
            c.CONFIG_STYLE_RESERVOIR: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 211, 223, 255],
            c.CONFIG_STYLE_RES_WTSHED: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                129, 189, 207, 255],
            c.CONFIG_STYLE_SALT_POND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                170, 211, 223, 255],
            c.CONFIG_STYLE_VILLAGE_GREEN: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                205, 235, 176, 255],
            c.CONFIG_STYLE_VACANT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                200, 200, 200, 255],
            c.CONFIG_STYLE_YES_LU: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                200, 200, 200, 255],
            c.CONFIG_STYLE_GOVERNMENT_LU: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                200, 200, 200, 255],

            c.CONFIG_STYLE_APARTMENTS: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_INDOOR: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CONDOMINIUM: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CONDOMINIUM_2: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TOWER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_AMPHITHEATRE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_BUNGALOW: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CABIN: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_DETACHED: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_DORMITORY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_FARM_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HOTEL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HOUSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HOUSEBOAT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_RESID_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SD_HOUSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_STATIC_CARAVAN: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TERRACE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_COMM_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_INDUSTRIAL_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_MANUFACTURE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_KIOSK: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_OFFICE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_RETAIL_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SHOP: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SUPERMARKET: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_WAREHOUSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CATHEDRAL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CHAPEL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CHURCH: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_MOSQUE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_RELIGIOUS_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SHRINE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SYNAGOGUE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TEMPLE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_BAKEHOUSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CIVIC: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GYM: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CANOPY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SHELTER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_BURIAL_VAULT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],

            c.CONFIG_STYLE_PART: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_COLLEGE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HEALTH: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HOTEL_2: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_MULTIPURPOSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_FIRE_STATION: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GOVERNMENT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GOVERNEMENT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SUBWAY_ENTRY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_LIBRARY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HOSPITAL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_KINDERGARTEN: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_PUBLIC: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SCHOOL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TOILETS: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TRAIN_STATION: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TRANSPORTATION: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_UNIVERSITY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_BARN: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CONSERVATORY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_COWSHED: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_FARM_AUXILIARY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GREENHOUSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SLURRY_TANK: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_STABLE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_STY: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GRANDSTAND: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_PAVILION: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_RIDING_HALL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SPORTS_HALL: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_STADIUM: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HANGAR: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_HUT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SHED: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CARPORT: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GARAGE_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GARAGES_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_PARKING: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_DIGESTER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_SERVICE_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TRANSF_TOWER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_WATER_TOWER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_BUNKER: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_BRIDGE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_CONSTR_BLDG: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_GATEHOUSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_ROOF: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_RUINS: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_TREE_HOUSE: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_YES: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_NO: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255],
            c.CONFIG_STYLE_UNDEF: [
                                c.CONFIG_TYPE_QCOLOR, True,
                                140, 140, 140, 255]
            }

        self._write()

    def _write(self):
        """
        Private function used to write the user configuration to the
        user.config file

        Parameters:
        -----------
        Returns:
        --------
        """
        # Write to file
        with open(self._fname, 'w') as outfile:
            json.dump(self._config, outfile)

    def _read(self):
        """
        Private function used to read the user configuration from the
        user.config file

        Parameters:
        -----------
        Returns:
        --------
        """
        # Load the user configuration
        with open(self._fname) as f:
            temp = json.load(f)

        # Now load the initial config
        self._initConfig()

        # Transfer the temp values to the initial config object
        for key in temp.keys():
            if key in self._config.keys():
                # If a key doesn't exist anymore, then we ignore it
                # This also ensures initialization of new values
                self._config[key] = temp[key]

        # Now write the config back to file
        self._write()
