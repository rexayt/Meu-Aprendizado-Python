from random import randint
from time import sleep
lista = []
c = int(input('Digite quantos jogos você quer sortear: '))
for r in range(1, c+1):
    lista = [[randint(0, 60)],[randint(0, 60)],[randint(0, 60)],[randint(0, 60)],[randint(0, 60)],[randint(0, 60)]]
    print(f'Jogo {r}: {lista}')
    lista.clear()
    sleep(1)