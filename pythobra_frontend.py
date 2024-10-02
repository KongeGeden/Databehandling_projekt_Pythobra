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
        #self.vertical_layout = QW.QVBoxLayout()
        #self.setLayout(self.vertical_layout)
        #Pen der virker på en måde
        self.pen = QPen(QColor(0, 0, 0))  # set lineColor
        self.pen.setWidth(3)  # set lineWidth
        self.brush = QBrush(QColor(255, 255, 255, 255))  # set fillColor
        self.polygon = self.createPoly(150, 200, 250,1,29,150)
        
        self.layout=QW.QVBoxLayout(self)
        self.button_løs_trekant=QW.QPushButton("Beregn trekant",self)
        self.layout.addWidget(self.button_løs_trekant)
        
        



    def createPoly(self,a,b,c,A,B,C):
        trekant=QPolygonF()
        k=100


        point1=QPointF(0+k,0+k)
        point2=QPointF(0+k,a+k)
        point3=QPointF(b*math.cos(A)+k,b*math.cos(A)+k)
        trekant.append(point1)
        trekant.append(point2)
        trekant.append(point3)



        self.a_text= Trekant_label("a=",self)
        self.A_text=Trekant_label("A=",self)
        self.a_text.move(int(point1.x()), int(point1.y()))
        self.A_text.move(int(point1.x()), int(point1.y())-self.a_text.height())
        #b
        self.b_text= Trekant_label("b=",self)
        self.B_text=Trekant_label("B=",self)
        self.b_text.move(int(point2.x()), int(point2.y()))
        self.B_text.move(int(point2.x()), int(point2.y())-self.b_text.height())
        #c
        self.c_text= Trekant_label("c=",self)
        self.C_text=Trekant_label("C=",self)
        self.c_text.move(int(point3.x()), int(point3.y()))
        self.C_text.move(int(point3.x()), int(point3.y())-self.c_text.height())
        self.liste_af_vinkler=[self.A_text,self.B_text,self.C_text]
        self.liste_af_sider=[self.a_text,self.b_text,self.c_text]
        

        return trekant

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.setBrush(self.brush)
        painter.drawPolygon(self.polygon)
    
    def giv_værdier(self):
        self.værdi_vinker=[]
        self.værdi_sider=[]
        #Tag vinkler og værider og gpår mehtondern der tag ting af boksen
        for tal in self.liste_af_vinkler:
            tal=tal.tag_værdi()
            self.værdi_vinker.append(tal)
        
        for tal in self.liste_af_sider:
            tal=tal.tag_værdi()
            self.værdi_sider.append(tal)
        return self.værdi_sider,self.værdi_vinker
        

class Trekant_label(QW.QWidget):
    def __init__(self,navn,parent=None):
        super().__init__(parent)
        layout = QW.QHBoxLayout(self)
        self._label = QW.QLabel(navn,self)
        layout.addWidget(self._label)

        self._lineedit = QW.QLineEdit(self)
        layout.addWidget(self._lineedit )
        self.setLayout(layout)
    def tag_værdi(self):
        return self._lineedit.text()
