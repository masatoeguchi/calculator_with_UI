
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
import re

class Test(QtWidgets.QWidget):


    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):

        self.cal_list = []
        self.decimal_count = 0

        self.setWindowTitle("Calculator")
        self.setGeometry(50, 50, 250, 270)

        self.display = QtWidgets.QTextEdit()
        # self.display.setText("Hello World!")


        self.display.setMaximumHeight(100)

        self.windowLayout = QtWidgets.QVBoxLayout()

        self.windowLayout.addWidget(self.display)
        self.setLayout(self.windowLayout)

        # self.horizontalGroupBox = QtWidgets.QGroupBox("Grid")
        # layout = QtWidgets.QGridLayout()
        # self.setLayout(layout)

        # layout.setColumnStretch(1, 4)
        # layout.setColumnStretch(2, 4)

        self.createGridLayout()

        self.btn1.clicked.connect(self.input)
        self.btn2.clicked.connect(self.input)
        self.btn3.clicked.connect(self.input)
        self.btn4.clicked.connect(self.input)
        self.btn5.clicked.connect(self.input)
        self.btn6.clicked.connect(self.input)
        self.btn7.clicked.connect(self.input)
        self.btn8.clicked.connect(self.input)
        self.btn9.clicked.connect(self.input)
        self.btn0.clicked.connect(self.input)
        self.btnDecimal.clicked.connect(self.input)
        self.btnPlus.clicked.connect(self.input)
        self.btnMinus.clicked.connect(self.input)
        self.btnMultiple.clicked.connect(self.input)
        self.btnDivide.clicked.connect(self.input)
        self.btnEqual.clicked.connect(self.dentaku)
        self.btnClear.clicked.connect(self.clear_value)
        self.btnBackSpace.clicked.connect(self.back_space)


        # self.btnPlus.clicked.connect(self.add_valuePlus)
        # self.btnMinus.clicked.connect(self.add_valueMinus)
        # self.btnMultiple.clicked.connect(self.add_valueMultiple)
        # self.btnDivide.clicked.connect(self.add_valueDivide)
        # self.btnEqual.clicked.connect(self.add_valueEqual)
        # self.btnClear.clicked.connect(self.add_valueClear)
        #

        # self.layout.resize(self.layout.sizeHint());
        self.show()

    # def onClicked(self):
    #     print(self.sender().text())

    def dentaku(self):

        print(self.cal_list)

        self.cal_list = re.split(r'([-|+|*|/])', self.tempStr)
        print(self.cal_list)

        # for i in self.tmp_list:
        #     self.cal_list.append(int(self.tmp_list[i]))

        # self.cal_list = re.split(r'([\/*-+\s*])', cal_list)
        # print(cal_list)
        # x = list(filter(None, cal_list))
        # print(x)
        #
        # for value in x:
        #     if value == " " or value == "":
        #         x.remove(value)

        # for i in range(len(x)):
        #     if x[i] != '4' and x[i] != '5' and x[i] != '+':
        #         print(type(x[i]))
        #         x.pop(i)
        #         print("Current:", x)

        # regex = re.compile('\D')
        # for value in x:
        #     if regex.match(value):
        #         x.remove(value)
        #         print("Current: ", x)

        # print(x)


        x0 = float((self.cal_list[0]))
        x1 = self.cal_list[1]
        x2 = float((self.cal_list[2]))

        def add(x, y):
            return x + y

        def substract(x, y):
            return x - y

        def multiple(x, y):
            return x * y

        def divide(x, y):
            return x / y

        def calculate(x, y, z):
            if y == "+":
                return add(x, z)

            elif y == "-":
                return substract(x, z)

            elif y == "*":
                return multiple(x, z)

            elif y == "/" and z != 0:

                return (divide(x, z))

            elif y == "/" and z == 0:

                return "ZeroDivisionError"

            else:
                print("error")

        self.result = (calculate(x0, x1, x2))

        if x1 == "/" and x2 == 0:

            print(self.result)
            self.cal_list.clear()

            self.decimal_count = 0

            self.display.setText(str(self.result))

        else:
            result = float(self.result)

            print(result)

            if result % 1 == 0:
                result = int(result)

            if result < 0 and result % 1 != 0:
                result = float(result)

            self.result = (round(result, 4))

            self.cal_list.clear()

            self.decimal_count = 0

            self.cal_list.append(str(self.result))

            self.display.setText(str(self.result))



    # app = QtGui.QApplication(sys.argv)
    #
    # window = QtGui.QWidget()
    # window.setGeometry(50, 50, 500, 300)
    # window.setWindowTitle("calculator")
    #
    # window.show()

    def clear_value(self):

        self.cal_list.clear()
        self.display.setText(''.join(self.cal_list))


    def input(self):

        self.tempStr = self.display.toPlainText()

        self.user_input = str(self.sender().text())

        if ((self.user_input == "+") or (self.user_input == "-") or (self.user_input == "*") or (self.user_input == "/")) and \
                ((self.tempStr[-1] == "+") or (self.tempStr[-1] == "-") or (self.tempStr[-1] == "*") or (self.tempStr[-1] == "/")):
            self.tempStr = self.tempStr[:-1]

        if self.check_bugs() == False:

            self.tempStr += self.user_input
            self.display.setText(self.tempStr)

    def back_space(self):

        self.tempStr = self.tempStr[:-1]
        print(self.tempStr)
        self.display.setText(self.tempStr)
        # def make_value(self):
    #     pass

        # if re.match(r'[0-9]', self.sender().text()):
        #     self.num_input()
        #
        # if re.match(r'[-|+|*|/]', self.sender().text()):
        #     self.cal_list.append(self.tmp_value_list[0])
        #     self.tmp_list.clear()
        #     self.tmp_value_list.clear()
        #
        #     self.operator_input()

    # def num_input(self):
    #     self.tmp_list.append(self.sender().text())
    #     self.tmp_value = ''.join(self.tmp_list)
    #     self.tmp_value_list.append(self.tmp_value)
    #     print(self.tmp_value)
    #
    #
    # def operator_input(self):
    #
    #     self.cal_list.append(self.sender().text())
    #     print(self.cal_list)

    def createGridLayout(self):

        self.layout = QtWidgets.QGridLayout()

        self.btn1 = QtWidgets.QPushButton("1")
        self.btn2 = QtWidgets.QPushButton("2")
        self.btn3 = QtWidgets.QPushButton("3")
        self.btn4 = QtWidgets.QPushButton("4")
        self.btn5 = QtWidgets.QPushButton("5")
        self.btn6 = QtWidgets.QPushButton("6")
        self.btn7 = QtWidgets.QPushButton("7")
        self.btn8 = QtWidgets.QPushButton("8")
        self.btn9 = QtWidgets.QPushButton("9")
        self.btn0 = QtWidgets.QPushButton("0")
        self.btnDecimal = QtWidgets.QPushButton(".")
        self.btnPlus = QtWidgets.QPushButton("+")
        self.btnMinus = QtWidgets.QPushButton("-")
        self.btnMultiple = QtWidgets.QPushButton("*")
        self.btnDivide= QtWidgets.QPushButton("/")
        self.btnClear = QtWidgets.QPushButton("C")
        self.btnEqual = QtWidgets.QPushButton("=")
        self.btnBackSpace = QtWidgets.QPushButton("⬅️")

        self.layout.addWidget((self.btn1), 2, 0)
        self.layout.addWidget((self.btn2), 2, 1)
        self.layout.addWidget((self.btn3), 2, 2)
        self.layout.addWidget((self.btn4), 1, 0)
        self.layout.addWidget((self.btn5), 1, 1)
        self.layout.addWidget((self.btn6), 1, 2)
        self.layout.addWidget((self.btn7), 0, 0)
        self.layout.addWidget((self.btn8), 0, 1)
        self.layout.addWidget((self.btn9), 0, 2)
        self.layout.addWidget((self.btn0), 3, 1)
        self.layout.addWidget((self.btnPlus), 0, 3)
        self.layout.addWidget((self.btnMinus), 1, 3)
        self.layout.addWidget((self.btnMultiple), 2, 3)
        self.layout.addWidget((self.btnDivide), 3, 3)
        self.layout.addWidget((self.btnClear), 4, 2)
        self.layout.addWidget((self.btnEqual), 3, 0)
        self.layout.addWidget((self.btnDecimal), 3, 2)
        self.layout.addWidget((self.btnBackSpace), 4, 3)

        # self.vbox = QtWidgets.QVBoxLayout()
        # self.vbox.addWidget(self.display)

        self.windowLayout.addLayout(self.layout)

    # def de_bugger1(self):
    #     print(self.tempStr[-1:])
    #     if (self.tempStr[-1:] == "+" or "-" or "*" or "\\/\\" and \
    #         self.user_input == "+" or "-" or "*" or "\\/\\"):
    #
    #         self.tempStr = self.tempStr[:-1]
    #         print(self.tempStr)

    def check_bugs(self):


        self.clear_decimal_count()

        if self.user_input == "." and self.decimal_count == 0:
            self.decimal_count += 1
            return False

        elif self.user_input == "." and self.decimal_count == 1:
            return True

        self.clear_decimal_count()

        if ((self.user_input == "+") or (self.user_input == "-") or (self.user_input == "*") or (self.user_input == "/")) and \
                ((self.tempStr.count('+')) + (self.tempStr.count('-')) + (self.tempStr.count('*')) + (self.tempStr.count('/')) == 1):
            return True

        if ((self.user_input == "+") or (self.user_input == "-") or (self.user_input == "*") or (self.user_input == "/")) and \
                self.tempStr.count('+') + self.tempStr.count('-') + self.tempStr.count('*') + self.tempStr.count('/') == 1:
            return True

        return False

    # def check_decimal_number(self):
    #
    #     self.clear_decimal_count()
    #
    #     if self.user_input == "." and self.decimal_count == 0:
    #         self.decimal_count += 1
    #         return False
    #
    #     elif self.user_input == "." and self.decimal_count == 1:
    #         return True


        #     if self.decimal_count == 0:
        #         self.decimal_count += 1
        #         return False
        #     elif self.decimal_count == 1:
        #         return True
        # else:
        #     return False



    def clear_decimal_count(self):
        if (self.user_input == "+") or (self.user_input == "-") or (self.user_input == "*") or (self.user_input == "/"):
                self.decimal_count = 0

    def check_operator_number(self):
        self.tempStr.count('+') + self.tempStr.count('-') + self.tempStr.count('*') + self.tempStr.count('/') == 1



        # if bad, give True

        # if self.user_input == re.search(r'/d', self.tempStr[-1:]):



        #
        # if (self.user_input == "+") or (self.user_input == "-") or (self.user_input == "*") or (self.user_input == "/"):
        #
        #     self.decimal_count = 0
        # # if (self.tempStr[-1:] == "." and self.user_input == "."):
        #
        # if self.decimal_count >= 2:
        #     """if there is decimal after last operator, do not get 'sender' """
        #     return True
        # else:
        #     return False


    # def check_decimal(self):
    #     if self.user_input == ".":
    #
    #         if self.decimal_count == 0:
    #             self.decimal_count += 1
    #             return False
    #         elif self.decimal_count == 1:
    #             return True
    #     else:
    #         return False
    #
    #     if (self.user_input == "+") or (self.user_input == "-") or (self.user_input == "*") or (self.user_input == "/"):
    #         self.decimal_count = 0
    #
    #






if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    test = Test()
    sys.exit(app.exec_())