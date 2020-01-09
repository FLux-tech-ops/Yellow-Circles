from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randint
import sys


class Circles(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.drawCircle)
        self.show()

    def paintEvent(self, e):
        QWidget.paintEvent(self, e)
        qp = QPainter()
        qp.begin(self)
        qp.setPen(QColor(255, 211, 0))
        r = randint(30, 360)
        qp.drawEllipse(randint(100, 450), randint(100, 450), r, r)
        qp.end()

    def drawCircle(self):
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Circles()
    sys.exit(app.exec_())
