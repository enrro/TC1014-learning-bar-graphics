'''
Created on 03/09/2014

@author: A01221672
'''
from Tkinter import*
import math
ventana = Tk()
lienzo =Canvas(ventana, width=400, height=400)
lienzo.pack()

fanslocal= 4706129*1.0
fansTotal = 97114292*1.0
Fanstwitter= 29500531*1.0
PL = (fanslocal/fansTotal)
PT = Fanstwitter/fansTotal
RL = 200-(180*PL)
RT = 200-(180*PT)

lienzo.create_line(5,0,5,200)
lienzo.create_line(5,200,200,200)
lienzo.create_text(300,180, text = "Cristiano ronaldo \n en Estados Unidos", width = 0)
lienzo.create_rectangle(10, 200, 60, RL, fill= "#15011A", width = 0)
lienzo.create_rectangle(70, 200, 120, 20, fill= "#15011A", width = 0)
lienzo.create_rectangle(130, 200, 180, RT, fill= "#15011A", width = 0)
mainloop()