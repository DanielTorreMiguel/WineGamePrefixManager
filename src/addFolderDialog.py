import foldersDialog as fd
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class addFolderDialog(object):

    def openDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = fd.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.connectFolderDialogSignals()
        self.window.exec() #won't show otherwise
        self.window.show()

    """
    Connects buttons from the dialog to functions
    """
    def connectFolderDialogSignals(self):
        self.ui.cancelButton.pressed.connect(self.cancelButtonPressed)
        self.ui.removeFolder.pressed.connect(self.removeFolderButtonPressed)
        self.ui.addFolder.pressed.connect(self.addFolderButtonPressed)
        self.ui.saveButton.pressed.connect(self.saveButtonPressed)
        pass

    def cancelButtonPressed(self):
        self.window.close()

    def saveButtonPressed(self):
        #TODO save data to json file
        self.window.close()
    
    def addFolderButtonPressed(self):
        #TODO open folder selection dialog and add it to list
        pass
   
    def removeFolderButtonPressed(self):
        #TODO remove folder from list
        pass
