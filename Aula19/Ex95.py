lista=list()
dic=dict()
joojs = list()
gols=list()
while True:
    while True:    
        dic.clear
        gols.clear
        dic['Nome']=str(input('Digite o nome do jogador: '))
        p = int(input(f'Quantos jogos {dic["Nome"]} jogou: '))
        for c in range(0, p):
            gols.append(int(input(f'Digite quantos gols {dic["Nome"]} fez no {c+1}° jogo: ')))
        dic['Gols'] = gols[:]
        dic['Total']= sum(gols[:])
        dic['Jogos']= p
        lista.append(dic.copy())
        co = str(input('Deseja continuar? [S/N]: ')).upper().strip()[0]
        while co not in 'SN':
            co = str(input('Comando inválido, digite [S/N]: ')).upper().strip()[0]
        if co == 'N':
            break
    break
print('-='*30)
print(' Cod ', end='')
for i in dic.keys():
    print(f'{i:<15}', end='')
print()
print('-='*30)
for k, v in enumerate(lista):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
while True:
    o = int(input('Deseja mostrar os dados de qual jogador? (999 interrompe): '))
    if o == 999:
        break
    if o >= len(lista):
        o = int(input(f'Comando inválido só existem {len(lista)} jogadores, Digite novamente (999 interrompe): '))
    else:
        print(f'Partidas do jogador {lista[o]['Nome']}')
    for i, g in enumerate(lista[o]['Gols']):
        print(f'   No jogo {i+1} fez {g} gols.')
print('-='30)