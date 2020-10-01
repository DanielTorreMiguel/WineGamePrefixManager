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
        self.connectSettingsSignals()
        self.window.exec() #won't show otherwise
        self.window.show()

    def connectSettingsSignals(self):
        pass