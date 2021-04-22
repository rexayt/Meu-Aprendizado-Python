def ficha(j='<Desconhecido>',g=0):
    print(f'O jogador {j}, fez {g} gols.')
j = str(input('Digite o nome do jogador: ')).strip().title()
g = str(input(f'Digite quantos gols {j} fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(j,g)