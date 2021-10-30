import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidgetItem, QFileDialog
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
import sqlite3


class MainWindow(QMainWindow, Ui_mainWindow):
    def __init__(self, id):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы
        self.id = id


class Authorize(QMainWindow, Ui_authwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
                di = self.cur.execute("""SELECT id FROM users WHERE id = ?""", self.i).fetchall()
            except Exception:
                flag = False
            self.i = self.i + 1
        try:
            di = self.cur.execute("""SELECT id FROM users WHERE login = ?""", self.name).fetchall()
            flag = False
        except Exception:
            flag = True
        if self.name.isalnum() and flag:
            with open(self.nameofphoto, 'rb') as file:
                self.nameofphoto = file.read()
            self.cur.execute("""INSERT INTO users(id, login, password, photo) VALUES(?, ?, ?, ?)""", (self.i, self.name,
                                                                                                      self.passw,
                                                                                                      self.nameofphoto))
            self.con.commit()
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
            password = self.cur.execute("""SELECT password FROM users WHERE login = ?""", self.name).fetchall()[0]
            i = self.cur.execute("""SELECT id FROM users WHERE login = ?""", self.name).fetchall()[0]
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


class Error(QMainWindow, Ui_errorwindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Kontrless(QMainWindow, Ui_kontrless):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Teor1(QMainWindow, Ui_teor1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Teor2(QMainWindow, Ui_teor2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Teor3(QMainWindow, Ui_teor3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Pract1(QMainWindow, Ui_pract1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Pract2(QMainWindow, Ui_pract2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


class Pract3(QMainWindow, Ui_pract3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)  # окно без рамки
        self.setAttribute(Qt.WA_TranslucentBackground)  # форма прозрачная
        self.closebutton.clicked.connect(self.close)
        self.layout().addWidget(self.closebutton)  # кнопочка закрытия окна и завершения программы


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Authorize()
    ex.show()
    sys.exit(app.exec())
