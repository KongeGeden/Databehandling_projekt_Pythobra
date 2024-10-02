import sys
import PySide6.QtWidgets as QW
import pythobra_backend
import pythobra_frontend

import sympy as sp


class PythobraApp:
    def __init__(self):
        self.frontend = pythobra_frontend.PythobraMainWindow()
        self.backend = pythobra_backend.PythobraBackend()

        self.frontend.solve_equation_button.clicked.connect(self.solve_equation)

        self.frontend.settings_button.clicked.connect(self.open_settings_dialog)
        self.frontend.triangle_solver.clicked.connect(self.triangle_solver)

    def solve_equation(self):
        equation = self.frontend.equation_text_field.text()
        variable = self.frontend.variable_text_field.text()
        result = self.backend.solve_equation(equation, variable)
        self.frontend.output_text_field.appendPlainText(result)

    def open_settings_dialog(self):
        self.settings_dialog = pythobra_frontend.SettingsDialog()
        self.settings_dialog.open()
        self.settings_dialog.accepted.connect(self.update_settings)
        self.settings_dialog.rejected.connect(self.cancel_settings)

    def update_settings(self):
        self.frontend.output_text_field.appendPlainText(
            "Oh yeah, I like being Rickrolled!"
        )

    def cancel_settings(self):
        self.frontend.output_text_field.appendPlainText(
            "No more Rickrolling. Get me out of here!"
        )
    def triangle_solver(self):
        self.triangle_solver_interface = pythobra_frontend.Triange_solver_class()
        widget=self.triangle_solver_interface
        widget.show()
        self.triangle_solver_interface.button_løs_trekant.clicked.connect(self.triangle_solver_2)
    
    def triangle_solver_2(self):
        #værdier=
        print(self.triangle_solver_interface.giv_værdier())
        nye_værdier=self.backend()
        
        #self.triangle_solver_interface.pen()

if __name__ == "__main__":
    qt_app = QW.QApplication.instance()
    if qt_app == None:
        qt_app = QW.QApplication(sys.argv)
    pythobra_app = PythobraApp()
    pythobra_app.frontend.show()
    qt_app.exec()
