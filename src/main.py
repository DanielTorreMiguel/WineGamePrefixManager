import sys
from gui import *
import steam as st
import os
import subprocess
import addFolderDialog as adf
import jsonWrapper as jw
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
        self.ui.launchButton.pressed.connect(self.launchGameButtonPressed)
        self.ui.winetricksButton.pressed.connect(self.winetricksButtonPressed)


    def scanButtonPressed(self):
        self.gameList = []
        #TODO add dialog to reflect this
        self.loadGameList()
        return
        
    def wineButtonPressed(self):
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
        self.gameList = st.loadGameList()
        for i in range(len(self.gameList)):
            table = self.ui.gameTable
            table.insertRow(table.rowCount())
            table.setItem(table.rowCount() - 1, 1, QTableWidgetItem(self.gameList[i]["name"]))
            table.setItem(table.rowCount() - 1, 0, QTableWidgetItem(str(i)))


    def settingsButtonPressed(self):
        #TODO open dialog with settings
        pass
    
    def launchGameButtonPressed(self):
        #steam steam://rungameid/656350
        if self.currentIndex != -1:
            pid=os.fork()
            if pid==0:
                os.system("steam steam://rungameid/" + str(self.gameList[self.currentIndex]['appid']))
    
    def winetricksButtonPressed(self):
        if self.currentIndex != -1:
            myenv = os.environ.copy()
            myenv['WINPREFIX'] = self.gameList[self.currentIndex]["prefixFolder"]
            command = ['winetricks']
            subprocess.check_call(command, env=myenv)
    
if __name__ == "__main__":
    window = mainWindow()
    window.start()
    
    
