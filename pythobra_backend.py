import sympy as sp
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
import math

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

    def triangle_solver(self,side_liste,vinkel_liste):
        vinkler_kendt=3-vinkel_liste.count("")
        sider_kendt=3-side_liste.count("")
        if vinkler_kendt==2:
            vinkel_liste=self.sidste_vinkel(vinkel_liste)
        #Laver et loop der lopper over de forskellige kombtionationer
        
        plus_ting1=0
        plus_ting2=0
        for i in range(3):
            plus_ting1=i+1
            plus_ting2=i+2
            if i+1>2:
                plus_ting1=i+1-3
            if i+2>2:
                plus_ting1=i+1-2
            
            if side_liste[0+i]!="" and side_liste[plus_ting1]!="" and vinkel_liste[0+i]!="":
                vinkel_liste[plus_ting1]=self.sinus_reletion(side_liste[0+i],side_liste[plus_ting1],vinkel_liste[0+i],True)
                vinkel_liste=self.sidste_vinkel(vinkel_liste)
                side_liste[plus_ting2]=self.sinus_reletion(side_liste[0+i],vinkel_liste[0+i],vinkel_liste[plus_ting2],False)
                
                return "ting"
        
        for i in range(3):
            plus_ting1=i+1
            plus_ting2=i+2
            if i+1>2:
                plus_ting1=i+1-3
            if i+2>2:
                plus_ting1=i+1-2   
            if side_liste[0+i]!="" and side_liste[plus_ting1]!="" and vinkel_liste[plus_ting2]!="":
                side_liste[plus_ting2]=self.cos_releation(side_liste[0+i],side_liste[plus_ting1],vinkel_liste[plus_ting2])
                vinkel_liste[0+i]=self.sinus_reletion(side_liste[plus_ting2],vinkel_liste[plus_ting2],side_liste[plus_ting1],True)
                vinkel_liste=self.sidste_vinkel(vinkel_liste) 
                return 2
        
        for i in range(3):
            plus_ting1=i+1
            plus_ting2=i+2
            if i+1>2:
                plus_ting1=i+1-3
            if i+2>2:
                plus_ting1=i+1-2   
            if side_liste[0+i]!="" and vinkel_liste[plus_ting1]!="" and vinkel_liste[plus_ting2]!="":
                side_liste[plus_ting1]=self.sinus_reletion(side_liste[0+i],vinkel_liste[i],vinkel_liste[plus_ting1],False)
                side_liste[plus_ting2]=self.sinus_reletion(side_liste[plus_ting1],vinkel_liste[plus_ting1],vinkel_liste[plus_ting2],False)
        
        
    def sinus_reletion(self,kendt_side,kendt_vinkel,kendt_side_eller_vinkel_2,to_kendte_sider=True):
        unkendt=0
        if to_kendte_sider:
            unkendt=math.asin((kendt_side/math.sin(kendt_vinkel))/kendt_side_eller_vinkel_2)
        else:
            unkendt=((kendt_side*math.sin(kendt_side_eller_vinkel_2))/math.sin(kendt_vinkel))
        return unkendt
        
    def cos_releation(self,tal_1,tal_2,vinkel):
        ukendt=math.sqrt(tal_1**2+tal_2**2)-2*tal_1*tal_2*math.cos(vinkel)
        return ukendt
    
    def sidste_vinkel(self,liste):
        if liste[0]=="":
            liste[0]= 180-liste[1]-liste[2]
        elif liste[1]=="":
            liste[1]= 180-liste[0]-liste[2]
        elif liste[2]=="":
            liste[2]= 180-liste[0]-liste[1]
        else:
            return liste
        
        
        
        
