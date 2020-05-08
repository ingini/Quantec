import pandas as pd
import random
import sys
from PyQt5.QtWidgets import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QT 개발팀 점심 메뉴 고르기 !!!")
        self.setGeometry(400, 300, 350, 300)

        label = QPushButton(" START ",self)
        label.move(130,250)
        #label.move(130,110)  가운데
        label.clicked.connect(self.label_clicked)

        textlabel = QLabel(" 오늘의 메뉴... ", self)
        textlabel.move(20,20)

        self.label = QLabel("뭐가 좋을까?! 시작 ㄱ", self)
        self.label.move(80,40)
        self.label.resize(150,150)

    def label_clicked(self):
        aa = '김치찌개'
        bb = '닭곰탕'
        cc = '수제비'
        dd = '돈까스'
        ee = '국밥'
        ff = '냉모밀'
        gg = '쌈밥'
        hh = '불고기전골'
        ll = '도시락'
        ii = '한정식'
        mm = '고추짜장'
        qq = '왕산'
        uu = '제육'
        oo = '순두부찌개'

        food_list = [aa, bb, cc, dd, ee, ff, gg, hh, ll, ii, mm, qq, uu, oo]

        result = random.choice(food_list)


        QMessageBox.about(self, "menu", result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
