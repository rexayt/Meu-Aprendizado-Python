from random import randint
from time import sleep

def ale():
    lista=[]
    print('-='*20)
    a = randint(0, 9)
    for c in range(0, a):
        lista.append(randint(0, 9))
    ma=0
    for c in lista:
        if ma <= c:
            ma = c  
    print('Analisando os dados passados...')
    for c in lista:
        print(c, end=' ', flush=True)
        sleep(0.5)
    print(f'Foram informados {a} valores ao todo.')
    print(f'O maior dado informado foi {ma}.')


ale()