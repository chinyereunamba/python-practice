# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from random import randint


class Ui_win(object):
    def setupUi(self, win):
        win.setObjectName("win")
        win.setEnabled(True)
        win.resize(440, 440)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding
        )
        self.life: int = 10
        self.hearts: str = "\U0001f5a4" * self.life
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win.sizePolicy().hasHeightForWidth())
        win.setSizePolicy(sizePolicy)
        win.setMinimumSize(QtCore.QSize(440, 440))
        win.setMaximumSize(QtCore.QSize(440, 500))
        win.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(win)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(80, 10, 271, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(18)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.guess_input = QtWidgets.QFrame(self.centralwidget)
        self.guess_input.setGeometry(QtCore.QRect(30, 133, 381, 81))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.guess_input.setFont(font)
        self.guess_input.setFocusPolicy(QtCore.Qt.TabFocus)
        self.guess_input.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.guess_input.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guess_input.setObjectName("guess_input")
        self.guess_input_1 = QtWidgets.QLineEdit(self.guess_input)
        self.guess_input_1.setValidator(QIntValidator())
        self.guess_input_1.setMaxLength(1)
        self.guess_input_1.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_input_1.setGeometry(QtCore.QRect(0, 0, 81, 81))
        self.guess_input_1.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.guess_input_1.setFocus()
        self.guess_input_1.setObjectName("guess_input_1")
        self.guess_input_2 = QtWidgets.QLineEdit(self.guess_input)
        self.guess_input_2.setValidator(QIntValidator())
        self.guess_input_2.setMaxLength(1)
        self.guess_input_2.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_input_2.setGeometry(QtCore.QRect(100, 0, 81, 81))
        self.guess_input_2.setObjectName("guess_input_2")
        self.guess_input_3 = QtWidgets.QLineEdit(self.guess_input)
        self.guess_input_3.setValidator(QIntValidator())
        self.guess_input_3.setMaxLength(1)
        self.guess_input_3.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_input_3.setGeometry(QtCore.QRect(200, 0, 81, 81))
        self.guess_input_3.setObjectName("guess_input_3")
        self.guess_input_4 = QtWidgets.QLineEdit(self.guess_input)
        self.guess_input_4.setValidator(QIntValidator())
        self.guess_input_4.setMaxLength(1)
        self.guess_input_4.setAlignment(QtCore.Qt.AlignCenter)
        self.guess_input_4.setGeometry(QtCore.QRect(300, 0, 81, 81))
        self.guess_input_4.setObjectName("guess_input_4")
        self.check_btn = QtWidgets.QPushButton(self.centralwidget)
        self.check_btn.clicked.connect(self.check)
        self.check_btn.setGeometry(QtCore.QRect(30, 240, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.check_btn.setFont(font)
        self.check_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_btn.setObjectName("check_btn")
        self.life = QtWidgets.QLabel(self.centralwidget)
        self.life.setGeometry(QtCore.QRect(20, 70, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.life.setFont(font)
        self.life.setObjectName("life")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 310, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 350, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        win.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 440, 26))
        self.menubar.setObjectName("menubar")
        win.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(win)
        self.statusbar.setObjectName("statusbar")
        win.setStatusBar(self.statusbar)

        self.guess_input_1.textChanged.connect(
            lambda: self.on_return_pressed(self.guess_input_1)
        )
        self.guess_input_2.textChanged.connect(
            lambda: self.on_return_pressed(self.guess_input_2)
        )
        self.guess_input_3.textChanged.connect(
            lambda: self.on_return_pressed(self.guess_input_3)
        )
        self.guess_input_4.textChanged.connect(
            lambda: self.on_return_pressed(self.guess_input_4)
        )

        self.retranslateUi(win)
        QtCore.QMetaObject.connectSlotsByName(win)

    def retranslateUi(self, win):
        _translate = QtCore.QCoreApplication.translate
        win.setWindowTitle(_translate("win", "MainWindow"))
        self.title.setText(_translate("win", "Guess the Number"))
        self.check_btn.setText(_translate("win", "Check"))
        self.life.setText(_translate("win", self.hearts))
        self.label.setText(_translate("win", "2 numbers are in the right position"))
        self.label_2.setText(
            _translate("win", "1 numbers is correct but in the wrong position")
        )

    def on_return_pressed(self, current_textbox):
        # If the current text box is not empty, set focus to the next text box
        if current_textbox.text():
            if current_textbox is self.guess_input_1:
                self.guess_input_2.setFocus()
            elif current_textbox is self.guess_input_2:
                self.guess_input_3.setFocus()
            elif current_textbox is self.guess_input_3:
                self.guess_input_4.setFocus()
            else:
                # Set focus to the first text box if the current one is the last
                self.guess_input_1.setFocus()

    def check(self):
        self.start()

    def player_guess(self) -> list[int]:
        guess = set(
            [
                int(self.guess_input_1.text()),
                int(self.guess_input_2.text()),
                int(self.guess_input_3.text()),
                int(self.guess_input_4.text()),
            ]
        )

        if self.guess_input_1 is None:
            print("Enter a value")

        return list(guess)

    def generate_number(self) -> list[int]:
        rnd_lst: set = set()

        while len(rnd_lst) < 4:
            rnd_lst.add(randint(0, 9))

        return list(rnd_lst)

    def start(self):
        guess_num = self.generate_number()
        guess = self.player_guess()

        life = 10

        while guess_num != guess and life > 0:
            life -= 1
            has_num: list[int] = list({x for x in guess if x in guess_num})

            match: list[int] = [
                x for x in has_num if guess.index(x) == guess_num.index(x)
            ]

            check: list[int] = list(set(has_num).difference(set(match)))

            if len(match) == 1:
                print(f"{len(match)} number is correct and in the right position")

            elif len(match) > 1:
                print(f"{len(match)} numbers are correct and in the right position")

            if len(check) == 1:
                print(f"{len(check)} number is correct but in the wrong position")

            elif len(check) > 1:
                print(f"{len(check)} numbers are correct but in the wrong position")
            if not match and not has_num:
                print("No number is correct")

            if len(match) == 2 and check not in guess_num:
                next_num = list(set(guess_num).difference(set(check)))
                if next_num[0] % 2 == 0:
                    print("The next number is an even number")
                else:
                    print("The next number is an odd number")

            guess = self.player_guess()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()
    ui = Ui_win()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
