import sys
from gui import *
import steam as st
import os
import subprocess
import addFolderDialog as adf
import openSettingsDialog as osd
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
        self.loadSettings()
        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def connectMainWindowSignals(self):
        self.ui.scanButton.pressed.connect(self.scanButtonPressed)
        self.ui.foldersButton.pressed.connect(self.foldersButtonPressed)
        self.ui.wineButton.pressed.connect(self.wineButtonPressed)
        self.ui.gameTable.itemClicked.connect(self.onItemActivated) #when a row is clicked
        self.ui.launchButton.pressed.connect(self.launchGameButtonPressed)
        self.ui.winetricksButton.pressed.connect(self.winetricksButtonPressed)
        self.ui.settingsButton.pressed.connect(self.settingsButtonPressed)

    def scanButtonPressed(self):
        self.gameList = []
        #TODO add dialog to reflect no folderList.json
        self.loadGameList()
        return
        

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
            table.setItem(max(table.rowCount() - 1, 0), 0, QTableWidgetItem(self.gameList[i]["name"]))
            #table.setItem(table.rowCount() - 1, 0, QTableWidgetItem(str(i)))


    def settingsButtonPressed(self):
        dialog = osd.openSettingsDialog()
        dialog.openDialog()
        self.loadSettings()
    
    def launchGameButtonPressed(self):
        #example steam steam://rungameid/656350
        if self.currentIndex != -1:
            pid=os.fork()
            if pid==0:
                os.system("steam steam://rungameid/" + str(self.gameList[self.currentIndex]['appid']))
    
    def winetricksButtonPressed(self):
        if self.settings['winetricks'] == "default":
            command = ['winetricks']
        else:
            command = [self.settings['winetricks']]
        self.wineLaunch(command)


    def wineButtonPressed(self):
        if self.settings['wine'] == "default":
            command = ['winecfg']
        else:
            command = [self.settings['wine']]
        self.wineLaunch(command)


    def wineLaunch(self, command):
         if self.currentIndex != -1:
            myenv = os.environ.copy()
            myenv['WINPREFIX'] = self.gameList[self.currentIndex]["prefixFolder"]
            subprocess.check_call(command, env=myenv)

    #TODO remove duplicate of openSettingsDialog.py
    def loadSettings(self):
        if os.path.isfile("settings.json"):
            self.settings = jw.openJson("settings.json")
        else:
            self.settings = {}
            self.settings['winetricks'] = "default"
            self.settings['wine'] = "default"

if __name__ == "__main__":
    window = mainWindow()
    window.start()
    
    
