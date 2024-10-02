import sys
import PySide6.QtWidgets as QW
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.figure import Figure
from PySide6.QtGui import QMovie,QBrush,QPen,QColor,QPolygonF,QPainter
import webbrowser
import math
from PySide6.QtCore import QPointF,QPoint



class PythobraMainWindow(QW.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pythobra")
        main_widget = QW.QWidget()
        self.setCentralWidget(main_widget)
        vertical_layout = QW.QVBoxLayout()
        horizontal_layout = QW.QHBoxLayout()
        main_widget.setLayout(vertical_layout)

        vertical_layout.addLayout(horizontal_layout)

        equation_label = QW.QLabel("Equation: ")
        horizontal_layout.addWidget(equation_label)

        self.equation_text_field = QW.QLineEdit()
        horizontal_layout.addWidget(self.equation_text_field)

        variable_label = QW.QLabel("Solve for: ")
        horizontal_layout.addWidget(variable_label)

        self.variable_text_field = QW.QLineEdit()
        horizontal_layout.addWidget(self.variable_text_field)

        self.solve_equation_button = QW.QPushButton("Solve equation")

        horizontal_layout.addWidget(self.solve_equation_button)

        horizontal_layout_2 = QW.QHBoxLayout()
        self.triangle_solver = QW.QPushButton("Triange solver")
        vertical_layout.addWidget(self.triangle_solver)
        vertical_layout.addLayout(horizontal_layout_2)

        output_label = QW.QLabel("Output")
        horizontal_layout_2.addWidget(output_label)

        horizontal_layout_2.addStretch()

        self.settings_button = QW.QPushButton("Settings")
        horizontal_layout_2.addWidget(self.settings_button)

        self.output_text_field = QW.QPlainTextEdit()
        self.output_text_field.setReadOnly(True)
        vertical_layout.addWidget(self.output_text_field)


class SettingsDialog(QW.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.vertical_layout = QW.QVBoxLayout()
        self.setLayout(self.vertical_layout)
        settings_movie = QMovie("img/settings.gif")
        settings_label = QW.QLabel()
        settings_label.setMovie(settings_movie)
        settings_movie.start()
        self.vertical_layout.addWidget(settings_label)
        self.vertical_layout.addWidget(
            QW.QLabel(
                "You got Rickrolled! You better read the source code before blindly running any code!"
            )
        )
        button_box = QW.QDialogButtonBox(
            QW.QDialogButtonBox.Ok | QW.QDialogButtonBox.Cancel
        )
        self.vertical_layout.addWidget(button_box)

        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        webbrowser.open(
            "https://ia801509.us.archive.org/10/items/Rick_Astley_Never_Gonna_Give_You_Up/Rick_Astley_Never_Gonna_Give_You_Up.ogv"
        )
class Triange_solver_class(QW.QWidget):
    def __init__(self, parent=None):
        QW.QWidget.__init__(self, parent)
        self.setWindowTitle("Triangle solver")
        self.vertical_layout = QW.QVBoxLayout()
        self.setLayout(self.vertical_layout)
        #Pen der virker på en måde
        self.pen = QPen(QColor(0, 0, 0))  # set lineColor
        self.pen.setWidth(3)  # set lineWidth
        self.brush = QBrush(QColor(255, 255, 255, 255))  # set fillColor
        self.polygon = self.createPoly(150, 200, 250,1,29,150)



    def createPoly(self,a,b,c,A,B,C):
        trekant=QPolygonF()
        k=100


        point1=QPointF(0+k,0+k)
        point2=QPointF(0+k,a+k)
        point3=QPointF(b*math.cos(A)+k,b*math.cos(A)+k)
        trekant.append(point1)
        trekant.append(point2)
        trekant.append(point3)



        a_text= Trekant_label("a=",self)
        print(a_text)
        a_text.move(int(point1.x()), int(point1.y()))
        print(a_text.x)



        return trekant

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPolygon(self.polygon)

class Trekant_label(QW.QWidget):
    def __init__(self,navn,vindue,parent=None):
        super().__init__(parent)
        layout = QW.QHBoxLayout(self)
        self._label = QW.QLabel(navn,self)
        layout.addWidget(self._label)

        self._lineeidt = QW.QLineEdit(self)
        layout.addWidget(self._lineeidt)
        self.setLayout(layout)
    def print_test(self):
        print((self._lineeidt.text()))
