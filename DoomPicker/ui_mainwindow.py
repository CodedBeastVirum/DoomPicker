# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MapSelect = QComboBox(self.centralwidget)
        self.MapSelect.setObjectName(u"MapSelect")
        self.MapSelect.setGeometry(QRect(650, 110, 131, 22))
        self.StartAtSelectedMap = QRadioButton(self.centralwidget)
        self.StartAtSelectedMap.setObjectName(u"StartAtSelectedMap")
        self.StartAtSelectedMap.setGeometry(QRect(650, 90, 91, 18))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartAtSelectedMap.sizePolicy().hasHeightForWidth())
        self.StartAtSelectedMap.setSizePolicy(sizePolicy)
        self.FirstMapStart = QRadioButton(self.centralwidget)
        self.FirstMapStart.setObjectName(u"FirstMapStart")
        self.FirstMapStart.setGeometry(QRect(650, 70, 101, 18))
        sizePolicy.setHeightForWidth(self.FirstMapStart.sizePolicy().hasHeightForWidth())
        self.FirstMapStart.setSizePolicy(sizePolicy)
        self.MainMenuStart = QRadioButton(self.centralwidget)
        self.MainMenuStart.setObjectName(u"MainMenuStart")
        self.MainMenuStart.setGeometry(QRect(650, 50, 111, 18))
        sizePolicy.setHeightForWidth(self.MainMenuStart.sizePolicy().hasHeightForWidth())
        self.MainMenuStart.setSizePolicy(sizePolicy)
        self.StartDoom = QPushButton(self.centralwidget)
        self.StartDoom.setObjectName(u"StartDoom")
        self.StartDoom.setGeometry(QRect(650, 550, 131, 21))
        self.Exit = QPushButton(self.centralwidget)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setGeometry(QRect(650, 520, 131, 21))
        self.Settings = QPushButton(self.centralwidget)
        self.Settings.setObjectName(u"Settings")
        self.Settings.setGeometry(QRect(650, 490, 131, 21))
        self.Difficulty = QComboBox(self.centralwidget)
        self.Difficulty.addItem("")
        self.Difficulty.addItem("")
        self.Difficulty.addItem("")
        self.Difficulty.addItem("")
        self.Difficulty.addItem("")
        self.Difficulty.addItem("")
        self.Difficulty.setObjectName(u"Difficulty")
        self.Difficulty.setGeometry(QRect(650, 160, 131, 22))
        self.DifficultyLabel = QLabel(self.centralwidget)
        self.DifficultyLabel.setObjectName(u"DifficultyLabel")
        self.DifficultyLabel.setGeometry(QRect(650, 140, 51, 16))
        self.IWAD_List = QListWidget(self.centralwidget)
        self.IWAD_List.setObjectName(u"IWAD_List")
        self.IWAD_List.setGeometry(QRect(10, 40, 161, 531))
        self.IWADLABEL = QLabel(self.centralwidget)
        self.IWADLABEL.setObjectName(u"IWADLABEL")
        self.IWADLABEL.setGeometry(QRect(10, 20, 37, 12))
        self.Mod_List = QListWidget(self.centralwidget)
        self.Mod_List.setObjectName(u"Mod_List")
        self.Mod_List.setGeometry(QRect(180, 40, 161, 531))
        self.ModLabel = QLabel(self.centralwidget)
        self.ModLabel.setObjectName(u"ModLabel")
        self.ModLabel.setGeometry(QRect(180, 20, 37, 12))
        self.MapPackLabel = QLabel(self.centralwidget)
        self.MapPackLabel.setObjectName(u"MapPackLabel")
        self.MapPackLabel.setGeometry(QRect(350, 20, 71, 16))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MapPackLabel.sizePolicy().hasHeightForWidth())
        self.MapPackLabel.setSizePolicy(sizePolicy1)
        self.MapPackList = QListWidget(self.centralwidget)
        self.MapPackList.setObjectName(u"MapPackList")
        self.MapPackList.setGeometry(QRect(350, 40, 161, 531))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.StartAtSelectedMap.setText(QCoreApplication.translate("MainWindow", u"Load Map:", None))
        self.FirstMapStart.setText(QCoreApplication.translate("MainWindow", u"AutoLoad Map", None))
        self.MainMenuStart.setText(QCoreApplication.translate("MainWindow", u"Start at main menu", None))
        self.StartDoom.setText(QCoreApplication.translate("MainWindow", u"Start Doom", None))
        self.Exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.Difficulty.setItemText(0, QCoreApplication.translate("MainWindow", u"Default", None))
        self.Difficulty.setItemText(1, QCoreApplication.translate("MainWindow", u"Very Easy", None))
        self.Difficulty.setItemText(2, QCoreApplication.translate("MainWindow", u"Easy", None))
        self.Difficulty.setItemText(3, QCoreApplication.translate("MainWindow", u"Normal", None))
        self.Difficulty.setItemText(4, QCoreApplication.translate("MainWindow", u"Hard", None))
        self.Difficulty.setItemText(5, QCoreApplication.translate("MainWindow", u"Very Hard", None))

        self.DifficultyLabel.setText(QCoreApplication.translate("MainWindow", u"Difficulty", None))
        self.IWADLABEL.setText(QCoreApplication.translate("MainWindow", u"IWAD", None))
        self.ModLabel.setText(QCoreApplication.translate("MainWindow", u"Mod", None))
        self.MapPackLabel.setText(QCoreApplication.translate("MainWindow", u"Map Pack", None))
    # retranslateUi

