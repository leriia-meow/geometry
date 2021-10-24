from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1154, 650)
        mainWindow.setDocumentMode(False)
        mainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1070, 0, 51, 41))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                      "border: 1px solid #555;\n"
                                      "padding: 5 px ;\n"
                                      "border-top-right-radius: 11px;\n"
                                      "background: qradialgradient(cx: 0.3, cy: -0.4, \n"
                                      "fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(58, 58, 58), stop: 1 rgb(50, 50, 50));\n"
                                      "}\n"
                                      "QPushButton:hover { background: rgba(255,255,255,.2); }\n"
                                      "QPushButton:pressed { background: white; }")
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("111.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setDefault(False)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 1051, 41))
        self.label.setStyleSheet("QLabel{\n"
                                 "    font: 75 italic 22pt \"MS Sans Serif\";\n"
                                 "color: white;\n"
                                 "border: 1px solid #555;\n"
                                 "border-top-left-radius: 11px;\n"
                                 "background: qradialgradient(cx: 0.3, cy: -0.4, \n"
                                 "fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(58, 58, 58), stop: 1 rgb(50, 50, 50));\n"
                                 "font-weight: 3;\n"
                                 "text-transform: capitalize;\n"
                                 "font-size: 25;\n"
                                 "}")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 1111, 101))
        self.groupBox.setStyleSheet("QGroupBox{\n"
                                    "background-color: grey;\n"
                                    "color: #333;\n"
                                    "border: 1 px solid #555;\n"
                                    "background: qradialgradient(cx: 0.3, cy: -0.4, \n"
                                    "fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(53, 53, 53), stop: 1 rgb(22, 22, 22));\n"
                                    "}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(480, 32, 621, 31))
        self.progressBar.setStyleSheet("QProgressBar {\n"
                                       "    border: 2px solid grey;\n"
                                       "    border-radius:15px;\n"
                                       "    color: white;\n"
                                       "    background-color: rgb(50, 50, 50);\n"
                                       "    font: 75 12pt  \"MS Sans Serif\";\n"
                                       "    text-align: center;\n"
                                       "\n"
                                       "}\n"
                                       "\n"
                                       "QProgressBar::chunk {\n"
                                       "    border-radius:13px;\n"
                                       "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgba(201, 81, 149, 255), stop:1 rgba(179, 65, 244, 255));\n"
                                       "}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.namelabel = QtWidgets.QLabel(self.groupBox)
        self.namelabel.setGeometry(QtCore.QRect(130, 30, 331, 41))
        self.namelabel.setStyleSheet("QLabel{\n"
                                     "    font: 75 italic 22pt \"MS Sans Serif\";\n"
                                     "color: white;\n"
                                     "font-weight: 3;\n"
                                     "text-transform: capitalize;\n"
                                     "font-size: 25;\n"
                                     "}")
        self.namelabel.setObjectName("namelabel")
        self.photo = QtWidgets.QLabel(self.groupBox)
        self.photo.setGeometry(QtCore.QRect(20, 10, 91, 81))
        self.photo.setText("")
        self.photo.setObjectName("photo")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 160, 1111, 431))
        self.groupBox_2.setStyleSheet("QGroupBox{\n"
                                      "border-bottom-left-radius: 11px;\n"
                                      "border-bottom-right-radius: 11px;\n"
                                      "background: qradialgradient(cx: 0.3, cy: -0.4, \n"
                                      "fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 rgb(35, 35, 35), stop: 1 rgb(0, 0, 0));\n"
                                      "}")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(20, 20, 47, 13))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 30, 47, 13))
        self.label_14.setObjectName("label_14")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 1071, 81))
        self.groupBox_3.setStyleSheet("QGroupBox{\n"
                                      "background-color: black;\n"
                                      "color: #333;\n"
                                      " border: 2px solid white;\n"
                                      "  border-radius: 1px;\n"
                                      "}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
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
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../Pictures/кнопка.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
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
        self.pushButton_5.setObjectName("pushButton_5")
        self.progressBar_2 = QtWidgets.QProgressBar(self.groupBox_3)
        self.progressBar_2.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progressBar_2.setStyleSheet("QProgressBar {\n"
                                         "    border: 2px solid grey;\n"
                                         "    border-radius:15px;\n"
                                         "    color: white;\n"
                                         "    background-color: rgb(50, 50, 50);\n"
                                         "    font: 12pt \"MS Sans Serif\";\n"
                                         "    text-align: center;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QProgressBar::chunk {\n"
                                         "    border-radius:13px;\n"
                                         "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(64, 83, 255), stop:1 rgb(0, 255, 255));\n"
                                         "}")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 411, 61))
        self.label_5.setStyleSheet("QLabel{\n"
                                   "font: 75 italic 26pt \"MS Sans Serif\";\n"
                                   "color: white;\n"
                                   "}")
        self.label_5.setObjectName("label_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 320, 1071, 81))
        self.groupBox_4.setStyleSheet("QGroupBox{\n"
                                      "background-color: black;\n"
                                      "color: #333;\n"
                                      "border: 2px solid white;\n"
                                      "border-radius: 1px;\n"
                                      "font: 75 italic 22pt \"MS Sans Serif\";\n"
                                      "color: white;\n"
                                      "}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_3.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
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
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
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
        self.pushButton_6.setObjectName("pushButton_6")
        self.progressBar_3 = QtWidgets.QProgressBar(self.groupBox_4)
        self.progressBar_3.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progressBar_3.setStyleSheet("QProgressBar {\n"
                                         "    border: 2px solid grey;\n"
                                         "    border-radius:15px;\n"
                                         "    color: white;\n"
                                         "    background-color: rgb(50, 50, 50);\n"
                                         "    font: 12pt \"MS Sans Serif\";\n"
                                         "    text-align: center;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QProgressBar::chunk {\n"
                                         "    border-radius:13px;\n"
                                         "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(0, 255, 0), stop:1 rgb(255, 255, 127));\n"
                                         "}")
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName("progressBar_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 411, 61))
        self.label_2.setStyleSheet("QLabel{\n"
                                   "font: 75 italic 26pt \"MS Sans Serif\";\n"
                                   "color: white;\n"
                                   "}")
        self.label_2.setObjectName("label_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 120, 1071, 81))
        self.groupBox_6.setStyleSheet("QGroupBox{\n"
                                      "background-color: black;\n"
                                      "color: #333;\n"
                                      " border: 2px solid white;\n"
                                      "  border-radius: 1px;\n"
                                      "}")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_8.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
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
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon1)
        self.pushButton_8.setDefault(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_9.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
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
        self.pushButton_9.setObjectName("pushButton_9")
        self.progressBar_5 = QtWidgets.QProgressBar(self.groupBox_6)
        self.progressBar_5.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progressBar_5.setStyleSheet("QProgressBar {\n"
                                         "    border: 2px solid grey;\n"
                                         "    border-radius:15px;\n"
                                         "    color: white;\n"
                                         "    background-color: rgb(50, 50, 50);\n"
                                         "    font: 12pt \"MS Sans Serif\";\n"
                                         "    text-align: center;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QProgressBar::chunk {\n"
                                         "    border-radius:13px;\n"
                                         "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(64, 83, 255), stop:1 rgb(0, 255, 255));\n"
                                         "}")
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setObjectName("progressBar_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(20, 10, 481, 61))
        self.label_4.setStyleSheet("QLabel{\n"
                                   "font: 75 italic 24pt \"MS Sans Serif\";\n"
                                   "color: white;\n"
                                   "}")
        self.label_4.setObjectName("label_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 220, 1071, 81))
        self.groupBox_5.setStyleSheet("QGroupBox{\n"
                                      "background-color: black;\n"
                                      "color: #333;\n"
                                      " border: 2px solid white;\n"
                                      "  border-radius: 1px;\n"
                                      "}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_4.setGeometry(QtCore.QRect(600, 20, 41, 41))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
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
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 20, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
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
        self.pushButton_7.setObjectName("pushButton_7")
        self.progressBar_4 = QtWidgets.QProgressBar(self.groupBox_5)
        self.progressBar_4.setGeometry(QtCore.QRect(660, 20, 401, 41))
        self.progressBar_4.setStyleSheet("QProgressBar {\n"
                                         "    border: 2px solid grey;\n"
                                         "    border-radius:15px;\n"
                                         "    color: white;\n"
                                         "    background-color: rgb(50, 50, 50);\n"
                                         "    font: 12pt \"MS Sans Serif\";\n"
                                         "    text-align: center;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QProgressBar::chunk {\n"
                                         "    border-radius:13px;\n"
                                         "    background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0,  stop:0 rgb(64, 83, 255), stop:1 rgb(0, 255, 255));\n"
                                         "}")
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setObjectName("progressBar_4")
        self.label_3 = QtWidgets.QLabel(self.groupBox_5)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 441, 61))
        self.label_3.setStyleSheet("QLabel{\n"
                                   "font: 75 italic 26pt \"MS Sans Serif\";\n"
                                   "color: white;\n"
                                   "}")
        self.label_3.setObjectName("label_3")
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1154, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.label.setText(_translate("mainWindow", "Построение сечений"))
        self.namelabel.setText(_translate("mainWindow", "1"))
        self.label_13.setText(_translate("mainWindow", "TextLabel"))
        self.label_14.setText(_translate("mainWindow", "TextLabel"))
        self.pushButton_5.setText(_translate("mainWindow", "?"))
        self.label_5.setText(_translate("mainWindow", "Метод следов"))
        self.pushButton_6.setText(_translate("mainWindow", "?"))
        self.label_2.setText(_translate("mainWindow", "Контрольное задание"))
        self.pushButton_9.setText(_translate("mainWindow", "?"))
        self.label_4.setText(_translate("mainWindow", "Метод вспомагательных сечений"))
        self.pushButton_7.setText(_translate("mainWindow", "?"))
        self.label_3.setText(_translate("mainWindow", "Комбинированный метод"))
