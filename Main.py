
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
eNome = Entry(tela, width=30).place(x=20,y=40)

#Campo: e-mail
tEmail= Label(tela, text="Insira um e-mail:").place(x=0,y=90)
eEmail= Entry(tela, width=30).place(x=20, y=130)

#Campo: Genero
tGenero = Label(text="Gênero").place(x=0,y=180)
eGenero = StringVar()
eGenero.set("Null")
opFeminino = Radiobutton(text="Feminino",variable=eGenero, value="Feminino").place(x=0,y=210) 
opMasculino = Radiobutton(text="Masculino",variable=eGenero,value="Masculino").place(x=0,y=250)


tela.mainloop()