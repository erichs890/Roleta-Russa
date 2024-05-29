import os
import random
from tkinter import *

def desligar():
    os.system('shutdown -s -t 00')

def desligarLinux():
    os.system('shutdown now')

def reiniciar():
    os.system('shutdown -r -t 00')

def reiniciarLinux():
    os.system('reboot')

def fechar():
    janela.quit()

def fecharLinux():
   janela.quit()

def iniciar_roleta():
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
    if random.randint(0,6) == 3:
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

def desligar_segundos():
    tempo = int(SegundosInput.get())
    os.system(f'shutdown -s -t {tempo}')
    def ordem_decrescente(n: int):
        if n == 0:
            return "Tchau"
        else:
            countdown_label.config(text=str(n))
            janela.update()
            janela.after(1000, lambda: ordem_decrescente(n-1))
    countdown_label.config(text=f"Contagem regressiva de {tempo} segundos")
    ordem_decrescente(tempo)
def reiniciar_segundos():
    tempo = int(SegundosInput.get())
    os.system(f'shutdown -r -t {tempo}')
    def ordem_decrescente(n: int):
        if n == 0:
            return "Tchau"
        else:
            countdown_label.config(text=str(n))
            janela.update()
            janela.after(1000, lambda: ordem_decrescente(n-1))
    countdown_label.config(text=f"Contagem regressiva de {tempo} segundos")
    ordem_decrescente(tempo)

def botoesWindows():
    # Define todas as funcionalidades após pressionar o botão "Windows"
    BotaoWindows.forget()
    DesligarBtn.pack()
    ReiniciarBtn.pack()
    Brincar.pack()
    Regressivo.pack()
    FecharBtn.pack()
def botoesLinux():
    BotaoLinux.forget()
    BotaoWindows.forget()
    DesligarLinuxBtn.pack()
    ReiniciarLinuxBtn.pack()   
    FecharLinuxBtn.pack() 

janela = Tk()
janela.geometry('300x300')
janela.title("Vishkkk")

BotaoWindows = Button(janela, text="Windows", command=botoesWindows)
BotaoWindows.pack()
BotaoLinux = Button(janela, text="Linux", command=botoesLinux)
BotaoLinux.pack()

Desligar = Label(janela, text="Brincando de ser gerenciador de tarefas")
DesligarBtn = Button(janela, text="Desligar", command=desligar)
ReiniciarBtn = Button(janela, text="Reiniciar", command=reiniciar)
Brincar = Button(janela, text="Iniciar roleta russa", command=iniciar_roleta)
Sortear = Button(janela, text="ATIRAR", command=tiro)
Voltar = Button(janela, text="Voltar", command=voltar)
Regressivo = Button(janela, text="Em quantos segundos quer desligar", command=regressivo)
Segundos = Label(janela, text='Digite os segundos ')
SegundosInput = Entry()
countdown_label = Label(janela, text="")
ReiniciarSec = Button(janela, text='Reiniciar', command=reiniciar_segundos)
DesligarSec = Button(janela, text="Desligar", command=desligar_segundos)
FecharBtn = Button(janela, text="Fechar o aplicativo", command=fechar)


DesligarLinuxBtn = Button(janela, text="Desligar", command=desligarLinux)
ReiniciarLinuxBtn = Button(janela, text="Reiniciar", command=reiniciarLinux)
FecharLinuxBtn = Button(janela, text="Fechar o aplicativo", command=fecharLinux)

janela.mainloop()