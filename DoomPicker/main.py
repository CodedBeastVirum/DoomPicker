# This Python file uses the following encoding: utf-8
import sys
from PyQt6 import QtWidgets, uic
import os
import omg
import DataBase_Collector


class Ui(QtWidgets.QMainWindow):



    def __init__(self):
        #code to grab maps
        Maps = DataBase_Collector.ripper("G:\LEVELS\PWADS") #os.listdir("G:\LEVELS\PWADS")
        IWADs = os.listdir(r"C:\Users\andbo\gzdoom-4-7-1-Windows-64bit\IWAD")
        Mods = os.listdir(r"C:\Users\andbo\gzdoom-4-7-1-Windows-64bit\Mods")
        #Main Loader Code
        super(Ui, self).__init__()
        uic.loadUi("mainwindow.ui", self)
        #Code to initialise various functions
        InitMapSelRadGroup(self)
        PopulateLists(self, IWADs, Mods, Maps)
        #code to link the function below to pressing the correct combobox button
        self.StartAtSelectedMap.toggled.connect(lambda:self.MapSelBoxEnabled(self.StartAtSelectedMap))
        #code to show the window
        self.show()

    def MapSelBoxEnabled(self, b):
        if b.text() == "Load Map:":
            if b.isChecked() == True:
                self.MapSelect.setEnabled(True)
            else:
                self.MapSelect.setEnabled(False)


def InitMapSelRadGroup(self):
    #sets up radio buttons with groups
    MapRadGrp = QtWidgets.QButtonGroup()
    MapRadGrp.addButton(self.StartAtSelectedMap)
    MapRadGrp.addButton(self.FirstMapStart)
    MapRadGrp.addButton(self.MainMenuStart)
    self.MainMenuStart.setChecked(True)

def PopulateLists(self, IWADs, Mods, Maps):
    #populates the map lists
    self.IWAD_List.addItems(IWADs)
    self.Mod_List.addItems(Mods)
    self.MapPackList.addItems(Maps)



app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec()
