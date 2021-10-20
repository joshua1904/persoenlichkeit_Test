# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'persönlichkeitTestrichtig.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QStatusBar, QWidget)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(813, 333)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.fragenLabel = QLabel(self.centralwidget)
        self.fragenLabel.setObjectName(u"fragenLabel")
        self.fragenLabel.setGeometry(QRect(10, 10, 791, 211))
        self.weiterButton = QPushButton(self.centralwidget)
        self.weiterButton.setObjectName(u"weiterButton")
        self.weiterButton.setGeometry(QRect(410, 270, 81, 31))
        self.zurueckButton = QPushButton(self.centralwidget)
        self.zurueckButton.setObjectName(u"zurueckButton")
        self.zurueckButton.setGeometry(QRect(330, 270, 81, 31))
        self.horizontalSlider = QSlider(self.centralwidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(330, 220, 160, 22))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.fragenLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.weiterButton.setText(QCoreApplication.translate("MainWindow", u"Weiter", None))
        self.zurueckButton.setText(QCoreApplication.translate("MainWindow", u"Zur\u00fcck", None))
    # retranslateUi


def frm_main():
    return None