
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo,showerror

# Configurando a janela 
tela = Tk()
tela.geometry('400x500')
tela.resizable(0,0)
tela.title("Formulário")


#Campo: nome
tNome = Label(tela,text="Insira um nome:").place(x=0,y=2)
eNome = Entry(tela, width=30).place(x=0,y=40)

#Campo: e-mail
tEmail= Label(tela, text="Insira um e-mail:").place(x=0,y=90)
eEmail= Entry(tela, width=30).place(x=0, y=130)


tela.mainloop()