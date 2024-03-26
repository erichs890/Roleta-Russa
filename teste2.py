import tkinter as tk
from time import sleep

def desligarRegressivo():
    def ordemDecrescente(n: int):
        if n == 0:
            return "Tchau"
        else:
            countdown_label.config(text=str(n))
            root.update()
            sleep(1)
            return ordemDecrescente(n-1)

    tempo = int(entry.get())
    countdown_label.config(text=f"Contagem regressiva de {tempo} segundos")
    ordemDecrescente(tempo)

root = tk.Tk()
root.title("Contagem Regressiva")
root.geometry("300x200")

label = tk.Label(root, text="Digite em quantos segundos o PC vai desligar. Ex: 00, 01, 10")
label.pack()

entry = tk.Entry(root)
entry.pack()

start_button = tk.Button(root, text="Iniciar Contagem Regressiva", command=desligarRegressivo)
start_button.pack()

countdown_label = tk.Label(root, text="")
countdown_label.pack()

root.mainloop()
