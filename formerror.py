# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formerror.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_errorwindow(object):
    def setupUi(self, errorwindow):
        errorwindow.setObjectName("errorwindow")
        errorwindow.resize(276, 192)
        errorwindow.setDocumentMode(False)
        errorwindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(errorwindow)
        self.centralwidget.setObjectName("centralwidget")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(220, 0, 51, 41))
        self.closebutton.setMouseTracking(False)
        self.closebutton.setStyleSheet("QPushButton{\n"
"border: 1px solid #555;\n"
"padding: 5 px ;\n"
"border-top-right-radius: 11px;\n"
"background: black;\n"
"}\n"
"QPushButton:hover { background: rgba(255,255,255,.2); }\n"
"QPushButton:pressed { background: white; }")
        self.closebutton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("photos/крестик.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closebutton.setIcon(icon)
        self.closebutton.setDefault(False)
        self.closebutton.setObjectName("closebutton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 201, 41))
        self.label.setStyleSheet("QLabel{\n"
"    font: 75 italic 22pt \"MS Sans Serif\";\n"
"color: white;\n"
"border: 1px solid #555;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"}")
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 261, 91))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
"border-bottom-left-radius: 11px;\n"
"border-bottom-right-radius: 11px;\n"
"background: black;\n"
"}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_14.setObjectName("label_14")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 241, 20))
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(100, 40, 61, 31))
        self.pushButton.setStyleSheet("QPushButton {\n"
"  display: inline-block;\n"
"  color: white;\n"
"  text-decoration: none;\n"
"  user-select: none;\n"
"  outline: none;\n"
"  border: 2px solid white;\n"
"  border-radius: 1px;\n"
"  transition: 0.2s;\n"
"} \n"
"QPushButton:hover { background: rgba(255,255,255,.2); }\n"
"QPushButton:pressed { background: white; }")
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2.raise_()
        self.closebutton.raise_()
        self.label.raise_()
        errorwindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(errorwindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 276, 21))
        self.menubar.setObjectName("menubar")
        errorwindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(errorwindow)
        self.statusbar.setObjectName("statusbar")
        errorwindow.setStatusBar(self.statusbar)

        self.retranslateUi(errorwindow)
        QtCore.QMetaObject.connectSlotsByName(errorwindow)

    def retranslateUi(self, errorwindow):
        _translate = QtCore.QCoreApplication.translate
        errorwindow.setWindowTitle(_translate("errorwindow", "MainWindow"))
        self.label.setText(_translate("errorwindow", "Ошибка"))
        self.label_13.setText(_translate("errorwindow", "TextLabel"))
        self.label_14.setText(_translate("errorwindow", "TextLabel"))
        self.label_3.setText(_translate("errorwindow", "Увы! Такой логин уже есть, придумайте новый!"))
        self.pushButton.setText(_translate("errorwindow", "Хорошо!"))
import photos_rc
