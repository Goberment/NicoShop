from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=500, height=400)
miFrame.pack()

cuadroTexto=Entry(miFrame)
cuadroTexto.grid(row=0, column=1)

nombreLabel=Label(miFrame, text="Nombre")
nombreLabel.grid(row=0,column=0)

raiz.mainloop()