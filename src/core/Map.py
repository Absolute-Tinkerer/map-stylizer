# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:18:49 2020

@author: The Absolute Tinkerer

This class is used to ingest an Open Source Map (osm extension) file. Map will
render lines (represented by QPen type) and fills (represented by QColor type)
but not points. Relations consist of Ways, which consist of Nodes.
"""

import xml.etree.ElementTree as ET

from PyQt5.QtGui import QPen, QColor, QPainterPath
from PyQt5.QtCore import QPointF

from Transform import Transform

import constants as c


class Node:
    def __init__(self, attrib, transform):
        """
        Constructor
        """
        self._id = int(attrib['id'])
        self._x = transform.convertLong(float(attrib['lon']))
        self._y = transform.convertLat(float(attrib['lat']))

    """
    ###########################################################################
                                    Properties
    ###########################################################################
    """
    @property
    def ID(self):
        return self._id

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Way:
    def __init__(self, parent):
        """
        Constructor
        """
        self._id = int(parent.attrib['id'])
        self._nids = []
        self._tags = {}

        for child in parent:
            if child.tag == 'nd':
                self._nids.append(int(child.attrib['ref']))
            elif child.tag == 'tag':
                key, value = child.attrib['k'], child.attrib['v']
                self._tags[key] = value

    """
    ###########################################################################
                                    Properties
    ###########################################################################
    """
    @property
    def ID(self):
        return self._id

    @property
    def NIDs(self):
        return self._nids

    @property
    def tags(self):
        return self._tags


class Relation:
    def __init__(self, parent):
        """
        Constructor
        """
        self._id = parent.attrib['id']
        self._wids = []
        self._tags = {}

        for child in parent:
            if child.tag == 'member' and child.attrib['type'] == 'way':
                self._wids.append(int(child.attrib['ref']))
            elif child.tag == 'tag':
                key, value = child.attrib['k'], child.attrib['v']
                self._tags[key] = value

    """
    ###########################################################################
                                    Properties
    ###########################################################################
    """
    @property
    def ID(self):
        return self._id

    @property
    def WIDs(self):
        return self._wids

    @property
    def tags(self):
        return self._tags


class Map:
    def __init__(self, width, height, fname, config, scale=1):
        """
        Constructor

        Parameters:
        -----------
        width : int
            The width of the canvas we're displaying to the user; a separate
            width will be used when saving the file
        height : int
            The height of the canvas we're displaying to the user; a
        fname : String
            The OSM file name
        config : Configuration
            The configuration file we use to get all relevant settings
        scale : float
            This determines how much you scale the pen widths. You want the
            output image to look the same as the GUI, so we scale the pen
            widths accordingly
        """
        # Initial variables
        root = ET.parse(fname).getroot()
        transform = None
        nodes = {}
        ways = {}
        relations = {}

        for child in root:
            if child.tag == 'node':
                node = Node(child.attrib, transform)
                nodes[node.ID] = node
            elif child.tag == 'way':
                way = Way(child)
                ways[way.ID] = way
            elif child.tag == 'relation':
                relation = Relation(child)
                relations[relation.ID] = relation
            elif child.tag == 'bounds':
                transform = Transform(float(child.attrib['minlat']),
                                      float(child.attrib['maxlat']),
                                      float(child.attrib['minlon']),
                                      float(child.attrib['maxlon']),
                                      width, height)

        # Bind class variables
        self._copyright = c.COPYRIGHT
        self._attribution = c.ATTRIBUTION
        self._license = c.LICENSE
        self._transform = transform
        self._nodes = nodes
        self._ways = ways
        self._relations = relations

        self._fname = fname
        self._scale = scale
        self._config = config

    """
    ###########################################################################
                                    Properties
    ###########################################################################
    """
    @property
    def Copyright(self):
        return self._copyright

    @property
    def Attribution(self):
        return self._attribution

    @property
    def License(self):
        return self._license

    @property
    def fname(self):
        return self._fname

    """
    ###########################################################################
                                Public Functions
    ###########################################################################
    """
    def setTransform(self, transform):
        """
        """
        self._transform = transform

    def getTransform(self):
        """
        """
        return self._transform

    def draw(self, p):
        """
        p : QPainter
        """
        p.setRenderHint(p.Antialiasing)

        # Simplification variables
        w, h = self._transform.width, self._transform.height
        xo, yo = self._transform.xOffset, self._transform.yOffset

        # Color the background according to the settings file
        p.fillRect(0, 0, w, h, self._config.getValue(c.CONFIG_BG_COLOR))

        # Fill all natural relations
        order = [c.KEY_NATURAL]
        for ID in self._relations.keys():
            rel = self._relations[ID]
            for i, tag in enumerate(order):
                try:
                    if(tag in rel.tags.keys() and self._config.getItemState(
                                      c.DATA_GROUPS[tag][rel.tags[tag]])):
                        self._renderRelation(p, rel, tag)
                except KeyError:
                    # See note in _buildQueue for details
                    s = '* WARNING: tag="%s"; key="%s"' % (tag, rel.tags[tag])
                    s += ' will not render unless manually added!'
                    print(s)

        # build the drawing queue so we don't have multiple for loops
        order = [c.KEY_LANDUSE, c.KEY_WATERWAY, c.KEY_NATURAL, c.KEY_HIGHWAY,
                 c.KEY_BUILDING]
        queue = self._buildQueue(order)

        # Draw the ways from the queue
        for i, tag in enumerate(order):
            for way in queue[i]:
                self._render(p, way, tag)

        # Lastly, color the out of bounds regions white: T, B, L, R
        p.fillRect(0, 0, w, yo, QColor(255, 255, 255))
        p.fillRect(0, h-yo, w, yo, QColor(255, 255, 255))
        p.fillRect(0, 0, xo, h, QColor(255, 255, 255))
        p.fillRect(w-xo, 0, xo, h, QColor(255, 255, 255))

    """
    ###########################################################################
                                Private Functions
    ###########################################################################
    """
    def _buildQueue(self, order):
        """
        Private function used to construct the paint order for elements. This
        will do very basic ordering, and it's recommended to implement a tool
        in the GUI to perform ordering in the future.

        Parameters:
        -----------
        order : String
            The KEY strings that determine in which order painting will be
            completed, with first indices being rendered first

        Returns:
        --------
        queue : List of Way lists
            This will be a 2d array of Ways for each KEY
        """
        queue = [[] for i in range(len(order))]

        for ID in self._ways.keys():
            way = self._ways[ID]

            for i, tag in enumerate(order):
                try:
                    if(tag in way.tags.keys() and self._config.getItemState(
                                           c.DATA_GROUPS[tag][way.tags[tag]])):
                        queue[i].append(way)
                except KeyError:
                    # User will need to add by the following
                    # 1) Create a unique VAL in constants.py
                    # 2) Create a unique CONFIG_STYLE in constants.py
                    # 3) Connect VAL and CONFIG_STYLE in the DATA_GROUPS data
                    #    (constants.py file)
                    # 4) Connect the CONFIG_STYLE to a QPen or QColor in
                    #    configuration.py
                    s = '* WARNING: tag="%s"; key="%s"' % (tag, way.tags[tag])
                    s += ' will not render unless manually added!'
                    print(s)

        return queue

    def _render(self, p, way, tag):
        """
        Private function used to render the Way object passed in. Ways may be
        filled or simply drawn, so the below code checks for a QPen (draw) vs.
        a QColor (fill)

        Parameters:
        -----------
        p : QPainter
            The object with which we're drawing
        way : Way
            The meta object containing drawing information
        tag : String
            The tag string corresponding to 'natural', 'highway', 'waterway',
            etc.

        Returns:
        --------
        """
        # Select the style
        styleKey = c.DATA_GROUPS[tag][way.tags[tag]]
        value = self._config.getValue(styleKey)

        points = []
        for nid in way.NIDs:
            points.append([self._nodes[nid].x,
                           self._nodes[nid].y])

        if type(value) == QPen:
            value.setWidthF(self._scale*value.widthF())
            p.setPen(value)
            path = QPainterPath(QPointF(*points[0]))
            for x, y in points[1:]:
                path.lineTo(QPointF(x, y))
            p.drawPath(path)
        elif type(value) == QColor:
            path = QPainterPath(QPointF(*points[0]))
            for x, y in points[1:-1]:
                path.lineTo(QPointF(x, y))
            path.closeSubpath()
            p.fillPath(path, value)

    def _renderRelation(self, p, relation, tag):
        """
        Private function to render relations. Relations are just different from
        ways that I constructed a separate function for them. Little bit of
        code copy-paste, but not much

        Parameters:
        -----------
        p : QPainter
            The object with which we're drawing
        relation : Relation
            The meta object containing OSM Relation information
        tag : String
            The tag string corresponding to 'natural', 'highway', 'waterway',
            etc.

        Returns:
        --------
        """
        ways = []
        for wid in relation.WIDs:
            # return if we don't have the data for this relation
            # Note, some OSM files don't include all of the ways that are in
            # relations... kinda annoying actually
            if wid in self._ways.keys():
                ways.append(self._ways[wid])
            else:
                return

        # Select the style
        styleKey = c.DATA_GROUPS[tag][relation.tags[tag]]
        value = self._config.getValue(styleKey)
        path = QPainterPath()

        # Trace out the ways using a QPainterPath
        for way in ways:
            points = []
            for nid in way.NIDs:
                points.append([self._nodes[nid].x,
                               self._nodes[nid].y])

            path.moveTo(*points[0])
            for x, y in points[1:]:
                path.lineTo(x, y)
            path.closeSubpath()

        # Draw the ways via the QPainter
        if type(value) == QPen:
            value.setWidthF(self._scale*value.widthF())
            p.setPen(value)
            p.drawPath(path)
        elif type(value) == QColor:
            p.fillPath(path, value)
