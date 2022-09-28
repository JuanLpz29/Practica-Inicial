'''
Librerias reportlab a usar:
'''
from reportlab.platypus import (SimpleDocTemplate, PageBreak, Image, Spacer,
Paragraph, Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

'''
Clase que genera la tabla
'''
class TableKeyConcepts:

    def __init__(self, data, size):
        self._data = data
        self._style = [
                    ('GRID',(0,0),(-1,-1),0.5,colors.grey),
                    ('BOX',(0,0),(-1,-1),2,colors.black),
                    ('BACKGROUND', (0, 0), (-1, 0), colors.pink),
                    ]
        if size > len(data):
            self._size = len(data)
        elif size <= 0:
            self._size = 0
        else:
            self._size = size
        return

    @property
    def data(self):
        return self._data

    @property
    def style(self):
        return self._style

    @property
    def size(self):
        return self._size

    
    def createTable(self):
        #Se pasa el diccionario a una lista
        concept_list = zip(self._data.keys(), self._data.values())
        concept_list = list(concept_list)
        #Separa lista por la mitad para generar tabla de 4 columnas.
        concept_list_divided = []
        #tamano = int(len(lista_conceptos)/2)
        size = int(self._size/2)
        concept_list_divided.append(['Concepto', 'Cantidad', 'Concepto', 'Cantidad'])
        for i in range(size):
            concept_list_divided.append(concept_list[i] + concept_list[size + i])
        data = concept_list_divided
        table = Table(data = data, style = self._style)
        return table
