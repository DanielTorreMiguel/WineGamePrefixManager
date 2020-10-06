import settingsDialog as sd
import sys
import os
import jsonWrapper as jw
import steam as st
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidget

class openSettingsDialog(object):
    def openDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = sd.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.loadSettings()
        self.connectSettingsSignals()
        self.window.exec() #won't show otherwise
        self.window.show()

    def connectSettingsSignals(self):
        self.ui.wineSearch.pressed.connect(self.onWineSearchPressed)
        self.ui.winetricksSearch.pressed.connect(self.onWinetricksSearchPressed)
        self.ui.saveButton.pressed.connect(self.onSaveChangesPressed)
        self.ui.discardButton.pressed.connect(self.onDiscardChangesPressed)

    def loadSettings(self):
        if os.path.isfile("settings.json"):
            self.settings = jw.openJson("settings.json")
        else:
            self.settings = {}
            self.settings['winetricks'] = "default"
            self.settings['wine'] = "default"

    def saveSettings(self):
        jw.saveToJson(self.settings, "settings.json")

    def onWinetricksSearchPressed(self):
        file = self.getFile()[0]
        print(file)
        self.ui.winetricksLine.setText(file)

    def onWineSearchPressed(self):
        file = self.getFile()[0]
        print(file)
        self.ui.wineLine.setText(file)


    def onSaveChangesPressed(self):
        if self.ui.customWine.isChecked():
            self.settings['wine'] = self.ui.wineLine.text()
        else:
            self.settings['wine'] = "default"
        if self.ui.customWinetricks.isChecked():
            self.settings['winetricks'] = self.ui.winetricksLine.text()
        else:
            self.settings['winetricks'] = "default"
        self.saveSettings()
        self.window.close()

    def onDiscardChangesPressed(self):
        self.window.close()

    def getFile(self):
        filepath = QFileDialog.getOpenFileName()
        return filepath
