import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QInputDialog
from PyQt5 import uic
import datetime as dt
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Главное окно.ui', self)
        self.setGeometry(100, 100, 713, 555)
        self.setWindowTitle('Кошелек')
        with open("Info.txt", mode='r', encoding='utf-8') as f:
            str_1 = f.readline()
            self.name = str_1.rstrip('\n')
            self.hello.setText(f'Приветствую, {self.name}!')

            str_2 = f.readline()
            self.score = int(str_2.rstrip('\n'))
            self.balance.setText(f'На вашем счете: {self.score} @')

        self.change_name.clicked.connect(self.run)
        self.notifications.clicked.connect(self.my_event)
        self.add_account.clicked.connect(self.add)
        self.all.clicked.connect(self.my_event)
        self.change_name.clicked.connect(self.my_event)
        self.calculator.clicked.connect(self.my_event)
        self.help.clicked.connect(self.my_event)
        self.investments.clicked.connect(self.my_event)
        self.payment_history.clicked.connect(self.history)

    def my_event(self):
        pass


    def history(self):
        self.history = History(self, 'данных нет')
        self.history.show()


    def run(self):
        name, ok_pressed = QInputDialog.getText(self, " ",
                                                "Введите имя, длинной не более 16 символов")
        if ok_pressed:
            if self.name == name:
                self.statusbar().showMessage(f'Новое имя совпадает с текущим')
            elif len(name) <= 16:
                self.name = name
                self.hello.setText(f'Приветствую, {self.name}!')
                self.save()

    def add(self):
        summ, ok_pressed = QInputDialog.getText(self, "Пополнить счет",
                                                "Добавить на счет:")
        if ok_pressed:
            try:
                self.score += int(summ)
                self.balance.setText(f'На вашем счете: {self.score} @')

                self.save()
            except ValueError:
                self.statusBar().showMessage(f'Неверный формат ввода')


    def save(self):
        with open("Info.txt", mode='w', encoding='utf-8') as g:
            g.write(self.name)
            g.write('\n')
            g.write(str(self.score))


class SecondForm(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Вторая форма')
        self.lbl = QLabel(args[-1], self)
        self.lbl.adjustSize()


class History(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('История платежей.ui', self)
        self.setWindowTitle('История платежей')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
