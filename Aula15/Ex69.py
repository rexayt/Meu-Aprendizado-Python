i = s = c = co = con = t = 0
print('-='*15)
while True:
    s = str(input('Digite o seu sexo [F/ M]: ')).strip().upper()
    if s not in 'FfMm':
        s = str(input('Comando inválido.\nDigite o seu sexo [F/ M]: '))
    i = int(input('Digite a sua idade: '))
    if i > 100 and i <= 0:
        i = int(input('Digite uma idade válida.\nDigite sua idade: '))
    else:
        if s in 'Mm':
            c += 1
        elif i >= 18:
            co += 1
        elif s in 'Ff' and i <= 19:
            con += 1        
    t = str(input('Deseja continuar? [S/ N]: ')).strip().upper()
    while t not in 'SsNn':
        t = str(input('Comando inválido\nDeseja continuar? [S/ N]: ')).strip().upper()
    if t in 'Nn':
        break
    print('--'*15)
print('-='*15)
print(f'{c} pessoas tem mais de 18 anos\n{co} Homens foram registrados\n{con} Mulheres tem menos de 20 anos.')