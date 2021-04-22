lista = []
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print('Esse número já foi digitado')
    else:
        lista.append(num)
    p = str(input('Deseja continuar? [S/N]: '))
    if p in 'Nn':
        break
lista.sort()
print(lista)
        