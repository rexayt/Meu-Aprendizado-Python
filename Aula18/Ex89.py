lista = []
alunos = []
o = 'Ss'
cont = média = 0
while o in 'Ss':
    lista.append(str(input('Nome: ')))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    alunos.append(lista[:])
    lista.clear()
    cont += 1
    o = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while o not in 'SsNn':
        o = str(input('Comando inválido, Digite S ou N: ')).upper().strip()
print('-='*30)
print('No.    NOME    MÉDIA')
print('-'*22)
for c in range(0, cont):
    média = (alunos[c][1] + alunos[c][2]) / 2
    print(f'{c}     {alunos[c][0]:^5}     {média:^2.1f}')
o = 0
print('-'*22)
while True:
    o = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if o == 999:
        break
    print(f'Notas de {alunos[o][0]} são: [{alunos[c][1]}, {alunos[c][2]}]')