
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
tEmail= Label(tela, text="Insira um e-mail:").place(x=0,y=70)# diferença de 38 do de baixo
eEmail= Entry(tela, width=30).place(x=20, y=108)# diferença de 30 do de baixo


#Campo: Telefone
tTelefone = Label(tela, text="Insira um telefone:").place(x=0,y=138)
eTelefone = Entry(tela,width=30).place(x=20,y=178)# Tem que ser um número com 9 caracteres


#Campo: Genero
tGenero = Label(tela,text="Gênero").place(x=0,y=210)# diferença de 30 para cada opção
eGenero = StringVar()
eGenero.set("Null")
opFeminino = Radiobutton(text="Feminino",variable=eGenero, value="Feminino").place(x=0,y=240) 
opMasculino = Radiobutton(text="Masculino",variable=eGenero,value="Masculino").place(x=0,y=270)

#Campo: Observações
tObs= Label(tela,text="Observações",fg="red").place(x=0,y=310)
eObs=Entry(tela).place(x=20,y=345, width=350,height=50)
tela.mainloop()