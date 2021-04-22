jogador={}
gols = []
jogador['Nome']=str(input('Digite o nome do jogador: '))
p = int(input(f'Digite quantas partidas {jogador["Nome"]} jogou: '))
for v in range(0, p):
    gols.append(int(input(f'Digite quantos gols pedro fez na {v+1} partida: ')))
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["Nome"]} jogou {len(jogador["Gols"])} partidas.')
for c in range(0, p):
    print(f'   ==> Na partida {c+1}, fez {jogador["Gols"][c]} gols.')
print(f'Foi um total de {jogador["Total"]} gols')
