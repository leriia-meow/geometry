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
from formright import Ui_rightwindow

MAINPRACT = 0
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
                                                   (self.id,)).fetchall()[0])) / 2 * 100)
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
        global MAINPRACT
        self.con.commit()
        self.con.close()
        MAINPRACT = Pract1(self.id)
        MAINPRACT.show()
        self.close()

    def pract2(self):
        global MAINPRACT
        self.con.commit()
        self.con.close()
        MAINPRACT = Pract2(self.id)
        MAINPRACT.show()
        self.close()

    def pract3(self):
        global MAINPRACT
        self.con.commit()
        self.con.close()
        MAINPRACT = Pract3(self.id)
        MAINPRACT.show()
        self.close()

    def practk(self):
        global MAINPRACT
        self.con.execute("""UPDATE progress SET lesk = 1 WHERE id = ?""", (self.id,))
        self.con.commit()
        self.con.close()
        MAINPRACT = Kontrless(self.id)
        MAINPRACT.show()
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
        self.fig = Figures([(50, 610, 250, 610), (50, 610, 50, 410), (50, 410, 250, 410), (250, 610, 250, 410),
                            (170, 330, 50, 410), (370, 330, 250, 410), (370, 330, 170, 330), (370, 330, 370, 530),
                            (250, 610, 370, 530), (170, 530, 370, 530), (170, 530, 50, 610), (170, 530, 170, 330)],
                           [(50, 610), (270, 330), (110, 370)])
        self.choisepoints = []
        self.choiselines = []
        self.n = -1
        self.point = []

    def check(self):
        points = self.fig.outputp()
        if (50, 610) in points and (270, 330) in points and (110, 370) in points and (370, 530) in points:
            self.con.execute("""UPDATE progress SET lesk1 = 1 WHERE id = ?""", (self.id,))
            self.con.commit()
            self.win = Right(self.id, 4, self.centralwidget)
            self.win.show()
            self.p1.right(4)
        else:
            self.win = Error(self.id, 4)
            self.win.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_L:
            self.poisk(0)
            self.n = 0
        if event.key() == Qt.Key_N and self.n != -1:
            lines = self.fig.outputl()
            self.n = (self.n + 1) % len(lines)
            self.poisk(self.n % len(lines))
        if event.key() == Qt.Key_D and self.n != -1:
            lines = self.fig.outputl()
            self.choiselines.append(lines[self.n % len(lines)])
            self.n = -1
            self.poisk(self.n)
        if event.key() == Qt.Key_R and self.n == -1:
            self.longer()
        if event.key() == Qt.Key_T:
            self.makepoints()
        if event.key() == Qt.Key_P:
            self.parall()

    def parall(self):
        if self.point != [] and len(self.choiselines) > 0:
            k = self.point[0] * (self.choiselines[-1][1] - self.choiselines[-1][3]) + self.point[1] * \
                (self.choiselines[-1][2] - self.choiselines[-1][0])
            if (self.choiselines[-1][1] - self.choiselines[-1][3]) == 0:
                x1 = 0
                x2 = 1000
                y1 = self.point[1]
                y2 = self.point[1]
            elif (self.choiselines[-1][2] - self.choiselines[-1][0]) == 0:
                x1 = self.point[0]
                x2 = self.point[0]
                y1 = 0
                y2 = 1000
            else:
                x1 = 0
                x2 = int(k / (self.choiselines[-1][1] - self.choiselines[-1][3]))
                y1 = int(k / (self.choiselines[-1][2] - self.choiselines[-1][0]))
                y2 = 0
            self.fig.addl(x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def makepoints(self):
        n = 100000000000000000000
        if len(self.choiselines) > 1:
            x1 = self.choiselines[-1][0]
            x2 = self.choiselines[-1][2]
            x3 = self.choiselines[-2][0]
            x4 = self.choiselines[-2][2]
            y1 = self.choiselines[-1][1]
            y2 = self.choiselines[-1][3]
            y3 = self.choiselines[-2][1]
            y4 = self.choiselines[-2][3]
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
                x = int(x3 + (x4 - x3) * n)
                y = int(y3 + (y4 - y3) * n)
                self.p1.setnum([x, y])
                self.fig.addp(x, y)
            self.update()

    def longer(self):
        if len(self.choiselines) > 0:
            a = self.choiselines[-1]
            if (a[2] - a[0]) != 0:
                x1 = 0
                x2 = 1000
                y1 = int((a[2] * a[1] - a[0] * a[3]) / (a[2] - a[0]))
                y2 = int((a[2] * a[1] - a[0] * a[3] + (a[3] - a[1]) * 1000) / (a[2] - a[0]))
            else:
                y1 = 0
                y2 = 1000
                x1 = int((a[2] * a[1] - a[0] * a[3]) / (a[1] - a[3]))
                x2 = int((a[2] * a[1] - a[0] * a[3] + (a[0] - a[2]) * 1000) / (a[1] - a[3]))
            self.fig.longer(a[0], a[1], a[2], a[3], x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def poisk(self, r):
        if r == -1:
            self.p1.delblue()
            self.update()
        else:
            lines = self.fig.outputl()
            self.p1.getblue(lines[r][0], lines[r][1], lines[r][2], lines[r][3])
            self.update()

    def mouseReleaseEvent(self, event):
        points = self.fig.outputp()
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
            if len(self.choisepoints) > 0 and (self.choisepoints[-1][0], self.choisepoints[-1][1],
                                               self.choisepoints[-2][0], self.choisepoints[-2][1]) not in points and \
                    (self.choisepoints[-2][0], self.choisepoints[-2][1], self.choisepoints[-1][0],
                     self.choisepoints[-1][1]) not in points:
                self.p1.setnum([self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                                self.choisepoints[-2][1]])
                self.fig.addl(self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                              self.choisepoints[-2][1])
                self.choisepoints.clear()
                self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.choisepoints.append((otvx, otvy,))
            self.update()
        elif event.button() == Qt.LeftButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.point = [otvx, otvy]
            self.update()

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
        self.fig = Figures([(50, 610, 250, 610), (50, 610, 50, 410), (50, 410, 250, 410), (250, 610, 250, 410),
                            (170, 330, 50, 410), (370, 330, 250, 410), (370, 330, 170, 330), (370, 330, 370, 530),
                            (250, 610, 370, 530), (170, 530, 370, 530), (170, 530, 50, 610), (170, 530, 170, 330)],
                           [(50, 610), (270, 330), (110, 370)])
        self.choisepoints = []
        self.choiselines = []
        self.n = -1
        self.point = []

    def check(self):
        points = self.fig.outputp()
        if (50, 610) in points and (270, 330) in points and (110, 370) in points and (370, 530) in points:
            self.con.execute("""UPDATE progress SET les1ex1 = 1 WHERE id = ?""", (self.id,))
            self.con.commit()
            self.win = Right(self.id, 1, self.centralwidget)
            self.win.show()
            self.p1.right(1)
        else:
            self.win = Error(self.id, 1)
            self.win.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_L:
            self.poisk(0)
            self.n = 0
        if event.key() == Qt.Key_N and self.n != -1:
            lines = self.fig.outputl()
            self.n = (self.n + 1) % len(lines)
            self.poisk(self.n % len(lines))
        if event.key() == Qt.Key_D and self.n != -1:
            lines = self.fig.outputl()
            self.choiselines.append(lines[self.n % len(lines)])
            self.n = -1
            self.poisk(self.n)
        if event.key() == Qt.Key_R and self.n == -1:
            self.longer()
        if event.key() == Qt.Key_T:
            self.makepoints()
        if event.key() == Qt.Key_P:
            self.parall()

    def parall(self):
        if self.point != [] and len(self.choiselines) > 0:
            k = self.point[0] * (self.choiselines[-1][1] - self.choiselines[-1][3]) + self.point[1] * \
                (self.choiselines[-1][2] - self.choiselines[-1][0])
            if (self.choiselines[-1][1] - self.choiselines[-1][3]) == 0:
                x1 = 0
                x2 = 1000
                y1 = self.point[1]
                y2 = self.point[1]
            elif (self.choiselines[-1][2] - self.choiselines[-1][0]) == 0:
                x1 = self.point[0]
                x2 = self.point[0]
                y1 = 0
                y2 = 1000
            else:
                x1 = 0
                x2 = int(k / (self.choiselines[-1][1] - self.choiselines[-1][3]))
                y1 = int(k / (self.choiselines[-1][2] - self.choiselines[-1][0]))
                y2 = 0
            self.fig.addl(x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def makepoints(self):
        n = 100000000000000000000
        if len(self.choiselines) > 1:
            x1 = self.choiselines[-1][0]
            x2 = self.choiselines[-1][2]
            x3 = self.choiselines[-2][0]
            x4 = self.choiselines[-2][2]
            y1 = self.choiselines[-1][1]
            y2 = self.choiselines[-1][3]
            y3 = self.choiselines[-2][1]
            y4 = self.choiselines[-2][3]
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
                x = int(x3 + (x4 - x3) * n)
                y = int(y3 + (y4 - y3) * n)
                self.p1.setnum([x, y])
                self.fig.addp(x, y)
            self.update()

    def longer(self):
        if len(self.choiselines) > 0:
            a = self.choiselines[-1]
            if (a[2] - a[0]) != 0:
                x1 = 0
                x2 = 1000
                y1 = int((a[2] * a[1] - a[0] * a[3]) / (a[2] - a[0]))
                y2 = int((a[2] * a[1] - a[0] * a[3] + (a[3] - a[1]) * 1000) / (a[2] - a[0]))
            else:
                y1 = 0
                y2 = 1000
                x1 = int((a[2] * a[1] - a[0] * a[3]) / (a[1] - a[3]))
                x2 = int((a[2] * a[1] - a[0] * a[3] + (a[0] - a[2]) * 1000) / (a[1] - a[3]))
            self.fig.longer(a[0], a[1], a[2], a[3], x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def poisk(self, r):
        if r == -1:
            self.p1.delblue()
            self.update()
        else:
            lines = self.fig.outputl()
            self.p1.getblue(lines[r][0], lines[r][1], lines[r][2], lines[r][3])
            self.update()

    def mouseReleaseEvent(self, event):
        points = self.fig.outputp()
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
            if len(self.choisepoints) > 0 and (self.choisepoints[-1][0], self.choisepoints[-1][1],
                                               self.choisepoints[-2][0], self.choisepoints[-2][1]) not in points and \
                    (self.choisepoints[-2][0], self.choisepoints[-2][1], self.choisepoints[-1][0],
                     self.choisepoints[-1][1]) not in points:
                self.p1.setnum([self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                                self.choisepoints[-2][1]])
                self.fig.addl(self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                              self.choisepoints[-2][1])
                self.choisepoints.clear()
                self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.choisepoints.append((otvx, otvy,))
            self.update()
        elif event.button() == Qt.LeftButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.point = [otvx, otvy]
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
        self.fig = Figures([(50, 60, 580, 60), (50, 340, 50, 60), (580, 340, 580, 60), (50, 60, 410, 300),
                            (410, 300, 580, 60), (410, 300, 410, 580), (50, 340, 410, 580), (580, 340, 410, 580),
                            (580, 340, 50, 340)], [(495, 180), (170, 420), (170, 140)])
        self.p1 = Painting(2, self.ex1)
        self.p1.setGeometry(QRect(10, 50, 921, 620))
        self.p1.setFrameShape(QFrame.StyledPanel)
        self.p1.setFrameShadow(QFrame.Raised)
        self.p1.setObjectName("frame_21")
        super().setMouseTracking(True)
        self.go1.clicked.connect(self.check)
        self.choisepoints = []
        self.choiselines = []
        self.n = -1
        self.point = []
        self.update()

    def check(self):
        points = self.fig.outputp()
        if (495, 180) in points and (170, 420) in points and (170, 140) in points and (495, 460) in points:
            self.con.execute("""UPDATE progress SET les2ex1 = 1 WHERE id = ?""", (self.id,))
            self.con.commit()
            self.win = Right(self.id, 2, self.centralwidget)
            self.win.show()
            self.p1.right(2)
        else:
            self.win = Error(self.id, 2)
            self.win.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_L:
            self.poisk(0)
            self.n = 0
        if event.key() == Qt.Key_N and self.n != -1:
            lines = self.fig.outputl()
            self.n = (self.n + 1) % len(lines)
            self.poisk(self.n % len(lines))
        if event.key() == Qt.Key_D and self.n != -1:
            lines = self.fig.outputl()
            self.choiselines.append(lines[self.n % len(lines)])
            self.n = -1
            self.poisk(self.n)
        if event.key() == Qt.Key_R and self.n == -1:
            self.longer()
        if event.key() == Qt.Key_T:
            self.makepoints()
        if event.key() == Qt.Key_P:
            self.parall()

    def parall(self):
        if self.point != [] and len(self.choiselines) > 0:
            k = self.point[0] * (self.choiselines[-1][1] - self.choiselines[-1][3]) + self.point[1] * \
                (self.choiselines[-1][2] - self.choiselines[-1][0])
            if (self.choiselines[-1][1] - self.choiselines[-1][3]) == 0:
                x1 = 0
                x2 = 1000
                y1 = self.point[1]
                y2 = self.point[1]
            elif (self.choiselines[-1][2] - self.choiselines[-1][0]) == 0:
                x1 = self.point[0]
                x2 = self.point[0]
                y1 = 0
                y2 = 1000
            else:
                x1 = 0
                x2 = int(k / (self.choiselines[-1][1] - self.choiselines[-1][3]))
                y1 = int(k / (self.choiselines[-1][2] - self.choiselines[-1][0]))
                y2 = 0
            self.fig.addl(x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def makepoints(self):
        n = 100000000000000000000
        if len(self.choiselines) > 1:
            x1 = self.choiselines[-1][0]
            x2 = self.choiselines[-1][2]
            x3 = self.choiselines[-2][0]
            x4 = self.choiselines[-2][2]
            y1 = self.choiselines[-1][1]
            y2 = self.choiselines[-1][3]
            y3 = self.choiselines[-2][1]
            y4 = self.choiselines[-2][3]
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
                x = int(x3 + (x4 - x3) * n)
                y = int(y3 + (y4 - y3) * n)
                self.p1.setnum([x, y])
                self.fig.addp(x, y)
            self.update()

    def longer(self):
        if len(self.choiselines) > 0:
            a = self.choiselines[-1]
            if (a[2] - a[0]) != 0:
                x1 = 0
                x2 = 1000
                y1 = int((a[2] * a[1] - a[0] * a[3]) / (a[2] - a[0]))
                y2 = int((a[2] * a[1] - a[0] * a[3] + (a[3] - a[1]) * 1000) / (a[2] - a[0]))
            else:
                y1 = 0
                y2 = 1000
                x1 = int((a[2] * a[1] - a[0] * a[3]) / (a[1] - a[3]))
                x2 = int((a[2] * a[1] - a[0] * a[3] + (a[0] - a[2]) * 1000) / (a[1] - a[3]))
            self.fig.longer(a[0], a[1], a[2], a[3], x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def poisk(self, r):
        if r == -1:
            self.p1.delblue()
            self.update()
        else:
            lines = self.fig.outputl()
            self.p1.getblue(lines[r][0], lines[r][1], lines[r][2], lines[r][3])
            self.update()

    def mouseReleaseEvent(self, event):
        points = self.fig.outputp()
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
            if len(self.choisepoints) > 0 and (self.choisepoints[-1][0], self.choisepoints[-1][1],
                                               self.choisepoints[-2][0], self.choisepoints[-2][1]) not in points and \
                    (self.choisepoints[-2][0], self.choisepoints[-2][1], self.choisepoints[-1][0],
                     self.choisepoints[-1][1]) not in points:
                self.p1.setnum([self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                                self.choisepoints[-2][1]])
                self.fig.addl(self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                              self.choisepoints[-2][1])
                self.choisepoints.clear()
                self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.choisepoints.append((otvx, otvy,))
            self.update()
        elif event.button() == Qt.LeftButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y):
                    otvx = i
                    otvy = j
            self.point = [otvx, otvy]
            self.update()

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
        self.fig = Figures([(490, 100, 190, 340), (490, 100, 550, 580), (190, 340, 550, 580), (550, 580, 670, 340),
                            (670, 340, 490, 100), (400, 370, 370, 460), (580, 280, 640, 400), (190, 340, 670, 340)],
                           [(400, 370), (580, 280), (460, 520)])
        self.p1 = Painting(3, self.ex1)
        self.p1.setGeometry(QRect(10, 50, 921, 620))
        self.p1.setFrameShape(QFrame.StyledPanel)
        self.p1.setFrameShadow(QFrame.Raised)
        self.p1.setObjectName("frame_31")
        super().setMouseTracking(True)
        self.go1.clicked.connect(self.check)
        self.choisepoints = []
        self.choiselines = []
        self.n = -1
        self.point = []
        self.update()

    def check(self):
        points = self.fig.outputp()
        if (340, 220) in points and (580, 220) in points and (580, 520) in points and (460, 520) in points:
            self.con.execute("""UPDATE progress SET les3ex1 = 1 WHERE id = ?""", (self.id,))
            self.con.commit()
            self.win = Right(self.id, 3, self.centralwidget)
            self.win.show()
            self.p1.right(3)
        else:
            self.win = Error(self.id, 3)
            self.win.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_L:
            self.poisk(0)
            self.n = 0
        if event.key() == Qt.Key_N and self.n != -1:
            lines = self.fig.outputl()
            self.n = (self.n + 1) % len(lines)
            self.poisk(self.n % len(lines))
        if event.key() == Qt.Key_D and self.n != -1:
            lines = self.fig.outputl()
            self.choiselines.append(lines[self.n % len(lines)])
            self.n = -1
            self.poisk(self.n)
        if event.key() == Qt.Key_R and self.n == -1:
            self.longer()
        if event.key() == Qt.Key_T:
            self.makepoints()
        if event.key() == Qt.Key_P:
            self.parall()

    def parall(self):
        if self.point != [] and len(self.choiselines) > 0:
            k = self.point[0] * (self.choiselines[-1][1] - self.choiselines[-1][3]) + self.point[1] * \
                (self.choiselines[-1][2] - self.choiselines[-1][0])
            if (self.choiselines[-1][1] - self.choiselines[-1][3]) == 0:
                x1 = 0
                x2 = 1000
                y1 = self.point[1]
                y2 = self.point[1]
            elif (self.choiselines[-1][2] - self.choiselines[-1][0]) == 0:
                x1 = self.point[0]
                x2 = self.point[0]
                y1 = 0
                y2 = 1000
            else:
                x1 = 0
                x2 = int(k / (self.choiselines[-1][1] - self.choiselines[-1][3]))
                y1 = int(k / (self.choiselines[-1][2] - self.choiselines[-1][0]))
                y2 = 0
            self.fig.addl(x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def makepoints(self):
        n = 100000000000000000000
        if len(self.choiselines) > 1:
            x1 = self.choiselines[-1][0]
            x2 = self.choiselines[-1][2]
            x3 = self.choiselines[-2][0]
            x4 = self.choiselines[-2][2]
            y1 = self.choiselines[-1][1]
            y2 = self.choiselines[-1][3]
            y3 = self.choiselines[-2][1]
            y4 = self.choiselines[-2][3]
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
                x = int(x3 + (x4 - x3) * n)
                y = int(y3 + (y4 - y3) * n)
                self.p1.setnum([x, y])
                self.fig.addp(x, y)
            self.update()

    def longer(self):
        if len(self.choiselines) > 0:
            a = self.choiselines[-1]
            if (a[2] - a[0]) != 0:
                x1 = 0
                x2 = 1000
                y1 = int((a[2] * a[1] - a[0] * a[3]) / (a[2] - a[0]))
                y2 = int((a[2] * a[1] - a[0] * a[3] + (a[3] - a[1]) * 1000) / (a[2] - a[0]))
            else:
                y1 = 0
                y2 = 1000
                x1 = int((a[2] * a[1] - a[0] * a[3]) / (a[1] - a[3]))
                x2 = int((a[2] * a[1] - a[0] * a[3] + (a[0] - a[2]) * 1000) / (a[1] - a[3]))
            self.fig.longer(a[0], a[1], a[2], a[3], x1, y1, x2, y2)
            self.p1.setnum([x1, y1, x2, y2])
            self.update()

    def poisk(self, r):
        if r == -1:
            self.p1.delblue()
            self.update()
        else:
            lines = self.fig.outputl()
            self.p1.getblue(lines[r][0], lines[r][1], lines[r][2], lines[r][3])
            self.update()

    def mouseReleaseEvent(self, event):
        points = self.fig.outputp()
        x = event.x()
        y = event.y()
        otvx = 0
        otvy = 0
        if event.button() == Qt.RightButton:
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y) or abs(x - i) <= abs(otvx - x) \
                        and abs(y - j) <= abs(otvy - y):
                    otvx = i
                    otvy = j
            self.choisepoints.append((otvx, otvy,))
            if len(self.choisepoints) > 0 and (self.choisepoints[-1][0], self.choisepoints[-1][1],
                                               self.choisepoints[-2][0], self.choisepoints[-2][1]) not in points and \
                    (self.choisepoints[-2][0], self.choisepoints[-2][1], self.choisepoints[-1][0],
                     self.choisepoints[-1][1]) not in points:
                self.p1.setnum([self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                                self.choisepoints[-2][1]])
                self.fig.addl(self.choisepoints[-1][0], self.choisepoints[-1][1], self.choisepoints[-2][0],
                              self.choisepoints[-2][1])
                self.choisepoints.clear()
                self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) <= abs(otvx - x) and abs(y - j)  <= abs(otvy - y):
                    otvx = i
                    otvy = j
            self.choisepoints.append((otvx, otvy,))
        elif event.button() == Qt.LeftButton:
            points = sorted(self.fig.outputp())
            x = event.x()
            y = event.y()
            otvx = 0
            otvy = 0
            for i, j in points:
                if abs(x - i) + abs(y - j) < abs(otvx - x) + abs(otvy - y) or abs(x - i) <= abs(otvx - x)\
                        and abs(y - j) <= abs(otvy - y):
                    otvx = i
                    otvy = j
            self.point = [otvx, otvy]
            self.update()

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()
        self.con.commit()
        self.con.close()


class Painting(QFrame):
    def __init__(self, number, parent=None):
        super().__init__(parent)
        self.n = number
        self.newpoints = []
        self.newlines = []
        self.num = number
        self.blue = 0
        self.f = 0

    def paintlines(self, x1, y1, x2, y2):
        self.newlines.append((x1, y1, x2, y2,))

    def setnum(self, u):
        if len(u) == 2:
            self.num = 7
            self.list = u
        elif len(u) == 4:
            self.num = 6
            self.list = u

    def paintpoints(self, x, y):
        self.newpoints.append((x, y,))

    def getblue(self, x1, y1, x2, y2):
        self.blue = (x1, y1, x2, y2,)

    def delblue(self):
        self.blue = 0

    def right(self, n):
        self.f = n

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.begin(self)
        if self.num == 6:
            self.paintlines(*self.list)
            self.num = 1
        if self.num == 7:
            self.paintpoints(*self.list)
            self.num = 1
        for x1, y1, x2, y2 in self.newlines:
            pen = QPen(Qt.yellow, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(x1, y1, x2, y2)
        if self.n == 1:
            pen = QPen(Qt.white, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(50, 610, 250, 610)
            painter.drawLine(50, 610, 50, 410)
            painter.drawLine(50, 410, 250, 410)
            painter.drawLine(250, 610, 250, 410)
            painter.drawLine(170, 330, 50, 410)
            painter.drawLine(370, 330, 250, 410)
            painter.drawLine(370, 330, 170, 330)
            painter.drawLine(370, 330, 370, 530)
            painter.drawLine(250, 610, 370, 530)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.drawLine(170, 530, 370, 530)
            painter.drawLine(170, 530, 50, 610)
            painter.drawLine(170, 530, 170, 330)
            pen = QPen(Qt.blue, 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(50, 610)
            painter.drawPoint(270, 330)
            painter.drawPoint(110, 370)
        elif self.n == 2:
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
        elif self.n == 3:
            pen = QPen(Qt.white, 3, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(490, 100, 190, 340)
            painter.drawLine(490, 100, 550, 580)
            painter.drawLine(190, 340, 550, 580)
            painter.drawLine(550, 580, 670, 340)
            painter.drawLine(670, 340, 490, 100)
            painter.drawLine(400, 370, 370, 460)
            painter.drawLine(580, 280, 640, 400)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.drawLine(190, 340, 670, 340)
            pen = QPen(Qt.blue, 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(400, 370)
            painter.drawPoint(580, 280)
            painter.drawPoint(460, 520)
        elif self.n == 4:
            pass
        for x, y in self.newpoints:
            pen = QPen(Qt.green, 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawPoint(x, y)
        if self.blue != 0:
            pen = QPen(Qt.blue, 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(self.blue[0], self.blue[1], self.blue[2], self.blue[3])
        if self.f == 1:
            pen = QPen(QColor(139, 0, 255), 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(50, 610, 110, 370)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.drawLine(270, 330, 110, 370)
            painter.drawLine(370, 530, 50, 610)
            painter.drawLine(370, 530, 270, 330)
        elif self.f == 2:
            pen = QPen(QColor(139, 0, 255), 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(170, 140, 495, 180)
            painter.drawLine(495, 180, 495, 460)
            painter.drawLine(170, 140, 170, 420)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.drawLine(170, 420, 495, 460)
        elif self.f == 3:
            pen = QPen(QColor(139, 0, 255), 7, Qt.SolidLine)
            painter.setPen(pen)
            painter.drawLine(340, 220, 360, 520)
            painter.drawLine(580, 220, 460, 520)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            painter.drawLine(340, 220, 580, 220)
            painter.drawLine(580, 520, 460, 520)


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
    def __init__(self, id, n):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.repeat.clicked.connect(self.rep)
        self.teor.clicked.connect(self.t)
        self.id = id
        self.num = n

    def t(self):
        global MAINPRACT
        MAINPRACT.close()
        if self.num == 1:
            self.win = Teor1(self.id)
            self.win.show()
            self.close()
        elif self.num == 2:
            self.win = Teor2(self.id)
            self.win.show()
            self.close()
        elif self.num == 3:
            self.win = Teor3(self.id)
            self.win.show()
            self.close()
        elif self.num == 4:
            self.win = Teor3(self.id)
            self.win.show()
            self.close()

    def rep(self):
        global MAINPRACT
        MAINPRACT.close()
        if self.num == 1:
            self.win = Pract1(self.id)
            self.win.show()
            self.close()
        elif self.num == 2:
            self.win = Pract2(self.id)
            self.win.show()
            self.close()
        elif self.num == 3:
            self.win = Pract3(self.id)
            self.win.show()
            self.close()
        elif self.num == 4:
            self.win = Kontrless(self.id)
            self.win.show()
            self.close()


class Right(QMainWindow, Ui_rightwindow):
    def __init__(self, id, n, closing):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id
        self.num = n
        self.goout.clicked.connect(self.tomain)
        self.c = closing

    def tomain(self):
        global MAINPRACT
        MAINPRACT.close()
        if self.num == 1:
            self.win = MainWindow(self.id)
            self.win.show()
            self.close()
        elif self.num == 2:
            self.win = MainWindow(self.id)
            self.win.show()
            self.close()
        elif self.num == 3:
            self.win = MainWindow(self.id)
            self.win.show()
            self.close()
        elif self.num == 4:
            pass


class Figures:
    def __init__(self, l, p):
        self.points = p
        self.lines = l

    def addp(self, x, y):
        self.points.append((x, y,))
        self.points = list(set(self.points))

    def addl(self, x1, y1, x2, y2):
        self.lines.append((x1, y1, x2, y2))
        self.lines = list(set(self.lines))

    def longer(self, x10, y10, x20, y20, x11, y11, x21, y21):
        del self.lines[self.lines.index((x10, y10, x20, y20,))]
        self.lines.append((x11, y11, x21, y21,))

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
    res = list(cur1.execute("""SELECT * FROM progress WHERE id = ?""", (ID,)).fetchall()[0])
    res.append(res[0])
    del res[0]
    cur2.execute("""UPDATE progress SET les1t = ?, les1ex1 = ?, les1ex2 = ?, les1ex3 = ?, les2t = ?, les2ex1 = ?, 
    les2ex2 = ?, les2ex3 = ?, les3t = ?, les3ex1 = ?, les3ex2 = ?, les3ex3 = ?, lesk = ?, lesk1 = ?, lesk2 = ?,
     lesk3 = ? WHERE id = ?""", tuple(res))
elif log == None and ID > 0:
    res = list(cur1.execute("""SELECT * FROM progress WHERE id = ?""", (ID,)).fetchall()[0])
    res.append(res[0])
    res2 = list(cur1.execute("""SELECT * FROM users WHERE id = ?""", (ID,)).fetchall()[0])
    res2.append(res2[0])
    cur2.execute("""INSERT INTO users(id, login, password, photo) VALUES(?, ?, ?, ?)""", tuple(res2))
    cur2.execute("""INSERT INTO progress(id, les1t, les1ex1, les1ex2, les1ex3, les2t, les2ex1, les2ex2,
                 les2ex3, les3t, les3ex1, les3ex2, les3ex3, lesk, lesk1, lesk2, lesk3) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, ?, ?)""", tuple(res))
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
