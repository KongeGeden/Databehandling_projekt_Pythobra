import sys
import PySide6.QtWidgets as QW
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtGui import QMovie,QBrush,QPen,QColor,QPolygonF,QPainter
import webbrowser
import math
from PySide6.QtCore import QPointF,QPoint



class App(QW.QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt absolute positioning - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 440
        self.height = 280
        self.initUIdsdsdsd()

    def initUIdsdsdsd(self):
        self.setWindowTitle(self.title)


        label = QW.QLabel('Python', self)
        label.move(50, 50)

        label2 = QW.QLabel('PyQt5', self)
        label2.move(100, 100)

        label3 = QW.QLabel('Examples', self)
        label3.move(150, 150)

        label4 = QW.QLabel('pythonspot.com', self)
        label4.move(200, 200)

        self.show()


if __name__ == '__main__':
    app = QW.QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())