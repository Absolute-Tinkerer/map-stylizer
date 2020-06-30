# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:45:40 2019

@author: The Absolute Tinkerer
"""

from PyQt5.QtGui import QPainter, QPixmap, QColor
from PyQt5.QtCore import Qt


class Painter(QPainter):
    def __init__(self, width, height):
        """
        Constructor
        """
        super(Painter, self).__init__()

        # Create the image upon which we're going to draw
        self.image = QPixmap(width, height)
        self.bg_color = QColor(255, 255, 255, 255)

        self.image.fill(Qt.transparent)

        # Begin the drawing on the image
        self.begin(self.image)

        self.fillRect(0, 0, width, height, self.bg_color)

    def saveImage(self, fileName, fmt=None, quality=-1):
        """
        """
        return self.image.save(fileName, fmt, quality)

    def pixmap(self):
        """
        Give the pixmap to the user
        """
        return self.image
