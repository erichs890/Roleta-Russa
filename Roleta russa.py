import os
from tkinter import *
import random
def desligar():
    os.system('shutdown -s -t 00')
def reiniciar():
    os.system('shutdown -r -t 00')
def fechar():
    os.system('taskkill /f /im python.exe')
def inicarRoleta():
    Desligar.configure(text="ROLETA RUSSA")
    DesligarBtn.forget()
    ReiniciarBtn.forget()
    FecharBtn.forget()
    Brincar.forget()
    Sortear.pack()
    Voltar.pack()
def voltar():
    Sortear.forget()
    Voltar.forget()
    DesligarBtn.pack()
    ReiniciarBtn.pack()
    Brincar.pack()
    FecharBtn.pack()
    Desligar.configure(text="Brincando de ser gerenciador de tarefas")
def tiro():
    
    if random.randint(0,6)== 3:
        Tchau = Label(text="tchau paizin")
        Tchau.pack()
        os.system('shutdown -s -t 01')

janela = Tk()
janela.geometry('300x300')
janela.title("Vishkkk")
Desligar = Label(janela, text="Brincando de ser gerenciador de tarefas")
Desligar.pack()

DesligarBtn = Button(janela, text="Desgligarkkkk", command= desligar)
DesligarBtn.pack()

ReiniciarBtn = Button(janela, text="Reiniciar", command= reiniciar)
ReiniciarBtn.pack()

Brincar = Button(janela, text="Iniciar roleta russa", command=inicarRoleta)
Brincar.pack()

Sortear = Button(janela, text="ATIRAR", command=tiro)
Voltar = Button(janela,text="Voltar", command=voltar)

FecharBtn = Button(janela, text= "Fechar o aplicativo", command= fechar)
FecharBtn.pack()

janela.mainloop()