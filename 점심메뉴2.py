import pandas as pd
import random
import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()



    def setupUI(self):

        self.setWindowTitle("QT 개발팀 점심 메뉴 고르기 !!!")
        self.setGeometry(800, 200, 500, 300)

        textlabel = QLabel(" 오늘의 메뉴... ", self)
        textlabel.move(20, 20)

        self.checkBox1 = QCheckBox("김치찌개", self)
        self.checkBox1.move(20, 50)
        self.checkBox1.resize(150, 30)
        self.checkBox1.stateChanged.connect(self.checkBoxState)

        self.checkBox2 = QCheckBox("왕산", self)
        self.checkBox2.move(20, 70)
        self.checkBox2.resize(150, 30)
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        self.checkBox3 = QCheckBox("돈까스", self)
        self.checkBox3.move(20, 90)
        self.checkBox3.resize(150, 30)
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        self.checkBox4 = QCheckBox("수제비", self)
        self.checkBox4.move(20, 110)
        self.checkBox4.resize(150, 30)
        self.checkBox4.stateChanged.connect(self.checkBoxState)

        self.checkBox5 = QCheckBox("냉모밀", self)
        self.checkBox5.move(20, 130)
        self.checkBox5.resize(150, 30)
        self.checkBox5.stateChanged.connect(self.checkBoxState)

        self.checkBox6 = QCheckBox("국밥", self)
        self.checkBox6.move(20, 150)
        self.checkBox6.resize(150, 30)
        self.checkBox6.stateChanged.connect(self.checkBoxState)

        self.checkBox7 = QCheckBox("쌈밥", self)
        self.checkBox7.move(20, 170)
        self.checkBox7.resize(150, 30)
        self.checkBox7.stateChanged.connect(self.checkBoxState)

        self.checkBox8 = QCheckBox("불고기전골", self)
        self.checkBox8.move(20, 190)
        self.checkBox8.resize(150, 30)
        self.checkBox8.stateChanged.connect(self.checkBoxState)

        self.checkBox9 = QCheckBox("도시락", self)
        self.checkBox9.move(140, 190)
        self.checkBox9.resize(150, 30)
        self.checkBox9.stateChanged.connect(self.checkBoxState)

        self.checkBox10 = QCheckBox("한정식", self)
        self.checkBox10.move(140, 170)
        self.checkBox10.resize(150, 30)
        self.checkBox10.stateChanged.connect(self.checkBoxState)

        self.checkBox11 = QCheckBox("고추짜장", self)
        self.checkBox11.move(140, 150)
        self.checkBox11.resize(150, 30)
        self.checkBox11.stateChanged.connect(self.checkBoxState)

        self.checkBox12 = QCheckBox("왕산", self)
        self.checkBox12.move(140, 130)
        self.checkBox12.resize(150, 30)
        self.checkBox12.stateChanged.connect(self.checkBoxState)

        self.checkBox13 = QCheckBox("제육", self)
        self.checkBox13.move(140, 110)
        self.checkBox13.resize(150, 30)
        self.checkBox13.stateChanged.connect(self.checkBoxState)

        self.checkBox14 = QCheckBox("순두부찌개", self)
        self.checkBox14.move(140, 90)
        self.checkBox14.resize(150, 30)
        self.checkBox14.stateChanged.connect(self.checkBoxState)


        label = QPushButton(" START ", self)
        label.move(180, 250)
        # label.move(130,110)  가운데
        label.clicked.connect(self.label_clicked)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self, result):
        food = ""
        if self.checkBox1.isChecked() == True:
            food += '김치찌개, '
        if self.checkBox2.isChecked() == True:
            food += '왕산, '
        if self.checkBox3.isChecked() == True:
            food += '돈까스, '
        if self.checkBox4.isChecked() == True:
            food += '수제비, '
        if self.checkBox5.isChecked() == True:
            food += '냉모밀, '
        if self.checkBox6.isChecked() == True:
            food += '국밥, '
        if self.checkBox7.isChecked() == True:
            food += '쌈밥, '
        if self.checkBox8.isChecked() == True:
            food += '불고기전골, '
        if self.checkBox9.isChecked() == True:
            food += '도시락, '
        if self.checkBox10.isChecked() == True:
            food += '한정식, '
        if self.checkBox11.isChecked() == True:
            food += '고추짜장, '
        if self.checkBox12.isChecked() == True:
            food += '왕산, '
        if self.checkBox13.isChecked() == True:
            food += '제육, '
        if self.checkBox14.isChecked() == True:
            food += '순두부찌개, '

        self.statusBar.showMessage(food)

        result1 = food.split(',')
        result1 = result1[:-1]
        print(result1)
        self.result = random.choice(result1)





    #@checkBoxState
    def label_clicked(self,result):
        #result = random.choice(food)
        #print(result)

        QMessageBox.about(self, "menu", self.result)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
