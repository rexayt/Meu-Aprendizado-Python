from random import randint
from time import sleep
lista=[]
def ran():

    print('Sorteando 5 valores para a lista: ', end='')
    for c in range(0, 5):
        a = randint(0, 9)
        lista.append(a)
    for c in lista:
        print(c, end=' ', flush=True)
        sleep(0.5)
    print('Pronto!')
def som():
    par = 0
    print('Somando os valores pares de ', end='')
    for c in lista:
        print(c, end=' ', flush=True)
        if c % 2 == 0:
            par += c
        sleep(0.5)
    print(f', Temos: {par}')
    lista.clear()


