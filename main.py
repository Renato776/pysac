from base import Doc
from io2.inventarios import Inventario

# ----------------------------------------------- Main -----------------------------------------
ren = Inventario('Ejercicio 1',r=5, c1=2, c2=3, c3=5, k=8)
doc = Doc('latex-test')
doc.append(ren)
doc.save()
