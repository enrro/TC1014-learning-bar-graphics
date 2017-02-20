'''
Created on 03/09/2014

@author: A01221672
'''

def PromedioPersonas(personasTotal,personasMuestra):
    relacion = personasMuestra/personasTotal
    return 200-180*relacion

def fondo():
    lienzo.create_line(5,0,5,200)
    lienzo.create_line(5,200,200,200)

def textos(compania,pais):
    lienzo.create_text(300,180, text = compania + "\n" + " en "+ pais, width = 0)

def AlturaBarras(barraA,barraC):
    lienzo.create_rectangle(10, 200, 60, barraA, fill= "#15011A", width = 0)
    lienzo.create_rectangle(70, 200, 120, 20, fill= "#15011A", width = 0)
    lienzo.create_rectangle(130, 200, 180, barraC, fill= "#15011A", width = 0)

def Grafico(fansTotal,fansLocales,fansTwitter,compania,pais):
    fondo()
    textos(compania,pais)
    barraTwitter = PromedioPersonas(fansTotal,fansTwitter)
    barraLocales = PromedioPersonas(fansTotal,fansLocales)
    AlturaBarras(barraLocales,barraTwitter)

from Tkinter import*

ventana = Tk()
lienzo =Canvas(ventana, width=400, height=400)
lienzo.pack()

fans = [32096269.0,34691090.0,568491.0]

Grafico(fans[1],fans[0],fans[2],"Walmart","Mexico")
mainloop()
