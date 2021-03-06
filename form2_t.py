# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form2_t.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_teor2(object):
    def setupUi(self, teor2):
        teor2.setObjectName("teor2")
        teor2.resize(936, 489)
        teor2.setDocumentMode(False)
        teor2.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(teor2)
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
        self.groupBox_2.setGeometry(QtCore.QRect(10, 50, 921, 381))
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
        self.stackedWidget = QtWidgets.QStackedWidget(self.groupBox_2)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 901, 361))
        self.stackedWidget.setStyleSheet("color:white;\n"
"background:black;\n"
"")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.textBrowser = QtWidgets.QTextBrowser(self.page)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 901, 351))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
"    font: 8pt \"MS Sans Serif\";\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser.setObjectName("textBrowser")
        self.go1 = QtWidgets.QPushButton(self.page)
        self.go1.setGeometry(QtCore.QRect(690, 330, 91, 31))
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
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.label_2.setStyleSheet("\n"
"font: 18pt \"MS Sans Serif\";")
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(0, 90, 231, 221))
        self.label_4.setStyleSheet("background-image: url(:/newPrefix2/пирамидка 21.png);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(650, 90, 251, 221))
        self.label_3.setStyleSheet("background-image: url(:/newPrefix2/пирамидка22.jpg.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(120, 0, 741, 51))
        self.textBrowser_2.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.page_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(240, 50, 401, 391))
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
        self.go2 = QtWidgets.QPushButton(self.page_2)
        self.go2.setGeometry(QtCore.QRect(690, 330, 91, 31))
        self.go2.setStyleSheet("QPushButton {\n"
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
        self.go2.setObjectName("go2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_5 = QtWidgets.QLabel(self.page_3)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.label_5.setStyleSheet("\n"
"font: 18pt \"MS Sans Serif\";")
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.page_3)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 211, 211))
        self.label_7.setStyleSheet("background-image: url(:/newPrefix2/куб 21.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.page_3)
        self.label_8.setGeometry(QtCore.QRect(590, 90, 291, 191))
        self.label_8.setStyleSheet("background-image: url(:/newPrefix2/куб 22.png);")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_12 = QtWidgets.QLabel(self.page_3)
        self.label_12.setGeometry(QtCore.QRect(130, 10, 641, 21))
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_12")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.page_3)
        self.textBrowser_4.setGeometry(QtCore.QRect(240, 40, 331, 321))
        self.textBrowser_4.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.go3 = QtWidgets.QPushButton(self.page_3)
        self.go3.setGeometry(QtCore.QRect(690, 330, 91, 31))
        self.go3.setStyleSheet("QPushButton {\n"
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
        self.go3.setObjectName("go3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_6 = QtWidgets.QLabel(self.page_4)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 111, 31))
        self.label_6.setStyleSheet("\n"
"font: 18pt \"MS Sans Serif\";")
        self.label_6.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setGeometry(QtCore.QRect(10, 80, 291, 241))
        self.label_9.setStyleSheet("background-image: url(:/newPrefix2/призма 21.png);")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.page_4)
        self.label_10.setGeometry(QtCore.QRect(630, 70, 261, 251))
        self.label_10.setStyleSheet("background-image: url(:/newPrefix2/призма 22.png);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_5.setGeometry(QtCore.QRect(120, 0, 411, 71))
        self.textBrowser_5.setStyleSheet("QTextBrowser{\n"
"font: 12pt \"MS Sans Serif\";\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.page_4)
        self.textBrowser_6.setGeometry(QtCore.QRect(310, 70, 311, 281))
        self.textBrowser_6.setStyleSheet("QTextBrowser{\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-top-left-radius: 11px;\n"
"background: black;\n"
"font-weight: 3;\n"
"text-transform: capitalize;\n"
"font-size: 25;\n"
"color: white;\n"
"}")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.stackedWidget.addWidget(self.page_4)
        self.tomainbutton = QtWidgets.QPushButton(self.groupBox_2)
        self.tomainbutton.setGeometry(QtCore.QRect(810, 340, 91, 31))
        self.tomainbutton.setStyleSheet("QPushButton {\n"
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
        self.tomainbutton.setObjectName("tomainbutton")
        self.groupBox_2.raise_()
        self.closebutton.raise_()
        self.label.raise_()
        teor2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(teor2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName("menubar")
        teor2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(teor2)
        self.statusbar.setObjectName("statusbar")
        teor2.setStatusBar(self.statusbar)

        self.retranslateUi(teor2)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(teor2)

    def retranslateUi(self, teor2):
        _translate = QtCore.QCoreApplication.translate
        teor2.setWindowTitle(_translate("teor2", "MainWindow"))
        self.label.setText(_translate("teor2", "Применение метода внутреннего проектирования.Теория."))
        self.label_13.setText(_translate("teor2", "TextLabel"))
        self.label_14.setText(_translate("teor2", "TextLabel"))
        self.textBrowser.setHtml(_translate("teor2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:8pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600; font-style:italic; color:#ffffff;\">Построение сечения методом внутреннего проецирования. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\">Этот метод является в достаточной мере универсальным. В тех случаях, когда нужный след (или следы) секущей плоскости оказывается за пределами чертежа, этот метод имеет даже определенные преимущества. Вместе с тем следует иметь в виду, что построения, выполняемые при использовании этого метода, зачастую получаются «скученными». Тем не менее, в некоторых случаях метод внутреннего проектирования оказывается наиболее рациональным. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">Метод внутреннего проекти­рования называют еще методом соответствий, или методом диагональных сечений.</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">При применении этого метода каждая заданная точка проектируется на плоскость основания. Существует два возможных вида проектирования: центральное и параллельное. Центральное проектирование, как правило, используется при построении сечений пирамид, вершина пирамиды при этом является центром проекции. Параллельное проектирование используется при построении сечений призм.</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-style:italic; color:#ffffff;\">Суть метода</span><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\"> – найти дополнительные точки с/п по проекциям ее известных точек на опорную плоскость при выбранном аппарате проецирования. проекции искомых точек с/п на опорную выбирают так, чтобы они были связаны с проекциями известных точек с/п, и чтобы число графических операций при решении задачи было минимальным. </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:600; color:#ffffff;\">Алгоритм построения сечения методом внутреннего проецирования.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\"> 1. Построить вспомогательные сечения и найти линию их пересечения.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\"> 2. Построить след сечения на ребре многогранника.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; color:#ffffff;\"> 3. Если точек сечения не хватает для построения самого сечения повторить пп.1-2. </span></p></body></html>"))
        self.go1.setText(_translate("teor2", "Далее"))
        self.label_2.setText(_translate("teor2", "Пример 1"))
        self.textBrowser_2.setHtml(_translate("teor2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; font-style:italic; color:#ffffff;\">Задача:</span><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\"> постройте сечение тетраэдра плоскостью, проходящей через точки М, N, K. Точка М лежит на ребре AD, N — на ребре DC, К — на ребре АВ.</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("teor2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\">Решение:</span><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Построим </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:600; color:#ffffff;\">центральные проекции</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> точек </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">K</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">M</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> из точки </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">C</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> на плоскость </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">SAB</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и обозначим их </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">K</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">M</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Проведём прямые </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">K</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">M</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">LB</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и отметим точку их пересечения </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">F</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Проведём прямые </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">CF</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff; vertical-align:sub;\">1</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">KM</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и отметим точку их пересечения </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">F</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Проведём прямую </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">LF</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и отметим точку её пересечения с ребром </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">CB</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> – точку </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">P</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">. Это первая вершина искомого сечения.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Проведём прямую </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">PM</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и отметим точку её пересечения с ребром </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">SB</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">. Это вторая вершина сечения.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Из второй вершины проведём прямую через точку </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">L</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и найдём третью вершину сечения.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Из третьей вершины проведём прямую через точку </span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; font-style:italic; color:#ffffff;\">K</span><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\"> и найдём четвёртую вершину сечения.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'arial\'; font-size:8pt; font-weight:400; color:#ffffff;\">Все четыре вершины сечения получены – построим сечение.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; color:#ffffff;\"><br /></span></p></body></html>"))
        self.go2.setText(_translate("teor2", "Далее"))
        self.label_5.setText(_translate("teor2", "Пример 2"))
        self.label_12.setText(_translate("teor2", "Задача: Построить сечение куба плоскостью, проходящей через точки M, N и К."))
        self.textBrowser_4.setHtml(_translate("teor2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\">Решение:</span><span style=\" font-size:12pt; font-weight:600; font-style:italic; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">Найдем ортогональные проекции точек М и N на плоскость АВС. Проекцию точки М обозначим М1.,ортогональная</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">проекция точки N есть точка А.</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">Рассмотрим плоскость MM1АN. В этой плоскости прямые MN и M1A пересекаются. Обозначим точку их пересечения</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">через Х. Понятно, что точка Х лежит не только в плоскости MM1АN, но и в плоскости сечения, так как принадлежит</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:12pt; color:#ffffff;\">прямой MN. Дальше все становится ясным.</span><span style=\" font-size:12pt; color:#ffffff;\"> </span></p></body></html>"))
        self.go3.setText(_translate("teor2", "Далее"))
        self.label_6.setText(_translate("teor2", "Пример 3"))
        self.textBrowser_5.setHtml(_translate("teor2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Sans Serif\'; font-size:12pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri\'; font-size:11pt; font-weight:600; font-style:italic; color:#ffffff;\">Задача</span><span style=\" font-family:\'Calibri\'; font-size:11pt; color:#ffffff;\">: Построить сечение правильной пятиугольной призмы ABCDEA1B1C1D1E1 плоскостью, проходящей через точки  N, O, P методом внутреннего проецирования.</span><span style=\" font-size:11pt; color:#ffffff;\"> </span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("teor2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:0; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">Решение:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Построим вспомогательное сечение пирамиды плоскостью, проходящей через</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">точку S и прямые SQ и SC, т. е. плоскость SCQ1.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Будем искать след плоскости PQR на прямой SD. Для этого построим второе</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">вспомогательное сечение пирамиды. Полученное сечение SDR - сечение, проходящее</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">через прямые SR и SD, на котором находим след секущей плоскости PQR.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Строим прямую SN1, по которой пересекаются плоскости SCQ1 и SDR1, и затем</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">точку N, в которой пересекаются прямые PQ и SN1.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4. Так как точка N лежит на прямой PQ, то она лежит и в секущей плоскости PQR.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Тогда прямая RN лежит в секущей плоскости, а также и точка Е - точка пересечения</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">прямых RN и SD.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5. Проведем прямую EQ, она пересекает прямую SA в точке F, которая является</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">следом секущей плоскости на ребре SA.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Многоугольник EFKP - искомое сечение.</p></body></html>"))
        self.tomainbutton.setText(_translate("teor2", "Главное меню"))
import photos