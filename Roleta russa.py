import os
from tkinter import *
from time import sleep
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
    Regressivo.forget()
def voltar():
    Sortear.forget()
    Voltar.forget()
    Segundos.forget()
    SegundosInput.forget()
    DesligarSec.forget()
    ReiniciarSec.forget()
    DesligarBtn.pack()
    ReiniciarBtn.pack()
    Brincar.pack()
    Regressivo.pack()
    FecharBtn.pack()
    Desligar.configure(text="Brincando de ser gerenciador de tarefas")
def tiro():
    if random.randint(0,6)== 3:
        Tchau = Label(text="tchau paizin")
        Tchau.pack()
        os.system('shutdown -s -t 01')
def regressivo():
    Desligar.configure(text="Em quantos segundos você quer desligar/reiniciar o pc")
    DesligarBtn.forget()
    Regressivo.forget()
    ReiniciarBtn.forget()
    FecharBtn.forget()
    Brincar.forget()
    Segundos.pack()
    SegundosInput.pack()
    ReiniciarSec.pack()
    DesligarSec.pack()
    Voltar.pack()
    countdown_label.pack()
    
def DesligarSegundos():
    tempo = int(SegundosInput.get())
    os.system(f'shutdown -s -t {tempo}')
    def ordemDecrescente(n: int):
        if n == 0:
            return "Tchau"
        else:
            countdown_label.config(text=str(n))
            janela.update()
            sleep(1)
            return ordemDecrescente(n-1)
    countdown_label.config(text=f"Contagem regressiva de {tempo} segundos")
    ordemDecrescente(tempo)

def ReiniciarSegundos():
    tempo = int(SegundosInput.get())
    os.system(f'shutdown -r -t {tempo}')
    def ordemDecrescente(n: int):
        if n == 0:
            return "Tchau"
        else:
            countdown_label.config(text=str(n))
            janela.update()
            sleep(1)
            return ordemDecrescente(n-1)
    countdown_label.config(text=f"Contagem regressiva de {tempo} segundos")
    ordemDecrescente(tempo)

    
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

Regressivo = Button(janela,text="Em quantos segundos quer desligar", command=regressivo)
Regressivo.pack()

Segundos = Label(text='Digite os segundos ')
SegundosInput = Entry()
countdown_label = Label(text="")


ReiniciarSec = Button(janela, text='Reiniciar', command=ReiniciarSegundos)
DesligarSec = Button(janela,text="Desligar", command=DesligarSegundos)
FecharBtn = Button(janela, text= "Fechar o aplicativo", command= fechar)
FecharBtn.pack()

janela.mainloop()