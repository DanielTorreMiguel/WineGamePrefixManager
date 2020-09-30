import foldersDialog as fd
import sys
import os
import json
from PyQt5 import Qt, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QListWidget

class addFolderDialog(object):

    def openDialog(self):
        self.window = QtWidgets.QDialog()
        self.ui = fd.Ui_Dialog()
        self.ui.setupUi(self.window)
        self.connectFolderDialogSignals()
        self.populateFolderList()
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
        self._saveFolderList()
        self.window.close()
    
    def addFolderButtonPressed(self):
        folderPath = QFileDialog.getExistingDirectory(None, "select steamapps directory")
        self._addToFolderList(folderPath)       
        self._setErrorLabel("Folder added correctly")
   
    def removeFolderButtonPressed(self):
        if len(self.ui.folderList.selectedItems()) == 0:
            self._setErrorLabel("No items were selected")
        else:
            for i in range(self.ui.folderList.count()):
                if(self.ui.folderList.item(i).isSelected()):
                    self.ui.folderList.takeItem(i)
                    self._setErrorLabel("Item deleted sucessfully")
                    return

    def populateFolderList(self):
        if os.path.isfile('folderList.json'): #if file exists
            with open('folderList.json') as json_file:
                data = json.load(json_file)
            for item in data:
                self._addToFolderList(item["path"])
        return

    def _addToFolderList(self, path):
        self.ui.folderList.addItem(path)

    def _saveFolderList(self):
        folderList = []
        for index in range(self.ui.folderList.count()):
            field = {}
            field["path"] = self.ui.folderList.item(index).text()
            folderList.append(field)
        with open("folderList.json", 'w', encoding='utf-8') as f:
            json.dump(folderList, f, ensure_ascii=False, indent=4)

    def _setErrorLabel(self, text):
        self.ui.errorLabel.setText(text)