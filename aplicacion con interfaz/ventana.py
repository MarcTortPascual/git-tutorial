import builtins
from tkinter import *

raiz=Tk()
marco=Frame(raiz)
marco.pack()

indi=StringVar()



textname=Label(marco)
textname.config(text="nombre:")

textname.grid(row=2,column=2,sticky="e")

entradaname=Entry(marco,textvariable=indi)
entradaname.grid(row=2,column=3,padx=3)

textapellido=Label(marco,text="apellido:")
textapellido.grid(row=3,column=2,sticky="e")

entradapellido=Entry(marco)
entradapellido.grid(row=3,column=3,padx=3)

textapellido=Label(marco,text="direcion:")
textapellido.grid(row=4,column=2,sticky="e")

entradapellido=Entry(marco)
entradapellido.grid(row=4,column=3,padx=3)


comentariotext=Label(marco,text="comentario:")
comentariotext.grid(row=5,column=2,sticky="e")

comentario=Text(marco)
bara=Scrollbar(marco,command=comentario.yview)
bara.grid(row=5,column=4,sticky="nsew")


comentario.config(width=16,height=5,yscrollcommand=bara.set)
comentario.grid(row=5,column=3,padx=3,pady=4)

def codigo():
    indi.set("hola introduce tu nombre")


boton=Button(raiz,text="pincha",command=codigo)
boton.pack()



raiz.mainloop()
