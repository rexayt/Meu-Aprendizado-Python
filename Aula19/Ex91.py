from random import randint
from time import sleep
from operator import itemgetter
dicionário = {'Jogador 1': randint(0, 6), 'Jogador 2': randint(0, 6), 'Jogador 3': randint(0, 6), 'Jogador 4': randint(0, 6)}
lista = []
for k, v in dicionário.items():
    print(f'{k} jogou {v} no dado')
    sleep(0.5)
lista = sorted(dicionário.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(lista):
    print(f'{k+1} lugar: {v[0]} com {v[1]}')
    sleep(0.5)