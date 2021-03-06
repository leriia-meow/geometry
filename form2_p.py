# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2_p.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pract2(object):
    def setupUi(self, pract2):
        pract2.setObjectName("pract2")
        pract2.resize(939, 868)
        pract2.setDocumentMode(False)
        pract2.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(pract2)
        self.centralwidget.setObjectName("centralwidget")
        self.closebutton = QtWidgets.QPushButton(self.centralwidget)
        self.closebutton.setGeometry(QtCore.QRect(880, 0, 51, 41))
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
        self.label.setGeometry(QtCore.QRect(10, 0, 861, 41))
        self.label.setStyleSheet("QLabel{\n"
"color: white;\n"
"border: 1px solid #555;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 22;\n"
"font: 75 italic 19pt \"MS Sans Serif\";\n"
"}")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, 921, 751))
        self.tabWidget.setStyleSheet("background:black;\n"
"")
        self.tabWidget.setObjectName("tabWidget")
        self.rules = QtWidgets.QWidget()
        self.rules.setObjectName("rules")
        self.tomain = QtWidgets.QPushButton(self.rules)
        self.tomain.setGeometry(QtCore.QRect(800, 670, 101, 41))
        self.tomain.setStyleSheet("QPushButton {\n"
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
        self.tomain.setObjectName("tomain")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.rules)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 901, 701))
        self.textBrowser_3.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.raise_()
        self.tomain.raise_()
        self.tabWidget.addTab(self.rules, "")
        self.ex1 = QtWidgets.QWidget()
        self.ex1.setObjectName("ex1")
        self.tomain1 = QtWidgets.QPushButton(self.ex1)
        self.tomain1.setGeometry(QtCore.QRect(800, 670, 101, 41))
        self.tomain1.setStyleSheet("QPushButton {\n"
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
        self.tomain1.setObjectName("tomain1")
        self.go1 = QtWidgets.QPushButton(self.ex1)
        self.go1.setGeometry(QtCore.QRect(680, 670, 101, 41))
        self.go1.setStyleSheet("QPushButton {\n"
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
        self.go1.setObjectName("go1")
        self.exe1 = QtWidgets.QLabel(self.ex1)
        self.exe1.setGeometry(QtCore.QRect(10, 10, 901, 61))
        self.exe1.setStyleSheet("color:white;")
        self.exe1.setObjectName("exe1")
        self.label_7 = QtWidgets.QLabel(self.ex1)
        self.label_7.setGeometry(QtCore.QRect(20, 90, 871, 561))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.tabWidget.addTab(self.ex1, "")
        pract2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pract2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 939, 21))
        self.menubar.setObjectName("menubar")
        pract2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(pract2)
        self.statusbar.setObjectName("statusbar")
        pract2.setStatusBar(self.statusbar)

        self.retranslateUi(pract2)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(pract2)

    def retranslateUi(self, pract2):
        _translate = QtCore.QCoreApplication.translate
        pract2.setWindowTitle(_translate("pract2", "MainWindow"))
        self.label.setText(_translate("pract2", "Применение метода внутреннего проектирования. Практика."))
        self.tomain.setText(_translate("pract2", "Главное меню"))
        self.textBrowser_3.setHtml(_translate("pract2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600; font-style:italic; color:#ffffff;\">Как играть?</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:28pt; font-weight:600; font-style:italic; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">Возможные построения этого урока:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">     1) Точка. Чтобы поставить точку необходимо выбрать 2 прямые и нажать &quot;T&quot;. Важно! Скрещивающиеся прямые также могут выглядеть пересекающимися на картинке, и программа даст возможо поставить точку на месте их &quot;пересечения&quot;)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">     2) Отрезок.Чтобы построить отрезок, необходимо выбрать одну точку правой конпкой мыши, довести до второй точки и отпустить.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">     3) Прямая, параллельная данной. Чтобы построить прямую, параллельную данной, выберите прямую, затем левой кнопкой мыши коснитесь какой-либо точки и нажмите &quot;P&quot;.</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:22pt; color:#ffffff;\">(Доп. Чтобы выбрать прямую необходимо нажать &quot;L&quot;, а после этого начать выбирать: &quot;D&quot; - если нужная прямая, иначе - &quot;N&quot;)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; color:#ffffff;\">Удачи!</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#121212;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#ffffff;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rules), _translate("pract2", "Правила"))
        self.tomain1.setText(_translate("pract2", "Главное меню"))
        self.go1.setText(_translate("pract2", "Сдать"))
        self.exe1.setText(_translate("pract2", "Задача: постройте сечение по заданным точкам"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ex1), _translate("pract2", "Задача"))
