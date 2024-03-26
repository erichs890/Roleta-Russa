import os
from time import sleep
def desligarRegressivo():
    def ordemDecrescente(n: int):
        if n == 0:
            return "Tchau"
        else:
            print(n)
            sleep(1)
            return ordemDecrescente(n-1)


    tempo = int(input("Digite em quantos segudos o pc vai desligar. Ex: 00, 01, 10\n" ))

    print(f"Contagem regressiva de {tempo} segundos")

    print(ordemDecrescente(tempo))
desligarRegressivo()