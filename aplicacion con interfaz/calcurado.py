from tkinter import *

raiz=Tk()
marco=Frame(raiz)
marco.pack()

pantalla=Entry(marco)
pantalla.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
pantalla.config(background="black",foreground="#03f943",justify="right")

#botones

bot7=Button(marco,text="7",width=3)
bot7.grid(row=1,column=0)
bot8=Button(marco,text="8",width=3)
bot8.grid(row=1,column=1)
bot9=Button(marco,text="9",width=3)
bot9.grid(row=1,column=2)
botx=Button(marco,text="*",width=3)
botx.grid(row=1,column=3)

raiz.mainloop()