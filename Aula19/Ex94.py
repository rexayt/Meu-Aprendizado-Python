dic = dict()
lista = list()
m = list()
c = ''
ida = me = 0
while True:
    while True:
        dic['Nome']=str(input('Digite o nome da pessoa: '))
        dic['Sexo']=str(input('Digite o sexo da pessoa: [M/F]: ')).upper().strip()[0]
        while dic['Sexo'] not in 'MmFf':
            dic['Sexo']=str(input('Comando inválido, digite [M/F]: ')).upper().strip()[0]
        if dic['Sexo'] == 'F':
            m.append(dic['Nome'])
        dic['Idade']=int(input('Digite a idade da pessoa: '))
        c = str(input('Deseja continuar? [S/N] ')).upper().strip()
        while c not in 'SsNn':
            c = str(input('Comando inválido, digite [S/N] ')).upper().strip()
        lista.append(dic.copy())
        ida+=dic['Idade']
        dic.clear
        if c == 'N':
            break
    me = ida / len(lista)
    break
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
print(f'B) A média da idade do grupo é {me:5.2f}')
print(f'C) As mulheres cadastradas foram:',end=' ')
for c in m:
    print(f'{c} ', end='')
print()
print(f'D) Listas das pesoas que estão acima da média: ')
for p in lista:
    if p['Idade'] >= me:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()