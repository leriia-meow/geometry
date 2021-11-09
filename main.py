import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QFileDialog, QFrame
from PyQt5.QtGui import QPixmap, QPainter, QColor, QPen
from PyQt5.QtCore import QRect
from PIL import Image
from PIL.ImageQt import ImageQt
import random
from PyQt5.QtCore import Qt
from form1_p import Ui_pract1
from form1_t import Ui_teor1
from form2_p import Ui_pract2
from form2_t import Ui_teor2
from form3_p import Ui_pract3
from form3_t import Ui_teor3
from formk import Ui_kontrless
from forminp import Ui_inputwindow
from formauth import Ui_authwindow
from formerror import Ui_errorwindow
from main_window import Ui_mainWindow
from formstop import Ui_stopwindow
import sqlite3
import yadisk
import math
ID = 0


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, id):
        global ID
        ID = id
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()
        self.ph = self.cur.execute("""SELECT photo FROM users WHERE id = ?""", (self.id,)).fetchall()[0][0]
        with open("photos/photo.jpg", 'wb') as file:
            file.write(self.ph)
        self.ph = Image.open('photos/photo.jpg').convert("RGBA")
        self.temp = ImageQt(self.ph)
        self.pixmap = QPixmap.fromImage(self.temp)
        self.photo.setPixmap(self.pixmap.scaled(self.photo.size()))
        self.log = self.cur.execute("""SELECT login FROM users WHERE id = ?""", (self.id,)).fetchall()[0][0]
        self.namelabel.setText(self.log)
        self.prog = int(sum(list(self.cur.execute("""SELECT * FROM progress 
        WHERE id = ?""", (self.id,)).fetchall()[0][1:])) / 8 * 100)
        self.prog1 = int(sum(list(self.cur.execute("""SELECT les1t, les1ex1 FROM progress
         WHERE id = ?""", (self.id,)).fetchall()[0])) / 2 * 100)
        self.prog2 = int(sum(list(self.cur.execute("""SELECT les2t, les2ex1 FROM progress
         WHERE id = ?""", (self.id,)).fetchall()[0])) / 2 * 100)
        self.prog3 = int(sum(list(self.cur.execute("""SELECT les3t, les3ex1 FROM progress 
        WHERE id = ?""", (self.id,)).fetchall()[0])) / 2 * 100)
        self.progk = int(sum(list(self.cur.execute("""SELECT lesk, lesk1 FROM progress WHERE id = ?""",
                                                   (self.id,)).fetchall()[0][1:])) / 2 * 100)
        self.mainprogress.setMaximum(100)
        self.progress1.setMaximum(100)
        self.progress2.setMaximum(100)
        self.progress3.setMaximum(100)
        self.progress.setMaximum(100)
        self.mainprogress.setValue(self.prog)
        self.progress1.setValue(self.prog1)
        self.progress2.setValue(self.prog2)
        self.progress3.setValue(self.prog3)
        self.progress.setValue(self.progk)
        self.butp1.clicked.connect(self.pract1)
        self.butp2.clicked.connect(self.pract2)
        self.butp3.clicked.connect(self.pract3)
        self.butt1.clicked.connect(self.teor1)
        self.butt2.clicked.connect(self.teor2)
        self.butt3.clicked.connect(self.teor3)
        if self.prog < 75:
            self.butpk.clicked.connect(self.dont)
        else:

            self.butpk.clicked.connect(self.practk)

    def dont(self):
        self.con.commit()
        self.con.close()
        self.win = Stop(self.id)
        self.win.show()
        self.close()

    def teor1(self):
        self.con.execute("""UPDATE progress SET les1t = 1 WHERE id = ?""", (self.id,))
        self.con.commit()
        self.con.close()
        self.win = Teor1(self.id)
        self.win.show()
        self.close()

    def teor2(self):
        self.con.execute("""UPDATE progress SET les2t = 1 WHERE id = ?""", (self.id,))
        self.con.commit()
        self.con.close()
        self.win = Teor2(self.id)
        self.win.show()
        self.close()

    def teor3(self):
        self.con.execute("""UPDATE progress SET les3t = 1 WHERE id = ?""", (self.id,))
        self.con.commit()
        self.con.close()
        self.win = Teor3(self.id)
        self.win.show()
        self.close()

    def pract1(self):
        self.con.commit()
        self.con.close()
        self.win = Pract1(self.id)
        self.win.show()
        self.close()

    def pract2(self):
        self.con.commit()
        self.con.close()
        self.win = Pract2(self.id)
        self.win.show()
        self.close()

    def pract3(self):
        self.con.commit()
        self.con.close()
        self.win = Pract3(self.id)
        self.win.show()
        self.close()

    def practk(self):
        self.con.execute("""UPDATE progress SET lesk = 1 WHERE id = ?""", (self.id,))
        self.con.commit()
        self.con.close()
        self.win = Kontrless(self.id)
        self.win.show()
        self.close()


class Authorize(QMainWindow, Ui_authwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.other.clicked.connect(self.oth)
        self.last.clicked.connect(self.inp)
        self.photo.clicked.connect(self.input_photo)
        self.nameofphoto = random.choice(['photos/bear.jpg', 'photos/owl.jpg',
                                          'photos/owl1.jpg', 'photos/woolf.jpg',
                                          'photos/lion.jpg', 'photos/cat.jpg'])
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()

    def oth(self):
        self.con.commit()
        self.con.close()
        self.win = Input()
        self.win.show()
        self.close()

    def inp(self):
        self.name = self.login.text()
        self.passw = self.password.text()
        self.i = 1
        flag = True
        while flag:
            try:
                di = self.cur.execute("""SELECT id FROM users WHERE id = ?""", (self.i,)).fetchall()[0]
                self.i = self.i + 1
            except Exception:
                flag = False
        try:
            di = self.cur.execute("""SELECT id FROM users WHERE login = ?""", (self.name,)).fetchall()[0]
            flag = False
        except Exception:
            flag = True
        if self.name.isalnum() and flag and not self.name.isdigit():
            with open(self.nameofphoto, 'rb') as file:
                self.nameofphoto = file.read()
            self.cur.execute("""INSERT INTO users(id, login, password, photo) VALUES(?, ?, ?, ?)""", (self.i, self.name,
                                                                                                      self.passw,
                                                                                                      self.nameofphoto))
            self.cur.execute("""INSERT INTO progress(id, les1t, les1ex1, les1ex2, les1ex3, les2t, les2ex1, les2ex2,
             les2ex3, les3t, les3ex1, les3ex2, les3ex3, lesk, lesk1, lesk2, lesk3) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,
              ?, ?, ?, ?, ?, ?, ?, ?)""", (self.i, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
            self.con.commit()
            self.con.close()
            self.close()
            self.window = MainWindow(self.i)
            self.window.show()
        elif not flag:
            self.error.setText("Такой логин уже есть. Придумайте новый")
        elif self.name.isdigit():
            self.error.setText("Логин должен содержать символы, отличные от цифр")

    def input_photo(self):
        try:
            self.nameofphoto = QFileDialog.getOpenFileName(self, 'Выбрать картинку',
                                                           '', "Картинка (*.jpeg);;"
                                                               "Картинка (*.jpg);;"
                                                               "Картинка (*.png);;")[0]
            self.naming.setText(self.nameofphoto)
        except Exception:
            self.nameofphoto = random.choice(['photos/bear.jpg', 'photos/owl.jpg',
                                              'photos/owl1.jpg', 'photos/woolf.jpg',
                                              'photos/lion.jpg', 'photos/cat.jpg'])


class Input(QMainWindow, Ui_inputwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.enter.clicked.connect(self.entry)
        self.back.clicked.connect(self.backing)
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()

    def entry(self):
        self.name = self.login.text()
        self.passw = self.password.text()
        password = ''
        try:
            password = self.cur.execute("""SELECT password FROM users WHERE login = ?""", (self.name,)).fetchall()[0][0]
            i = self.cur.execute("""SELECT id FROM users WHERE login = ?""", (self.name,)).fetchall()[0][0]
            flag = True
        except Exception:
            flag = False
            self.logerror.setText("Не существует такого логина")
        if flag and password == self.passw:
            self.con.commit()
            self.con.close()
            self.close()
            self.window = MainWindow(i)
            self.window.show()
        elif password != self.passw or flag:
            self.passerror.setText("Неправильный пароль")

    def backing(self):
        self.win = Authorize()
        self.win.show()
        self.con.commit()
        self.con.close()
        self.close()


class Kontrless(QMainWindow, Ui_kontrless):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.tomainbutton.clicked.connect(self.back)

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()


class Teor1(QMainWindow, Ui_teor1):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.tomainbutton.clicked.connect(self.back)
        self.id = id
        self.go1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.go2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.go3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.label_4.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/тет 1.png").convert("RGBA"))
                                                 ).scaled(self.label_4.size()))
        self.label_3.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/тет 2.jpg").convert("RGBA"))
                                                 ).scaled(self.label_3.size()))
        self.label_7.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/куб1.png").convert("RGBA"))
                                                 ).scaled(self.label_7.size()))
        self.label_8.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/куб2.png").convert("RGBA"))
                                                 ).scaled(self.label_8.size()))
        self.label_9.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/призма1.png").convert("RGBA"))
                                                 ).scaled(self.label_9.size()))
        self.label_10.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/призма2.png").convert("RGBA"))
                                                  ).scaled(self.label_10.size()))

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()


class Teor2(QMainWindow, Ui_teor2):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.tomainbutton.clicked.connect(self.back)
        self.go1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.go2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.go3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.label_4.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/пирамидка 21.png").convert("RGBA"))
                                                 ).scaled(self.label_4.size()))
        self.label_3.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/пирамидка22.jpg.png").convert("RGBA"))
                                                 ).scaled(self.label_3.size()))
        self.label_7.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/куб 21.png").convert("RGBA"))
                                                 ).scaled(self.label_7.size()))
        self.label_8.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/куб 22.png").convert("RGBA"))
                                                 ).scaled(self.label_8.size()))
        self.label_9.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/призма 21.png").convert("RGBA"))
                                                 ).scaled(self.label_9.size()))
        self.label_10.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/призма 22.png").convert("RGBA"))
                                                  ).scaled(self.label_10.size()))

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()


class Teor3(QMainWindow, Ui_teor3):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.tomainbutton.clicked.connect(self.back)
        self.go1.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.go2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.go3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.label_3.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/Паралл.jpg").convert("RGBA")
                                                         )).scaled(self.label_3.size()))
        self.label_7.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/параллA.png").convert("RGBA")
                                                         )).scaled(self.label_7.size()))
        self.label_9.setPixmap(QPixmap.fromImage(ImageQt(Image.open("photos/параллБ.png").convert("RGBA")
                                                         )).scaled(self.label_9.size()))

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()


class Pract1(QMainWindow, Ui_pract1):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.tomain.clicked.connect(self.back)
        self.tomain1.clicked.connect(self.back)
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()
        self.p1 = Painting(1, self.ex1)
        self.p1.setGeometry(QRect(10, 50, 921, 620))
        self.p1.setFrameShape(QFrame.StyledPanel)
        self.p1.setFrameShadow(QFrame.Raised)
        self.p1.setObjectName("frame_11")
        super().setMouseTracking(True)
        self.go1.clicked.connect(self.check)
        self.fig = Figures([(50, 610, 350, 610), (50, 610, 50, 300), (50, 300, 350, 300), (350, 300, 350, 610),
                               (350, 610, 530, 490), (530, 490, 530, 190), (530, 190, 230, 190), (230, 190, 50, 300),
                               (350, 300, 530, 190), (230, 190, 230, 490), (230, 490, 50, 610), (230, 490, 530, 490)],
                              [(50, 610), (140, 245), (380, 190)])
        self.choisepoints = []
        self.choiselines = []

    def check(self):
        points = self.fig.outputp()
        if (50, 610,) in points and (140, 245,) in points and (380, 190,) in points and (530, 490,) in points:
            self.con.execute("""UPDATE progress SET les1ex1 = 1 WHERE id = ?""", (self.id,))
            self.con.commit()
        else:
            pass

    def keyPressEvent(self, event):
        key = event.key()
        if event.key() == Qt.Key.Key_W:
            self.update()
        elif event.key() == Qt.Key_Space:
            self.update()
        elif event.key() == Qt.Key_Shift:
            n = 100000000000000000000
            if len(self.choisepoints[0]) == 4 and len(self.choisepoints[1]) == 4:
                x1 = self.choisepoints[0][0]
                x2 = self.choisepoints[0][2]
                x3 = self.choisepoints[1][0]
                x4 = self.choisepoints[0][2]
                y1 = self.choisepoints[0][1]
                y2 = self.choisepoints[0][3]
                y3 = self.choisepoints[1][1]
                y4 = self.choisepoints[1][3]
                if y2 - y1 != 0:
                    q = (x2 - x1) / (y1 - y2)
                    sn = (x3 - x4) + (y3 - y4) * q
                    if sn:
                        fn = (x3 - x1) + (y3 - y1) * q
                        n = fn / sn
                else:
                    if (y3 - y4) > 0:
                        n = (y3 - y1) / (y3 - y4)
                if n != 100000000000000000000:
                    x = x3 + (x4 - x3) * n
                    y = y3 + (y4 - y3) * n
                    self.p1.setnum([x, y])
            self.update()

    def mouseReleaseEvent(self, event):
        points = self.fig.outputp()
        lines = self.fig.outputl()
        x = event.x()
        y = event.y()
        otvx = 0
        otvy = 0
        if event.button() == Qt.RightButton:
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.choisepoints.append((otvx, otvy,))
            self.p1.setnum([self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                            self.choisepoints[-2][1]])
            self.update()

    def mousePressEvent(self, event):
        points = self.fig.outputp()
        lines = self.fig.outputl()
        x = event.x()
        y = event.y()
        otvx = 0
        otvy = 0
        if event.button() == Qt.LeftButton:
            r = 1000000000
            otvx2 = 0
            otvy2 = 0
            for a, b, c, d in lines:
                if x + y > 0 and abs((b - d) * x + (d - a) * y + a * d - b * c) / math.sqrt(x ** 2 + y ** 2) < r:
                    r = abs((b - d) * x + (d - a) * y + a * d - b * c) / math.sqrt(x ** 2 + y ** 2)
                    otvx2 = c
                    otvy2 = d
                    otvx = a
                    otvy = b
            self.choiselines.append((otvx, otvy, otvx2, otvy2,))
            self.update()
        if event.button() == Qt.RightButton:
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.choisepoints.append((otvx, otvy,))
            if len(self.choisepoints) == 2:
                del self.choisepoints[0]
            self.update()

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()
        self.con.commit()
        self.con.close()


class Pract2(QMainWindow, Ui_pract2):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.tomain.clicked.connect(self.back)
        self.tomain1.clicked.connect(self.back)
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()
        self.p21 = Painting(2, self.ex1)
        self.p21.setGeometry(QRect(10, 50, 921, 620))
        self.p21.setFrameShape(QFrame.StyledPanel)
        self.p21.setFrameShadow(QFrame.Raised)
        self.p21.setObjectName("frame_21")
        self.go1.clicked.connect(self.check)
        self.points = Figures([(50, 610, 350, 610), (50, 610, 50, 300), (50, 300, 350, 300), (350, 300, 350, 610),
                              (350, 610, 530, 490), (530, 490, 530, 190), (530, 190, 230, 190), (230, 190, 50, 300),
                              (350, 300, 530, 190), (230, 190, 230, 490), (230, 490, 50, 610), (230, 490, 530, 490)],
                              [(50, 610), (140, 245), (380, 190)])

    def check(self):
        points = self.points.outputp()
        if (495, 180,) in points and (170, 420,) in points and (170, 140,) in points and (495, 460,) in points:
            self.con.execute("""UPDATE progress SET les2ex1 = 1 WHERE id = ?""", (self.id,))
            self.con.commit()

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()
        self.con.commit()
        self.con.close()


class Pract3(QMainWindow, Ui_pract3):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.tomain.clicked.connect(self.back)
        self.tomain1.clicked.connect(self.back)
        self.setFixedSize(self.size())
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()
        self.p31 = Painting(3, self.ex1)
        self.p31.setGeometry(QRect(10, 50, 921, 620))
        self.p31.setFrameShape(QFrame.StyledPanel)
        self.p31.setFrameShadow(QFrame.Raised)

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()
        self.con.commit()
        self.con.close()


class Painting(QFrame):
    def __init__(self, number, parent=None):
        super().__init__(parent)
        self.newpoints = []
        self.newlines = []
        self.num = number

    def paintlines(self, x1, y1, x2, y2):
        self.newlines.append((x1, y1, x2, y2,))

    def setnum(self, u):
        if len(u) == 2:
            self.num = 7
            self.list = u
        elif len(u) == 4:
            self.num = 6
            self.list = u

    def paintpoint(self, x, y):
        self.newpoints.append((x, y,))

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.begin(self)
        if self.num == 6:
            self.paintlines(*self.list)
        if self.num == 7:
            self.paintpoints(*self.list)
        for x1, y1, x2, y2 in self.newlines:
            pen = QPen(Qt.yellow, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(x1, y1, x2, y2)
        if self.num == 6 or self.num == 1:
            pen = QPen(Qt.white, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(50, 610, 350, 610)
            painter.drawLine(50, 610, 50, 300)
            painter.drawLine(50, 300, 350, 300)
            painter.drawLine(350, 300, 350, 610)
            painter.drawLine(350, 610, 530, 490)
            painter.drawLine(530, 490, 530, 190)
            painter.drawLine(530, 190, 230, 190)
            painter.drawLine(230, 190, 50, 300)
            painter.drawLine(350, 300, 530, 190)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.drawLine(230, 190, 230, 490)
            painter.drawLine(230, 490, 50, 610)
            painter.drawLine(230, 490, 530, 490)
            pen = QPen(Qt.blue, 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(50, 610)
            painter.drawPoint(140, 245)
            painter.drawPoint(380, 190)
        elif self.num == 2:
            pen = QPen(Qt.white, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(50, 60, 580, 60)
            painter.drawLine(50, 340, 50, 60)
            painter.drawLine(580, 340, 580, 60)
            painter.drawLine(50, 60, 410, 300)
            painter.drawLine(410, 300, 580, 60)
            painter.drawLine(410, 300, 410, 580)
            painter.drawLine(50, 340, 410, 580)
            painter.drawLine(580, 340, 410, 580)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.drawLine(580, 340, 50, 340)
            pen = QPen(Qt.blue, 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(495, 180)
            painter.drawPoint(170, 420)
            painter.drawPoint(170, 140)
        elif self.num == 3:
            pass
        elif self.num == 4:
            pass
        for x, y in self.newpoints:
            pen = QPen(Qt.green, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(x, y)


class Stop(QMainWindow, Ui_stopwindow):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.tomain.clicked.connect(self.back)
        self.setFixedSize(self.size())

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()


class Error(QMainWindow, Ui_errorwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Figures:
    def __init__(self, l, p):
        self.points = p
        self.lines = l

    def addp(self, x, y):
        self.points.append((x, y,))

    def addl(self, x1, y1, x2, y2):
        self.points.append((x1, y1, x2, y2))

    def longer(self, x10, y10, x20, y20, x11, y11, x21, y21):
        pass

    def outputp(self):
        return self.points

    def outputl(self):
        return self.lines


y = yadisk.YaDisk(token="AQAAAABE8FllAAd6ntFbwMKB-02KqLvhcIbTWso")
y.download("/user.db", "user.db")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorize()
    ex.show()
    app.exec()
y.download("/user.db", "user1.db")
con1 = sqlite3.connect("user.db")
cur1 = con1.cursor()
con2 = sqlite3.connect("user1.db")
cur2 = con2.cursor()
flag = True
log = log1 = ""
try:
    log = cur2.execute("""SELECT id FROM users WHERE id = ?""", (ID,)).fetchall()[0]
    log1 = cur1.execute("""SELECT id FROM users WHERE id = ?""", (ID,)).fetchall()[0]
except Exception:
    flag = False
    log = None
if log == log1:
    cur2.execute("""UPDATE progress SET les1t = ?, les1ex1 = ?, les1ex2 = ?, les1ex3 = ?, les2t = ?, les2ex1 = ?, 
    les2ex2 = ?, les2ex3 = ?, les3t = ?, les3ex1 = ?, les3ex2 = ?, les3ex3 = ?, lesk = ?, lesk1 = ?, lesk2 = ?,
     lesk3 = ? WHERE id = ?""", cur1.execute("""SELECT * FROM progress WHERE id = ?""", (ID,)).fetchall()[0])
elif log == None and ID > 0:
    cur2.execute("""INSERT INTO users(id, login, password, photo) VALUES(?, ?, ?, ?)""", cur1.execute("""SELECT *
     FROM users WHERE id = ?""", (ID,)).fetchall()[0])
    cur2.execute("""INSERT INTO progress(id, les1t, les1ex1, les1ex2, les1ex3, les2t, les2ex1, les2ex2,
                 les2ex3, les3t, les3ex1, les3ex2, les3ex3, lesk, lesk1, lesk2, lesk3) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, ?, ?)""", cur1.execute("""SELECT * FROM progress WHERE id = ?""",
                                                           (ID,)).fetchall()[0])
elif ID > 0:
    id = ID + 1
    while flag:
        try:
            log = cur2.execute("""SELECT id FROM users WHERE id = ?""", (id,)).fetchall()[0]
        except Exception:
            cur2.execute("""INSERT INTO users(login, password, photo) VALUES(?, ?, ?, ?)""",
                         cur1.execute("""SELECT login, password, photo FROM users WHERE id = ?""", (ID,)).fetchall()[0])
            cur2.execute("""INSERT INTO progress(les1t, les1ex1, les1ex2, les1ex3, les2t, les2ex1, les2ex2, les2ex3,
             les3t, les3ex1, les3ex2, les3ex3, lesk, lesk1, lesk2, lesk3) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
              ?, ?, ?, ?)""", cur1.execute("""SELECT * FROM progress WHERE id = ?""", (ID,)).fetchall()[0][1:])
con1.commit()
con1.close()
con2.commit()
con2.close()
y.remove("/user.db", permanently=True)
y.upload("user1.db", "/user.db")
sys.exit()
