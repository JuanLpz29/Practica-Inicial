import os
if os.name == "nt": #en Windows es necesario este dll, instalado para weasyprint
    os.add_dll_directory("C:/Program Files/GTK3-Runtime Win64/bin")

from weasyprint import HTML

print("Generando Pdf's")
#2 Introduccion
HTML('./introduccion.html').write_pdf("./introduccion.pdf")
print("\t2_introduccion Generada")

print("PDF Generado")
