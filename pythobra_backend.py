import sympy as sp
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr

class PythobraBackend:
    def __init__(self):
        pass

    def solve_equation(self, equation, unknown):
        #unknown=sp.Symbol(unknown)
        hvor_mange=equation.count(",")+1
        liste_af_ligninger=[]
        liste_med_uligninge=equation.split(",")
        liste_af_cha=unknown.split(",")
        liste_med_symb=[]
        for cha in liste_af_cha:
            liste_med_symb.append(sp.Symbol(cha))

        #print(unknown)
        for i in range(hvor_mange):
            funktionsstreng, ligemed = liste_med_uligninge[i].split("=")
            #liste_med_første_side.append
            ligning=(parse_expr(funktionsstreng))
            anden_side=(parse_expr(ligemed))
            #iste_med_anden_side.append
            liste_af_ligninger.append(sp.Eq(ligning,anden_side))


        losning = (sp.solve(liste_af_ligninger,liste_med_symb,dict=True))
        return str(losning)
        #return "I må selv finde ud af at få koden til at gøre det rigtige, men jeg skal selvfølgelig nok hjælpe jer. :)"

    def plot_function(
        self,
        mpl_ax,
        function_name,
        function_expression,
        domain_min,
        domain_max,
        color,
        line_style,
        show_name,
        show_legend,
    ):
        pass

    def triangle_solver(self,a,b,c,A,B,C):
        pass
