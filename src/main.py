import sys
from gui import *
import steam as st
import json
import os
import addFolderDialog as adf
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem


class mainWindow(object):
    def start(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.connectMainWindowSignals()
        self.MainWindow.show()
        sys.exit(self.app.exec_())
    def connectMainWindowSignals(self):
        self.ui.scanButton.pressed.connect(self.scanButtonPressed)
        self.ui.foldersButton.pressed.connect(self.foldersButtonPressed)
        self.ui.wineButton.pressed.connect(self.wineButtonPressed)

    def scanButtonPressed(self):
        self.gameList = []
        #TODO add dialog to reflect this
        if os.path.isfile('folderList.json'): #if file exists
            with open('folderList.json') as json_file:
                data = json.load(json_file)
            for item in data:
                self.gameList.extend(st.populateGameList(item["path"]))
            for i in range(len(self.gameList)):
                table = self.ui.gameTable
                table.insertRow(table.rowCount())
                table.setItem(table.rowCount() - 1, 1, QTableWidgetItem(self.gameList[i]["name"]))
                table.setItem(table.rowCount() - 1, 0, QTableWidgetItem(str(i)))
        return
        
    def wineButtonPressed(self):
        print("hola2")


    def foldersButtonPressed(self):
        dialog = adf.addFolderDialog()
        dialog.openDialog()



    
if __name__ == "__main__":
    window = mainWindow()
    window.start()
    
    
