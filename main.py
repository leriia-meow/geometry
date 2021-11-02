import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QFileDialog
from PyQt5.QtGui import QPixmap
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


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, id):
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
        WHERE id = ?""", (self.id,)).fetchall()[0][1:])) / 16 * 100)
        self.prog1 = int(sum(list(self.cur.execute("""SELECT les1t, les1ex1, les1ex2, les1ex3 FROM progress
         WHERE id = ?""", (self.id,)).fetchall()[0])) / 4 * 100)
        self.prog2 = int(sum(list(self.cur.execute("""SELECT les2t, les2ex1, les2ex2, les2ex3 FROM progress
         WHERE id = ?""", (self.id,)).fetchall()[0])) / 4 * 100)
        self.prog3 = int(sum(list(self.cur.execute("""SELECT les3t, les3ex1, les3ex2, les3ex3 FROM progress 
        WHERE id = ?""", (self.id,)).fetchall()[0])) / 4 * 100)
        self.progk = int(sum(list(self.cur.execute("""SELECT lesk, lesk1, lesk2, lesk3 FROM progress WHERE id = ?""",
                                                   (self.id,)).fetchall()[0][1:])) / 4 * 100)
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
        if self.name.isalnum() and flag:
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
        self.tomain2.clicked.connect(self.back)
        self.tomain3.clicked.connect(self.back)
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()

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
        self.tomain2.clicked.connect(self.back)
        self.tomain3.clicked.connect(self.back)
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()

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
        self.tomain2.clicked.connect(self.back)
        self.tomain3.clicked.connect(self.back)
        self.setFixedSize(self.size())
        self.con = sqlite3.connect("user.db")
        self.cur = self.con.cursor()

    def back(self):
        self.win = MainWindow(self.id)
        self.win.show()
        self.close()
        self.con.commit()
        self.con.close()


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


y = yadisk.YaDisk(token="AQAAAABE8FllAAd6ntFbwMKB-02KqLvhcIbTWso")
y.download("/user.db", "user.db")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorize()
    ex.show()
    app.exec()
y.remove("/user.db", permanently=True)
y.upload("user.db", "/user.db")
sys.exit()
