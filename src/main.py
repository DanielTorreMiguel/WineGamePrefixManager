import sys
from gui import *
import addFolderDialog as adf
from PyQt5 import QtCore, QtGui, QtWidgets




def connectMainWindowSignals(ui):
    ui.scanButton.pressed.connect(scanButtonPressed)
    ui.foldersButton.pressed.connect(foldersButtonPressed)
    ui.wineButton.pressed.connect(wineButtonPressed)

def scanButtonPressed():
    print("hola")

def wineButtonPressed():
    print("hola2")


def foldersButtonPressed():
    dialog = adf.addFolderDialog()
    dialog.openDialog()


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    connectMainWindowSignals(ui)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
    
