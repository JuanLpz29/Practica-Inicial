from ctypes import alignment
#from turtle import width
from matplotlib.pyplot import text
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

#medidas 

width, height = legal

#nombre del archivo pdf de salida
c = canvas.Canvas("intro.pdf", pagesize = legal) 

c.drawImage('logo_gore_horizontal.png', 10, 950, width = 140, height = 50 ,preserveAspectRatio=True, mask=[0,0,0,0,0,0])
c.drawImage('logo_sophia2.png', 460, 950, width = 140, height = 50,preserveAspectRatio=True, mask=[0,0,0,0,0,0])


#Fuentes disponibles: ['Courier', 'Courier-Bold', 'Courier-BoldOblique', 'Courier-Oblique', 'Helvetica', 'Helvetica-Bold', 'Helvetica-BoldOblique', 'Helvetica-Oblique', 'Symbol', 'Times-Bold', 'Times-BoldItalic', 'Times-Italic', 'Times-Roman', 'ZapfDingbats']

# Registrando la fuente Gill Sans
pdfmetrics.registerFont(TTFont('GillSans', 'gillSans.ttf'))
pdfmetrics.registerFont(TTFont('GillSansBold', 'gillSansBold.ttf'))

#fuentes = c.getAvailableFonts()

#print(fuentes)

#imagenes



#texto en posicion deseada pos X, Y por puntos, 1 pt = 1/72 pulgadas

c.setFont('GillSans', 12)
c.drawString(180,970,"Percepción mediática de los problemas territoriales")

c.setFont('GillSansBold', 27)
c.drawString(70,900,"I. Introduccion")


style = ParagraphStyle('p1',
fontName = 'GillSans', #tipo de letra
fontSize = 12, #tamaño de letra
leading = 15, #interlineado
leftIndent = 5)

#primer parrafo
p1 = Paragraph ('''Los informes de "Percepción mediática de las problemáticas territoriales" proponen una síntesis
periódica de las problemáticas identificadas y emergentes del territorio a través del análisis
automatizada de los medios de prensa regionales. Estos informes tienen tres ventajas para
acompañar el equipo del gobierno regional en este trabajo:
''', style)

p1.wrapOn(c,470,50)
p1.drawOn(c, width-540, height-200)


#segundo parrafo
textoP2 = ["1. Optimizan el tiempo del equipo entregando un resumen operativo de las problemáticas territoriales en el periodo,","2. Refuerzan el conocimiento del equipo destancando problemáticas emergentes aún no identificadas,","3. Son flexibles. El equipo puede definir la periodicidad del informe e identificar problemáticas territoriales específicas que monitorear."]
num = 0
for i in textoP2:
    p2 = Paragraph('''{}'''.format(i), style)
    p2.wrapOn(c,470,50)
    p2.drawOn(c,width - 540 , height - 240-num)
    num+= 40
p3 = Paragraph(''' El presente informe de demostración ilustra la estructura del informe. En primer lugar, se detalla cuál es la metodología para elaborar el informe. Luego, por cada problemática territorial identificada se propone un conjunto de indicadores que resumen los conceptos claves y noticias claves de la problemática, a qué comunas corresponde esta problemática y cómo evoluciona en el tiempo.''', style)
p3.wrapOn(c,470,50)
p3.drawOn(c, width - 540, height - 400)

'''text2 = c.beginText(50, height - 250)
text2.setFont("GillSans", 12)
text2.textLines("1. Optimizan el tiempo del equipo entregando un resumen operativo de las problemáticas territoriales en el periodo,\n2. Refuerzan el conocimiento del equipo destancando problemáticas emergentes aún no identificadas,\n3. Son flexibles. El equipo puede definir la periodicidad del informe e identificar problemáticas territoriales específicas que monitorear. El presente informe de demostración ilustra la estructura del informe. En primer lugar, se detalla cuál es la metodología para elaborar el informe. Luego, por cada problemática territorial identificada se propone un conjunto de indicadores que resumen los conceptos claves y noticias claves de la problemática, a qué comunas corresponde esta problemática y cómo evoluciona en el tiempo.")
c.drawText(text2)'''
c.save()

