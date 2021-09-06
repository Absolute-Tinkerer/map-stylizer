# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 15:57:36 2020

@author: The Absolute Tinkerer
"""

from PyQt5.QtWidgets import QMainWindow, QPushButton, QTreeWidget
from PyQt5.QtWidgets import QDoubleSpinBox, QTreeWidgetItem, QColorDialog
from PyQt5.QtWidgets import QWidget, QFileDialog, QLabel, QComboBox

from PyQt5.QtGui import QIcon, QPen, QColor

from PyQt5.QtCore import Qt

from shutil import copyfile

from MainWindowUI import Ui_MainWindow

import constants as c

from configuration import Configuration


class MainWindowHandlers(QMainWindow):
    def __init__(self):
        """
        Constructor
        """
        QMainWindow.__init__(self)

        # Assign the UI file to this window and maximize
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.showMaximized()

        # Set the window icon
        self.setWindowIcon(QIcon(c.FILE_ICON))

    """
    ###########################################################################
                                Public Functions
    ###########################################################################
    """
    def initialize(self):
        """
        Public function called upon program start to ensure we assign GUI
        elements to class variables. This cannot be done in the constructor!

        Parameters:
        -----------
        Returns:
        --------
        """
        # Bind widgets to class variables
        self._initWidgets()

        # Bind other class variables
        self._config = Configuration()

        # Finalize the widgets' appearance using the config file
        self._configWidgets()

    """
    ###########################################################################
                                Slot Functions
    ###########################################################################
    """
    def bgColorBtnClicked(self):
        """
        Button to set the background color has been clicked
        """
        color = self._colorPicker(self._config.getValue(c.CONFIG_BG_COLOR))

        # If the user cancels out
        if not color.isValid():
            return

        # Update the button background, save to the config file, and update
        # the map widget
        self._setButtonColor(self._btn_bg_color, color)
        self._config.setValue(c.CONFIG_BG_COLOR, color)

    def lineColorBtnClicked(self):
        """
        Button to set the selected line color clicked
        """
        if not self._tree_line.selectedItems():
            return
        item = self._tree_line.selectedItems()[0]
        text, ptext = item.text(0), item.parent().text(0)
        pen = self._config.getValue(c.DATA_GROUPS[ptext][text])

        color = self._colorPicker(pen.color())

        # if the user cancels out
        if not color.isValid():
            return

        # Update the config file, button color
        pen.setColor(color)
        self._setButtonColor(self._btn_line, color)
        self._config.setValue(c.DATA_GROUPS[ptext][text], pen)

    def lineWidthChanged(self, value):
        """
        The user has changed the width of the selected line
        """
        if not self._tree_line.selectedItems():
            return

        item = self._tree_line.selectedItems()[0]
        text, ptext = item.text(0), item.parent().text(0)
        pen = self._config.getValue(c.DATA_GROUPS[ptext][text])

        # Update the pen, map, and the config file
        pen.setWidthF(value)
        self._config.setValue(c.DATA_GROUPS[ptext][text], pen)
        self._map.update()

    def lineComboChanged(self, value):
        """
        The user has changed the selected item's line style combo box
        """
        if not self._tree_line.selectedItems():
            return
        item = self._tree_line.selectedItems()[0]
        text, ptext = item.text(0), item.parent().text(0)
        pen = self._config.getValue(c.DATA_GROUPS[ptext][text])

        # Update the pen, map, and the config file
        lStyle = list(c.DICT_QPEN_STYLE.keys())[
                                 list(c.DICT_QPEN_STYLE.values()).index(value)]
        pen.setStyle(lStyle)
        self._config.setValue(c.DATA_GROUPS[ptext][text], pen)
        self._map.update()

    def capComboChanged(self, value):
        """
        The user has changed the selected item's line cap combo box
        """
        if not self._tree_line.selectedItems():
            return
        item = self._tree_line.selectedItems()[0]
        text, ptext = item.text(0), item.parent().text(0)
        pen = self._config.getValue(c.DATA_GROUPS[ptext][text])

        # Update the pen, map, and the config file
        cStyle = list(c.DICT_QPEN_CAP.keys())[
                                   list(c.DICT_QPEN_CAP.values()).index(value)]
        pen.setCapStyle(cStyle)
        self._config.setValue(c.DATA_GROUPS[ptext][text], pen)
        self._map.update()

    def joinComboChanged(self, value):
        """
        The user has changed the selected item's join combo box
        """
        if not self._tree_line.selectedItems():
            return
        item = self._tree_line.selectedItems()[0]
        text, ptext = item.text(0), item.parent().text(0)
        pen = self._config.getValue(c.DATA_GROUPS[ptext][text])

        # Update the pen and the config file
        jStyle = list(c.DICT_QPEN_JOIN.keys())[
                                  list(c.DICT_QPEN_JOIN.values()).index(value)]
        pen.setJoinStyle(jStyle)
        self._config.setValue(c.DATA_GROUPS[ptext][text], pen)

    def fillColorBtnClicked(self):
        """
        Button to set the selected fill color clicked
        """
        if not self._tree_fill.selectedItems():
            return
        item = self._tree_fill.selectedItems()[0]
        text, ptext = item.text(0), item.parent().text(0)
        color = self._colorPicker(self._config.getValue(
                                                   c.DATA_GROUPS[ptext][text]))

        # if the user cancels out
        if not color.isValid():
            return

        # Update the config file, button color
        self._setButtonColor(self._btn_fill, color)
        self._config.setValue(c.DATA_GROUPS[ptext][text], color)

    def checkboxChanged(self, item, idx):
        """
        The user has changed an item's checked state
        """
        text = item.text(0)
        state = text not in c.DATA_GROUPS.keys()

        if state:
            ptext = item.parent().text(0)
            state = item.checkState(0) == Qt.Checked
            self._config.setItemState(c.DATA_GROUPS[ptext][text], state)

            # Update the map
            self._map.update()

    def loadOSMFile(self):
        """
        The user has clicked the button to load an OSM file
        """
        fileName, _ = QFileDialog.getOpenFileName(
                  self, 'Open OSM File', 'data', 'OpenStreetMap Files (*.osm)')

        if not fileName:
            return

        # Create the map object
        self._map.setOSMFile(fileName)

        # Enable all settings fields
        self._tree_line.setEnabled(True)
        self._tree_fill.setEnabled(True)
        self._btn_save.setEnabled(True)
        self._btn_reset.setEnabled(True)
        self._btn_load_settings.setEnabled(True)

        # Select the first item
        self._tree_line.topLevelItem(0).setSelected(True)
        self._tree_fill.topLevelItem(0).setSelected(True)

        # Update the lists so we capture a config file's changes
        self._current_file_tags = self._map.getMap().getAllTags()
        self._refreshLists()

        # Force the item metadata fields to update
        self.lineSelChanged()
        self.fillSelChanged()

        # Update the map
        self._map.update()

    def saveImage(self):
        """
        The user has clicked the button to save the map as an image
        """
        fileName, _ = QFileDialog.getSaveFileName(
                           self, 'Save Image', 'output', 'Image Files (*.jpg)')

        if fileName:
            self._map.saveImage(self._box_max_dim.value(), fileName)

            # Copy the user config file to reflect the user's settings for the
            # image
            fileName = fileName.split('/')[-1]
            dst = '%s/%s.%s' % (c.FOLDER_USER_CONFIGS, fileName[:-4],
                                c.FILE_CONFIG.split('.')[1])
            copyfile(c.FILE_CONFIG, dst)

    def resetBtnClicked(self):
        """
        The user has clicked the button to reset the map to the default
        configuration
        """
        # Reset the configuration file
        self._config._initConfig()

        self._refreshLists()

        # Force the item metadata fields to update
        self.lineSelChanged()
        self.fillSelChanged()

        # Update the map
        self._map.update()

    def loadSettingsClicked(self):
        """
        The user has clicked the button to load a pre-defined configuration
        file
        """
        fileName, _ = QFileDialog.getOpenFileName(
                 self, 'Set Config File', 'configs', 'Config Files (*.config)')

        if fileName:
            # Overwrite the existing config file
            copyfile(fileName, c.FILE_CONFIG)

            # Rebuild the config file
            self._config._read()

            # Update the lists
            self._refreshLists()

            # Force the item metadata fields to update
            self.lineSelChanged()
            self.fillSelChanged()

            # Update the map
            self._map.update()

    def lineSelChanged(self):
        """
        The user has changed which line item is selected
        """
        if not self._tree_line.selectedItems():
            return
        item = self._tree_line.selectedItems()[0]

        text = item.text(0)
        state = text not in c.DATA_GROUPS.keys()

        # Enable / disable the configuration edit field
        self._label_line.setEnabled(state)
        self._btn_line.setEnabled(state)
        self._box_line.setEnabled(state)
        self._combo_line.setEnabled(state)
        self._combo_cap.setEnabled(state)
        self._combo_join.setEnabled(state)

        # Populate the metadata fields
        if state:
            self._blockAllSignals(True)

            self._label_line.setText(text)
            ptext = item.parent().text(0)
            pen = self._config.getValue(c.DATA_GROUPS[ptext][text])
            self._setButtonColor(self._btn_line, pen.color())

            self._box_line.setValue(pen.widthF())

            idx = self._combo_line.findText(c.DICT_QPEN_STYLE[pen.style()])
            self._combo_line.setCurrentIndex(idx)
            idx = self._combo_cap.findText(c.DICT_QPEN_CAP[pen.capStyle()])
            self._combo_cap.setCurrentIndex(idx)
            idx = self._combo_join.findText(c.DICT_QPEN_JOIN[pen.joinStyle()])
            self._combo_join.setCurrentIndex(idx)

            self._blockAllSignals(False)

    def fillSelChanged(self):
        """
        The user has changed which fill item is selected
        """
        if not self._tree_fill.selectedItems():
            return
        item = self._tree_fill.selectedItems()[0]

        text = item.text(0)
        state = text not in c.DATA_GROUPS.keys()

        # Enable / disable the configuration edit field
        self._label_fill.setEnabled(state)
        self._btn_fill.setEnabled(state)

        # Populate the metadata fields
        if state:
            self._blockAllSignals(True)

            self._label_fill.setText(text)
            ptext = item.parent().text(0)
            color = self._config.getValue(c.DATA_GROUPS[ptext][text])
            self._setButtonColor(self._btn_fill, color)

            self._blockAllSignals(False)

    """
    ###########################################################################
                                Private Functions
    ###########################################################################
    """
    def _initWidgets(self):
        """
        Private function used to bind the GUI elements to class variables so
        we can work with them

        Parameters:
        -----------
        Returns:
        --------
        """
        # QLabels
        self._label_line = self.findChild(QLabel, 'label_line')
        self._label_fill = self.findChild(QLabel, 'label_fill')

        # QComboBoxes
        self._combo_line = self.findChild(QComboBox, 'comboBox_line')
        self._combo_cap = self.findChild(QComboBox, 'comboBox_cap')
        self._combo_join = self.findChild(QComboBox, 'comboBox_join')

        # QDoubleSpinBoxes
        self._box_max_dim = self.findChild(QDoubleSpinBox, 'doubleSpinBox_max')
        self._box_line = self.findChild(QDoubleSpinBox, 'doubleSpinBox_line')

        # QPushButtons
        self._btn_bg_color = self.findChild(QPushButton, 'button_bg_color')
        self._btn_line = self.findChild(QPushButton, 'button_line')
        self._btn_fill = self.findChild(QPushButton, 'button_fill')
        self._btn_save = self.findChild(QPushButton, 'pushButton_save')
        self._btn_reset = self.findChild(QPushButton, 'pushButton_reset')
        self._btn_load_settings = self.findChild(QPushButton,
                                                 'pushButton_load_settings')

        # QTreeWidgets
        self._tree_line = self.findChild(QTreeWidget,
                                         'treeWidget_line_settings')
        self._tree_fill = self.findChild(QTreeWidget,
                                         'treeWidget_fill_settings')

        # Map Widget
        self._map = self.findChild(QWidget, 'widget_map')

    def _blockAllSignals(self, state):
        """
        Private function used to block all signals from firing. This is useful
        if a signal fires due to updating a widget, but it's not desireable to
        fire that signal at this time

        Parameters:
        -----------
        state : boolean
            True to block all signals; False otherwise

        Returns:
        --------
        """
        self._label_line.blockSignals(state)
        self._label_fill.blockSignals(state)

        self._combo_line.blockSignals(state)
        self._combo_cap.blockSignals(state)
        self._combo_join.blockSignals(state)

        self._box_max_dim.blockSignals(state)
        self._box_line.blockSignals(state)

        self._btn_bg_color.blockSignals(state)
        self._btn_line.blockSignals(state)
        self._btn_fill.blockSignals(state)

        self._tree_line.blockSignals(state)
        self._tree_fill.blockSignals(state)

        self._map.blockSignals(state)

    def _configWidgets(self):
        """
        Private function used to configure the widgets according to the
        user's configuration file

        Parameters:
        -----------
        Returns:
        --------
        """
        # Attach this configuration instance to the map widget
        self._map.setConfiguration(self._config)

        # Set the background color of the bg button
        self._setButtonColor(self._btn_bg_color,
                             self._config.getValue(c.CONFIG_BG_COLOR))

        # Populate the line and fill widgets
        self._blockAllSignals(True)
        self._populateList(QPen, self._tree_line, noAlph=[c.KEY_HIGHWAY])
        self._populateList(QColor, self._tree_fill)
        self._blockAllSignals(False)

    def _setButtonColor(self, button, color):
        """
        Private helper function used to set the background color of a specified
        button

        Parameters:
        -----------
        button : QPushButton
            The button you're changing the background color of
        color : QColor
            The new background color

        Returns:
        --------
        """
        r, g, b = color.red(), color.green(), color.blue()
        button.setStyleSheet('background-color: rgb(%s, %s, %s)' % (r, g, b))

    def _populateList(self, dType, tree, noAlph=[]):
        """
        Private function used to populate a QTreeWidget with list item

        Parameters:
        -----------
        dType : QPen | QColor
            This function is used to add both datatypes to our lists, but only
            one at a time, as Line-Items used QPen and Fill-Items use QColor
        tree : QTreeWidget
            The parent list widget receiving the items
        noAlpha : list of Strings
            Include the keys for the items (natural, highway, etc.) that you
            do NOT want to alphabetize on presentation. Typically, you want
            everything except highway alphabetized.

        Returns:
        --------
        """
        # Add the data groups to the top level for the line tree
        for key in c.DATA_GROUPS.keys():
            parent = None

            # Alphabetize?
            childKeys = list(c.DATA_GROUPS[key].keys())
            if key not in noAlph:
                # Ensure full alphabetization including upper case keys
                childKeys.sort(key=lambda item: item.lower())

            for childKey in childKeys:
                childConfig = c.DATA_GROUPS[key][childKey]

                # Add the children to the relevant list
                typ = type(self._config.getValue(childConfig))
                if typ == dType:
                    # Only create a parent if any children are the proper type
                    if parent is None:
                        parent = self._parentHelper(tree, key)
                    child = QTreeWidgetItem(parent)
                    child.setText(0, childKey)
                    child.setFlags(child.flags() | Qt.ItemIsUserCheckable)
                    child.setCheckState(0, Qt.Checked)

    def _refreshLists(self):
        """
        Private function used to update the QTreeWidgets with the proper
        checked states after a change has occured, such as loading a new
        configuration file

        Parameters:
        -----------
        Returns:
        --------
        """
        # Block signals during updating
        self._blockAllSignals(True)

        # Iterate over the QTreeWidgets and set the proper checked state
        for tree in [self._tree_line, self._tree_fill]:
            root = tree.invisibleRootItem()
            for i in range(root.childCount()):
                pitem = root.child(i)
                pitem.setDisabled(False)
                should_disable_parent = True
                for j in range(pitem.childCount()):
                    citem = pitem.child(j)
                    ptext, ctext = pitem.text(0), citem.text(0)

                    # If currently loaded OSM data does not use this tag, disable it
                    # without changing the check state (no reason to update their config)
                    if ptext not in self._current_file_tags or ctext not in self._current_file_tags[ptext]:
                        citem.setDisabled(True)
                        continue
                    else:
                        citem.setDisabled(False)
                        should_disable_parent = False

                    # Set the check state
                    if self._config.getItemState(c.DATA_GROUPS[ptext][ctext]):
                        citem.setCheckState(0, Qt.Checked)
                    else:
                        citem.setCheckState(0, Qt.Unchecked)
                
                # If there was nothing enabled in this parent, then we should disable the 
                # parent too. Note that _tree_line/_tree_fill.selectedItems() can be empty
                if should_disable_parent:
                   pitem.setDisabled(True)

        # Unblock signals
        self._blockAllSignals(False)

    def _parentHelper(self, tree, text):
        """
        Private function used to initialize and add a QTreeWidgetItem parent
        for a given tree and with given text

        Parameters:
        -----------
        tree : QTreeWidget
            The tree you're adding to
        text : String
            The text of the item

        Returns:
        --------
        parent : QTreeWidgetItem
            The parent item
        """
        parent = QTreeWidgetItem(tree)
        parent.setText(0, text)
        parent.setFlags(parent.flags() | Qt.ItemIsTristate |
                        Qt.ItemIsUserCheckable)
        parent.setCheckState(0, Qt.Checked)

        return parent

    def _colorPicker(self, sColor):
        """
        Private function used to return a selected color to the user

        Parameters:
        -----------
        sColor : QColor
            The starting color of the color chooser

        Returns:
        --------
        color : QColor
            Resulting selection
        """
        color = QColorDialog.getColor(sColor, self,
                                      'Choose a Color',
                                      QColorDialog.ShowAlphaChannel)

        return color
