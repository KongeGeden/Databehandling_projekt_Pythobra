from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt
import sys

class _Bar(QtWidgets.QWidget):
    pass

class Trekant_label(QtWidgets.QWidget):
    """
    Custom Qt Widget to show a power bar and dial.
    Demonstrating compound and custom-drawn widget.
    """

    def __init__(self, navn, *args, **kwargs):
        super(Trekant_label, self).__init__(*args, **kwargs)

        layout = QtWidgets.QHBoxLayout()
        self._label = QtWidgets.QLabel(navn)
        layout.addWidget(self._label)

        self._lineeidt = QtWidgets.QLineEdit()
        layout.addWidget(self._lineeidt)
        self.setLayout(layout)

app = QtWidgets.QApplication(sys.argv)
volume = Trekant_label("a=")
volume.show()
app.exec()