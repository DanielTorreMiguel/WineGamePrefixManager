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
        self.currentIndex = -1
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.connectMainWindowSignals()
        self.loadGameList()
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def connectMainWindowSignals(self):
        self.ui.scanButton.pressed.connect(self.scanButtonPressed)
        self.ui.foldersButton.pressed.connect(self.foldersButtonPressed)
        self.ui.wineButton.pressed.connect(self.wineButtonPressed)
        self.ui.gameTable.itemClicked.connect(self.onItemActivated) #when a row is clicked

    def scanButtonPressed(self):
        self.gameList = []
        #TODO add dialog to reflect this
        self.loadGameList()
        return
        
    def wineButtonPressed(self):
        import subprocess
        if self.currentIndex != -1:
            myenv = os.environ.copy()
            myenv['WINPREFIX'] = self.gameList[self.currentIndex]["prefixFolder"]
            command = ['/usr/bin/winecfg']
            subprocess.check_call(command, env=myenv)

    def foldersButtonPressed(self):
        dialog = adf.addFolderDialog()
        dialog.openDialog()
    
    def onItemActivated(self, item):
        index = self.ui.gameTable.indexFromItem(item)
        self.currentIndex = index.row() - 1
        print(self.currentIndex)
        
    def loadGameList(self):
        if os.path.isfile('gameList.json'):
            with open('gameList.json') as json_file:
                self.gameList = json.load(json_file)
        else:
            if os.path.isfile('folderList.json'): #if file exists
                with open('folderList.json') as json_file:
                    data = json.load(json_file)
                for item in data:
                    self.gameList.extend(st.populateGameList(item["path"]))
                with open("gameList.json", 'w', encoding='utf-8') as f:
                    json.dump(self.gameList, f, ensure_ascii=False, indent=4)
        for i in range(len(self.gameList)):
            table = self.ui.gameTable
            table.insertRow(table.rowCount())
            table.setItem(table.rowCount() - 1, 1, QTableWidgetItem(self.gameList[i]["name"]))
            table.setItem(table.rowCount() - 1, 0, QTableWidgetItem(str(i)))



    
if __name__ == "__main__":
    window = mainWindow()
    window.start()
    
    
