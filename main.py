from base import Doc
from io2.inventarios import Inventario
from io2.descuentos import Descuento
from sympy.abc import p as s_p
from sympy import oo
# ----------------------------------------------- Main -----------------------------------------

ej0 = Descuento('Ejercicio 0',p=25,c3=50,r=3000,c1=0.3*s_p,
                prices=[((0,39),s_p),((40,69),0.9*s_p),((70,oo),0.85*s_p)])
ej1 = Inventario('Ejercicio 1',r=round(20000/12,4),k=2500, c1=0.15, c2=20/12, c3=500)
ej2 = Inventario('Ejercicio 2',r=600, k=48*30, c1=round(0.05/12,4), c3=750)
doc = Doc('tarea1')
doc.append(ej0)
doc.append(ej1)
doc.append(ej2)
doc.save()
