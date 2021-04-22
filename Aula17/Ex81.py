lista = []
c = n = 0
co = 'S'
while True:
    while co == 'S':
        op = int(input('Digite um número: '))
        if c == 0 or op not in lista:
            lista.append(op)
        if op == 5:
            n += 1
        c += 1
        co = str(input('Deseja continuar? [S/N]: ')).upper()
        while co not in 'SsNn':
            co = str(input('Opção inválida, Digite [S/N]: '))
    break
lista.sort(reverse=True)
if c == 1:
    print('1 número foi digitado')
else:
    print(f'{c} números foram digitados')
print(lista)
if n == 1:
    print('O valor 5 foi digitado 1 vez')
elif n >= 2:
    print(f'O valor 5 foi digitado {n} vezes')
else:
    print('O número 5 não foi digitado.')