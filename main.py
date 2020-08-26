from base import Doc
from io2.inventarios import Inventario

# ----------------------------------------------- Main -----------------------------------------
ren = Inventario()
doc = Doc('latex-test')
doc.append(ren)
doc.save()
