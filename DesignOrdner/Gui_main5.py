# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Gui_main5.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1030, 307)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fragenLabel = QLabel(self.centralwidget)
        self.fragenLabel.setObjectName(u"fragenLabel")
        self.fragenLabel.setGeometry(QRect(-10, -10, 1041, 201))
        self.fragenLabel.setAutoFillBackground(False)
        self.fragenLabel.setAlignment(Qt.AlignCenter)
        self.fragenLabel.setMargin(10)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(390, 200, 251, 81))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.weiterButton = QPushButton(self.gridLayoutWidget)
        self.weiterButton.setObjectName(u"weiterButton")

        self.gridLayout_2.addWidget(self.weiterButton, 2, 1, 1, 1)

        self.horizontalSlider = QSlider(self.gridLayoutWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setCursor(QCursor(Qt.SizeHorCursor))
        self.horizontalSlider.setMouseTracking(True)
        self.horizontalSlider.setMaximum(6)
        self.horizontalSlider.setSliderPosition(3)
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 1, 0, 1, 2)

        self.zurueckButton = QPushButton(self.gridLayoutWidget)
        self.zurueckButton.setObjectName(u"zurueckButton")

        self.gridLayout_2.addWidget(self.zurueckButton, 2, 0, 1, 1)

        self.eingabeLabel = QLabel(self.gridLayoutWidget)
        self.eingabeLabel.setObjectName(u"eingabeLabel")
        self.eingabeLabel.setLayoutDirection(Qt.LeftToRight)
        self.eingabeLabel.setTextFormat(Qt.PlainText)
        self.eingabeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.eingabeLabel, 0, 0, 1, 2)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(867, 260, 161, 23))
        self.progressBar.setValue(24)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fragenLabel.setText(QCoreApplication.translate("MainWindow", u"1) Bla bla bla bla dies das", None))
        self.weiterButton.setText(QCoreApplication.translate("MainWindow", u"Weiter", None))
        self.zurueckButton.setText(QCoreApplication.translate("MainWindow", u"Zur\u00fcck", None))
        self.eingabeLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

