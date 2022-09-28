#Librerias reportlab a usar:
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# num_conceptos corresponde al numero de conceptos que desea ver en la tabla.
# el numero ingresado debe ser un numero par.
def generaTabla(diccionario, num_conceptos):
    #Se pasa el diccionario a una lista
    lista_conceptos = zip(diccionario.keys(), diccionario.values())
    lista_conceptos = list(lista_conceptos)

    #Separa lista por la mitad para generar tabla de 4 columnas.
    lista_conceptos_dividida = []
    #tamano = int(len(lista_conceptos)/2)
    tamano = int(num_conceptos/2)
    lista_conceptos_dividida.append(['Concepto', 'Cantidad', 'Concepto', 'Cantidad'])
    for i in range(tamano):
        lista_conceptos_dividida.append(lista_conceptos[i] + lista_conceptos[tamano + i])
    print(lista_conceptos_dividida)

    #Genera documento PDF
    doc = SimpleDocTemplate("test.pdf", pagesize = A4)
    story=[]

    tabla = Table(data = lista_conceptos_dividida,
                            style = [
                                ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                                ('BOX',(0,0),(-1,-1),2,colors.black),
                                ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                                ]
                )
    story.append(tabla)
    story.append(Spacer(0,15))

    doc.build(story)
    return

def main():
    #Diccionario de conceptos claves y sus apariciones
    dic = {'Provincia de osorno' : '18', 'Seremi de agricultura' : '13', 'Provincia de llanquihue' : '12', 'Olimpiadas de actualidad' : '11', 
    'Millones de pesos' : '11', 'Meteorológica de chile' : '8', 'Efectos del cambio' : '8', 'Cantidad de agua' : '8', 
    'Parques de la patagonia' : '7', 'Fin de semana' : '7', 'Municipalidad de puerto' : '7', 'Austral de chile' : '7', 
    'Superintendencia deservicios' : '7', 'Productores de leche' : '7', 'Proyectos de agua' : '7', 'Sur de chile' : '7', 
    'Sur del país' : '7', 'Nacional de leche' : '6', 'Producción de leche' : '6', 'Seremi de salud' : '6'}
    generaTabla(dic, 9)

main()