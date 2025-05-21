from tkinter import *

raiz=Tk()
raiz.title("NicoShop")
##raiz.resizable(True, False)
#raiz.geometry("650x350")
raiz.config(bg="cyan")

miFrame=Frame()
miFrame.pack(fill="both", expand=True)
miFrame.config(bg="white")
miFrame.config(width="650", height="350")
miFrame.config(bd="20")
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")



raiz.mainloop()
